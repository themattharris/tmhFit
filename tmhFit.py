import struct

class tmhFit():
  MIN_HEADER_SIZE=12

  def __init__(self):
    self._bytepointer = 0

  @staticmethod
  def calculate_crc(crc, byte):
    # page 14 of Flexible and Interoperable Data Transfer Protocol Rev 2.4
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

  def read_bytes_from_pointer(self, bytes_to_read, fmt, data=None):
    if data is None:
      data = self._content

    read_bytes = data[self._bytepointer:self._bytepointer+bytes_to_read]
    self._bytepointer = self._bytepointer + bytes_to_read

    return struct.unpack(fmt, read_bytes)
  
  def read_header(self):
    # page 14 of Flexible and Interoperable Data Transfer Protocol Rev 2.4
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
        raise "Invalid file header. expected at least 2 CRC bytes but got less"
      crc_bytes = self.read_bytes_from_pointer(2, "H")

      # spec says the header can grow in the future but no definition as to what. read them for now but ignore
      other_header = self.read_bytes_from_pointer(header_remaining-2, "B")

    self._header = {
      'header_size': header_size,
      'protocol_version': float("%d.%d" % (protocol_version >> 4, protocol_version & ((1 << 4) - 1))),
      'profile_version': float("%d.%d" % (profile_version / 100, profile_version % 100)),
      'data_size': data_size,
      'data_type': data_type,
      'crc': crc_bytes
    }

  def read_data_records(self):
    self._records = []
    bytes_left = self._header['data_size']

    # this is per message
    # read the record header
    record_header = self.read_record_header_byte()
    
    if record_header['message_type'] is True:
      # definition record next
      self.read_record_definition()
    else:
      # data record next
      self.read_data()

  def read_record_header_byte(self):
    # page 17 of Flexible and Interoperable Data Transfer Protocol Rev 2.4
    # Bit   Value         Description
    # 7     0             Normal Header
    # 6     0 or 1        Message Type: 1: Definition, 0: Data
    # 5     0 (default)   Message Type Specific
    # 4     0             Reserved
    # 0-3   0-15          Local Message Type
    record_header = self.read_bytes_from_pointer(1, "B")[0]
    return {
      'normal_header': bool(record_header & 0x80),
      'message_type': bool(record_header & 0x40),
      'message_type_specific': bool(record_header & 0x20),
      'reserved': record_header & 0x10,
      'local_message_type': record_header & 0xF
    }

  def read_record_definition(self):
    # page 23 of Flexible and Interoperable Data Transfer Protocol Rev 2.4
    # Byte                    Description                   Length              Value
    # 0                       Reserved                      1 Byte              0
    # 1                       Architecture                  1 Byte              0 if Little Endian, 1 if Big Endian
    # 2-3                     Global Message Number         2 Bytes             Unique to message
    # 4                       Fields                        1 Byte              # of fields in the data message
    # 5 - 4 + Fields * 3      Field Definition              3 Bytes/Field       
    # 5 + Fields * 3          # Developer Fields            1 Byte              # of self descriptive fields in the data message
    # 6 + Fields * 3 - END    Developer Field Definition    3 Bytes/Field

    # we need to read the first 2 bytes to know the endian
    reserved, architecture = self.read_bytes_from_pointer(2, "BB")
    endian = '>' if architecture == 1 else '<'

    # next 3 bytes tell us the global message number and number of fields
    global_message_num, field_count = self.read_bytes_from_pointer(3, "{}HB".format(endian))

    # read the fields
    # TODO convert global message number
    print(field_count)
    for i in range(field_count):
      # page 23 of Flexible and Interoperable Data Transfer Protocol Rev 2.4
      # Byte   Description
      # 0      Field Definition Num
      # 1      Size
      # 2      Base Type
      field_def_num, field_size, field_base_type = self.read_bytes_from_pointer(3, "{}3B".format(endian))
      print('{}-{}-{}'.format(field_def_num, field_size, field_base_type))


filename = './fixtures/Activity.fit'
tmhFit = tmhFit()
tmhFit_content = tmhFit.open_file(filename)

tmh_header = tmhFit.read_header()
tmh_records = tmhFit.read_data_records()