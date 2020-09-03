# script to convert Profile.xslx profile sheet exported as CSV to python constants
import csv
import os
import sys

class ProfileToPy():
  DEFAULT_OUTPUT='../profile.py'
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
            'basetype': row[1],
            'values': []
          }
          continue

        # if we're here, we have values
        name = row[2]
        if name[0].isdigit():
          name = "_{}".format(name)

        if len(name) > self.MAX_NAME_LEN:
          self.MAX_NAME_LEN = len(name) + 1
        
        everything[current_type]['values'].append({
          'name': name,
          'value': row[3],
          'comment': row[4]
        })

    return self.possibly_add_bool(everything)

  def possibly_add_bool(self, everything):
    # as of SDK 21.32 the bool field type is still not included in the profile
    # so check for it, and if it's not present, add it in
    if not 'bool' in everything:
      everything['bool'] = {
        'basetype': 'enum',
        'values': [
          {
            'name': 'false',
            'value': '0',
            'comment': "absent from profile. added artificially"
          },
          {
            'name': 'true',
            'value': '1',
            'comment': "absent from profile. added artificially"
          }
        ]
      }
      everything = dict(sorted(everything.items()))
    return everything

  def output_header(self):
    return '''### THIS FILE IS AUTO-GENERATED ###
# Garmin FIT message types from profile.xslx in the SDK
# Version: FitSDKRelease_21.32.00
import basetypes
from enum import Enum, unique
'''

  def basetype_block(self, basetype):
    return '''
  @staticmethod
  def basetype():
    return basetypes.{}
'''.format(basetype)

  def write_to_output(self, content_dict, output_py):
    with open(output_py, 'w') as outfile:
      outfile.write(self.output_header())

      for profile_type, meta in content_dict.items():
        outfile.write("\n")
        outfile.write('class {}(Enum):\n'.format(profile_type))

        for value in meta['values']:
          row = '  {name:{width}}= {val:8}'.format(name=value['name'], width=self.MAX_NAME_LEN, val=value['value'])
          if len(value['comment']) > 0:
            row = '{}# {}'.format(row, value['comment'])
          outfile.write("{}\n".format(row))

        outfile.write(self.basetype_block(meta['basetype']))

  def main(self, input_csv, output_py):
    if not os.path.exists(input_csv):
      print("{} does not exist. Quitting".format(input_csv))

    content = self.parse_csv(input_csv)
    self.write_to_output(content, output_py)




if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: {} profile.csv [../profile.py]'.format(os.path.basename(__file__)))
    sys.exit(0)

  csvin = sys.argv[1]
  out = sys.argv[2] if len(sys.argv) == 3 else ProfileToPy.DEFAULT_OUTPUT
  
  ptp = ProfileToPy()
  ptp.main(csvin, out)