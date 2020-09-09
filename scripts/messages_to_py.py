# script to convert Profile.xslx messages sheet exported as CSV to python objects
import csv
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import basetypes

class MessagesToPy():
  CONSTS_OUTPUT='../messages.py'
  META_OUTPUT='../messages_meta.py'
  MAX_NAME_LEN = 0

  def parse_csv(self, input_csv):
    with open(input_csv) as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')

      is_header = True
      current_type = ''
      everything = {}

      for row in reader:
        if is_header:
          is_header = False
          continue

        # first column has a string then we're in a new type
        if len(row[0]) > 0:
          current_type = row[0]
          everything[current_type] = {
            'comment': row[13],
            'values': []
          }
          continue

        # second column has a string then we're reading a field definition
        if len(row[1]) > 0:
          name = row[2]
          if len(name) > self.MAX_NAME_LEN:
            self.MAX_NAME_LEN = len(name) + 1

          everything[current_type]['values'].append({
            'defnum': row[1],
            'name': name,
            'type': row[3],
            'array': row[4],
            'components': row[5],
            'scale': row[6],
            'offset': row[7],
            'units': row[8],
            'bits': row[9],
            'accumulate': row[10],
            'reffieldname': row[11],
            'reffieldvalue': row[12],
            'comment': row[13],
            'products': row[14]
          })
    return everything

  def output_header(self):
    return '''### THIS FILE IS AUTO-GENERATED ###
# Garmin FIT message types from profile.xslx in the SDK
# Version: FitSDKRelease_21.32.00
import basetypes
import profile
import sys
'''

  def output_header_extra(self):
    return 'from enum import Enum, unique\n'

  def output_header_functions(self):
    return '''
def by_name(name):
  return sys.modules[__name__].__getattribute__(name)
'''

  def write_consts_to_output(self, content_dict, output_py):
    with open(output_py, 'w') as outfile:
      outfile.write(self.output_header())
      outfile.write(self.output_header_extra())
      outfile.write(self.output_header_functions())

      for message_type, meta in content_dict.items():
        outfile.write("\n")
        outfile.write("@unique\n")
        outfile.write('class {}(Enum):\n'.format(message_type))
        if len(meta['comment']) > 0:
          outfile.write('  # {}\n'.format(meta['comment']))

        for value in meta['values']:
          row = '  {name:{width}}= {val:8}'.format(name=value['name'], width=self.MAX_NAME_LEN, val=value['defnum'])
          if len(value['comment']) > 0:
            row = '{}# {}'.format(row, value['comment'])
          outfile.write("{}\n".format(row))

  def write_meta_to_output(self, content_dict, output_py):
    with open(output_py, 'w') as outfile:
      outfile.write(self.output_header())
      outfile.write(self.output_header_functions())

      for message_type, meta in content_dict.items():
        outfile.write("\n")
        outfile.write('class {}():\n'.format(message_type))

        for values in meta['values']:
          block = "  {} = {{\n".format(values['name'])

          for k, v in values.items():
            if k in ['defnum', 'name', 'comment']:
              continue

            if k == 'type':
              try:
                if basetypes.Field[v]:
                  v = 'basetypes.Field.{}'.format(v)
              except KeyError as e:
                v = 'profile.{}'.format(v)
                pass
            elif k in ['offset']:
              v = v if v.isdigit() else 0
            elif k in ['scale']:
              v = v if v.isdigit() else 1
            elif k in ['units']:
              v = v if len(v) > 0 else ""
              v = '"{}"'.format(v.replace("\n", " "))
            # is this one of the nested component types?
            elif len(v) > 0 and len(v.split(',')) > 0:
              # TODO handle this better - explode as sub components?
              v = '"{}"'.format(v.replace("\n", " "))
            elif len(v) > 0:
              v = "'{}'".format(v)
            else:
              continue

            k = "'{}'".format(k)
            block = block + "    {:16}: {},\n".format(k, v)
          block = block + '  }'
          outfile.write("{}\n".format(block))

  def main(self, input_csv):
    if not os.path.exists(input_csv):
      print("{} does not exist. Quitting".format(input_csv))

    content = self.parse_csv(input_csv)
    self.write_consts_to_output(content, self.CONSTS_OUTPUT)
    self.write_meta_to_output(content, self.META_OUTPUT)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: {} messages.csv'.format(os.path.basename(__file__)))
    sys.exit(0)

  csvin = sys.argv[1]
  mtp = MessagesToPy()
  mtp.main(csvin)