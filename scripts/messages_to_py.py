# script to convert Profile.xslx messages sheet exported as CSV to python objects
import csv
import os
import sys

class MessagesToPy():
  DEFAULT_OUTPUT='../messages.py'
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
    return '''# Garmin FIT message types from profile.xslx in the SDK
# Version: FitSDKRelease_21.32.00
import basetypes
from enum import Enum, unique
'''

  def write_to_output(self, content_dict, output_py):
    with open(output_py, 'w') as outfile:
      outfile.write(self.output_header())

      for message_type, meta in content_dict.items():
        outfile.write("\n")
        outfile.write('class {}(Enum):\n'.format(message_type))
        if len(meta['comment']) > 0:
          outfile.write(' # {}\n'.format(meta['comment']))

        for value in meta['values']:
          row = '  {name:{width}}= {val:8}'.format(name=value['name'], width=self.MAX_NAME_LEN, val=value['defnum'])
          if len(value['comment']) > 0:
            row = '{}# {}'.format(row, value['comment'])
          outfile.write("{}\n".format(row))

  def main(self, input_csv, output_py):
    if not os.path.exists(input_csv):
      print("{} does not exist. Quitting".format(input_csv))

    content = self.parse_csv(input_csv)
    self.write_to_output(content, output_py)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: {} messages.csv [../messages.py]'.format(os.path.basename(__file__)))
    sys.exit(0)

  csvin = sys.argv[1]
  out = sys.argv[2] if len(sys.argv) == 3 else MessagesToPy.DEFAULT_OUTPUT
  
  mtp = MessagesToPy()
  mtp.main(csvin, out)