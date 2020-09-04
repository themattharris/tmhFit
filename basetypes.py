# Garmin FIT file base types, and invalid values
# Ref: Flexible and Interoperable Data Transfer Protocol Rev 2.4, Page 23
#
# Base Type #   Endian Ability   Base Type Field   Type Name     Invalid Value          Size (Bytes)   Comment
# 0             0                0x00              enum          0xFF                   1
# 1             0                0x01              sint8         0x7F                   1              2's complement format
# 2             0                0x02              uint8         0xFF                   1
# 3             1                0x83              sint16        0x7FFF                 2              2's complement format
# 4             1                0x84              uint16        0xFFFF                 2
# 5             1                0x85              sint32        0x7FFFFFFF             4              2's complement format
# 6             1                0x86              uint32        0xFFFFFFFF             4
# 7             0                0x07              string        0x00                   1              Null terminated string encoded in UTF-8 format
# 8             1                0x88              float32       0xFFFFFFFF             4
# 9             1                0x89              float64       0xFFFFFFFFFFFFFFFF     8
# 10            0                0x0A              uint8z        0x00                   1
# 11            1                0x8B              uint16z       0x0000                 2
# 12            1                0x8C              uint32z       0x00000000             4
# 13            0                0x0D              byte          0xFF                   1              Array of bytes. Field is invalid if all bytes are invalid.
# 14            1                0x8E              sint64        0x7FFFFFFFFFFFFFFF     8              2's complement format
# 15            1                0x8F              uint64        0xFFFFFFFFFFFFFFFF     8
# 16            1                0x90              uint64z       0x0000000000000000     8
from enum import Enum, unique

class Field(Enum):
  enum    = 0x00
  sint8   = 0x01
  uint8   = 0x02
  sint16  = 0x83
  uint16  = 0x84
  sint32  = 0x85
  uint32  = 0x86
  string  = 0x07
  float32 = 0x88
  float64 = 0x89
  uint8z  = 0x0A
  uint16z = 0x8B
  uint32z = 0x8C
  byte    = 0x0D
  sint64  = 0x8E
  uint64  = 0x8F
  uint64z = 0x90

class Size(Enum):
  enum    = 1
  sint8   = 1
  uint8   = 1
  sint16  = 2
  uint16  = 2
  sint32  = 4
  uint32  = 4
  string  = 1
  float32 = 4
  float64 = 8
  uint8z  = 1
  uint16z = 2
  uint32z = 4
  byte    = 1
  sint64  = 8
  uint64  = 8
  uint64z = 8

class FormatChar(Enum):
  enum    = 'B'
  sint8   = 'b'
  uint8   = 'B'
  sint16  = 'h'
  uint16  = 'H'
  sint32  = 'i'
  uint32  = 'I'
  string  = 's'
  float32 = 'f'
  float64 = 'd'
  uint8z  = 'B'
  uint16z = 'H'
  uint32z = 'I'
  byte    = 'B'
  sint64  = 'q'
  uint64  = 'Q'
  uint64z = 'Q'

class EndianAbility(Enum):
  enum    = 0
  sint8   = 0
  uint8   = 0
  sint16  = 1
  uint16  = 1
  sint32  = 1
  uint32  = 1
  string  = 0
  float32 = 1
  float64 = 1
  uint8z  = 0
  uint16z = 1
  uint32z = 1
  byte    = 0
  sint64  = 1
  uint64  = 1
  uint64z = 1

class InvalidValue(Enum):
  enum    = 0xFF
  sint8   = 0x7F
  uint8   = 0xFF
  sint16  = 0x7FFF
  uint16  = 0xFFFF
  sint32  = 0x7FFFFFFF
  uint32  = 0xFFFFFFFF
  string  = 0x00
  float32 = 0xFFFFFFFF
  float64 = 0xFFFFFFFFFFFFFFFF
  uint8z  = 0x00
  uint16z = 0x0000
  uint32z = 0x00000000
  byte    = 0xFF
  sint64  = 0x7FFFFFFFFFFFFFFF
  uint64  = 0xFFFFFFFFFFFFFFFF
  uint64z = 0x0000000000000000