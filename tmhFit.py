import copy
import struct
import basetypes
import profile
import messages
import messages_meta

class tmhFit():
  MIN_HEADER_SIZE=12
  EPOCH = 631065600  # timestamp for UTC 00:00 Dec 31 1989

  def __init__(self):
    self._byte_ptr = 0
    self._databyte_ptr = 0
    self._field_definitions = {}

  @staticmethod
  def calculate_crc(crc, byte):
    # Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 14
    crc_table = [
      0x0000, 0xCC01, 0xD801, 0x1400, 0xF001, 0x3C00, 0x2800, 0xE401,
      0xA001, 0x6C00, 0x7800, 0xB401, 0x5000, 0x9C01, 0x8801, 0x4400
    ]

    # compute checksum of lower four bits of byte
    tmp = crc_table[crc & 0xF]
    crc = (crc >> 4) & 0x0FFF
    crc = crc ^ tmp ^ crc_table[byte & 0xF]
    
    # now compute checksum of upper four bits of byte 
    tmp = crc_table[crc & 0xF]
    crc = (crc >> 4) & 0x0FFF
    crc = crc ^ tmp ^ crc_table[(byte >> 4) & 0xF]
    return crc

  def open_file(self, filename):
    with open(filename, mode='rb') as file:
      self._content = file.read()
    return self._content

  def read_data_bytes(self, bytes_to_read, fmt, data=None):
    self._databyte_ptr = self._databyte_ptr - bytes_to_read
    return self.read_bytes_from_pointer(bytes_to_read, fmt)

  def read_bytes_from_pointer(self, bytes_to_read, fmt, data=None):
    if data is None:
      data = self._content

    read_bytes = data[self._byte_ptr:self._byte_ptr+bytes_to_read]
    self._byte_ptr = self._byte_ptr + bytes_to_read

    return struct.unpack(fmt, read_bytes)
  
  def read_header(self):
    # Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 14
    # 0   Header Size             Indicates the length of this file header including header size. Min 12
    # 1   Protocol Version        Protocol version number as provided in SDK
    # 2   Profile Version LSB     Profile version number as provided in SDK
    # 3   Profile Version MSB
    # 4   Data Size LSB           Length of the Data Records section in bytes
    # 5   Data Size               Does not include Header or CRC
    # 6   Data Size
    # 7   Data Size MSB
    # 8   Data Type Byte[0]       ASCII values for “.FIT”. 
    # 9   Data Type Byte[1]
    # 10  Data Type Byte[2]
    # 11  Data Type Byte[3]
    # 12  CRC LSB                 Contains the value of the CRC (see section 3.3.2 ) of Bytes 0 through 11, or may be set to 0x0000. Optional
    # 13  CRC MSB
    header_size, protocol_version, profile_version, data_size, data_type = self.read_bytes_from_pointer(self.MIN_HEADER_SIZE, "2BHI4s")
    crc_bytes = 0

    header_remaining = header_size - self.MIN_HEADER_SIZE

    # do we have bytes left in the header?
    if header_remaining > 0:
      # need to have at least 2 bytes to calculate CRC
      if header_remaining < 2:
        raise SyntaxException("Invalid file header. expected at least 2 CRC bytes but got less")
      crc_bytes = self.read_bytes_from_pointer(2, "H")

      # spec says the header can grow in the future but no definition as to what. read them for now but ignore
      other_header = self.read_bytes_from_pointer(header_remaining-2, "B")

    self._header = {
      'header_size': header_size,
      'protocol_version': protocol_version,
      'profile_version': profile_version,
      'data_size': data_size,
      'data_type': data_type,
      'crc': crc_bytes
    }
    return self._header

  def read_data_records(self):
    self._records = []
    self._databyte_ptr = self._header['data_size']

    field_def = {}
    while self._databyte_ptr > 0:
      # read the record header
      record_header = self.read_record_header_byte()
      # message_type 1 is a definition, 0 is a data record. absence of message_type means compressed timestamp
      if record_header['normal_header'] == 0 and record_header['message_type'] == 1:
        self.read_record_definition(record_header)
      else:
        self._records.append(self.read_data(record_header))
    return self._records

  def read_record_header_byte(self):
    record_header = self.read_data_bytes(1, "B")[0]
    header = {
      'normal_header': (record_header & 0x80) >> 7
    }

    # normal_header 0 is normal, 1 is a compressed timestamp header
    if header['normal_header'] == 0:
      # Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 17
      # Bit   Value         Description
      # 7     0             Normal Header
      # 6     0 or 1        Message Type: 1: Definition, 0: Data
      # 5     0 (default)   Message Type Specific (Developer Data Flag for Normal Header)
      # 4     0             Reserved
      # 0-3   0-15          Local Message Type
      header = {**header, **{
        'message_type': (record_header & 0x40) >> 6,
        'message_type_specific': (record_header & 0x20) >> 5,
        'reserved': (record_header & 0x10) >> 4,
        'local_message_type': record_header & 0xF
      }}
    else:
      # Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 19
      # Bit   Value         Description
      # 7     1             Compressed Timestamp Header
      # 5-6   0-3           Local Message Type
      # 0-4   0-31          Time Offset (Seconds)
      header = {**header, **{
        'local_message_type': (record_header & 0x60) >> 5,
        'time_offset': record_header & 0x1F
      }}
    return header

  def read_record_definition(self, record_header):
    # Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 23
    # Byte                    Description                   Length              Value
    # 0                       Reserved                      1 Byte              0
    # 1                       Architecture                  1 Byte              0 if Little Endian, 1 if Big Endian
    # 2-3                     Global Message Number         2 Bytes             Unique to message
    # 4                       Fields                        1 Byte              # of fields in the data message
    # 5 - 4 + Fields * 3      Field Definition              3 Bytes/Field       
    # 5 + Fields * 3          # Developer Fields            1 Byte              # of self descriptive fields in the data message
    # 6 + Fields * 3 - END    Developer Field Definition    3 Bytes/Field

    # we need to read the first 2 bytes to know the endian
    reserved, architecture = self.read_data_bytes(2, "BB")
    endian = '>' if architecture == 1 else '<'

    # next 3 bytes tell us the global message number and number of fields
    global_message_num, field_count = self.read_data_bytes(3, "{}HB".format(endian))

    # lookup the message number in the profile
    message_type = profile.mesg_num(global_message_num).name

    # lookup the profiles field defs in the messages profile
    field_defs = messages.by_name(message_type)

    # read the fields
    definition = []
    for i in range(field_count):
      # Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 23
      # Byte   Description
      # 0      Field Definition Num
      # 1      Size
      # 2      Base Type
      field_def_num, field_size, field_base_type = self.read_data_bytes(3, "{}3B".format(endian))

      field_base_type = basetypes.Field(field_base_type).name
      if not basetypes.Size[field_base_type].value == field_size:
        raise ValueError("Invalid field size for {} of type '{}', excepected multiple of {} bytes".format(field_def_num, field_base_type, basetypes.Size[field_base_type]))

      name = field_defs(field_def_num).name
      meta = getattr(messages_meta.by_name(message_type), name)

      definition.append({
        'message_type': message_type,
        'number': field_def_num,
        'name': name,
        'bytes': field_size,
        'units': meta['units'] if 'units' in meta.keys() else '',
        'scale': meta['scale'] if 'scale' in meta.keys() else 1,
        'offset': meta['offset'] if 'offset' in meta.keys() else 0,
        'type': field_base_type,
        'pattern': basetypes.FormatChar[field_base_type].value,
        'endian': endian
      })
    self._field_definitions[record_header['local_message_type']] = definition

  def read_data(self, record_header):
    definition = self._field_definitions[record_header['local_message_type']]
    record = {}

    pattern = self.definition_to_struct(definition)
    size = struct.calcsize(pattern)

    fields = [field['name'] for field in definition]
    data = self.read_data_bytes(size, "{}{}".format(definition[0]['endian'], pattern))
    record = list(zip(fields, data))

    for r in record:
      record['value'] = self.process_record(record['value'])

    # need to do field validity checks and set values to defaults if invalid
    # need to set accumulators
    # need to process developer fields
    return definition

  def process_record(self, record):
    # data fields need formatting based on the standards in the SDK
    if record['type'] == profile.date_time:
      # adjust timestamp due to custom epoch
      record['value'] = record['value'] - self.EPOCH

    # scale, then offset
    if 'scale' in record and record['scale'] > 1:
      record['value'] = float(record['value']/record['scale'])

    if 'offset' in record and record['offset'] > 0:
      record['value'] = float(record['value']) - record['offset']
    return record


  def definition_to_struct(self, definition):
    _struct = ""
    for field in definition:
      _struct = _struct + field['pattern']
    return _struct


filename = './fixtures/Activity.fit'
tmhFit = tmhFit()
tmhFit_content = tmhFit.open_file(filename)

tmh_header = tmhFit.read_header()
tmh_records = tmhFit.read_data_records()

for r in tmh_records:
  for i in r:
    print("{}: {} {}".format(i['name'], i['value'], i['units']))
  print("\n")