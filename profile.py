# Garmin FIT message types from profile.xslx in the SDK
# Version: FitSDKRelease_21.32.00
import basetypes
from enum import Enum, unique

class file(Enum):
  device                                                   = 1       # Read only, single file. Must be in root directory.
  settings                                                 = 2       # Read/write, single file. Directory=Settings
  sport                                                    = 3       # Read/write, multiple files, file number = sport type. Directory=Sports
  activity                                                 = 4       # Read/erase, multiple files. Directory=Activities
  workout                                                  = 5       # Read/write/erase, multiple files. Directory=Workouts
  course                                                   = 6       # Read/write/erase, multiple files. Directory=Courses
  schedules                                                = 7       # Read/write, single file. Directory=Schedules
  weight                                                   = 9       # Read only, single file. Circular buffer. All message definitions at start of file. Directory=Weight
  totals                                                   = 10      # Read only, single file. Directory=Totals
  goals                                                    = 11      # Read/write, single file. Directory=Goals
  blood_pressure                                           = 14      # Read only. Directory=Blood Pressure
  monitoring_a                                             = 15      # Read only. Directory=Monitoring. File number=sub type.
  activity_summary                                         = 20      # Read/erase, multiple files. Directory=Activities
  monitoring_daily                                         = 28      
  monitoring_b                                             = 32      # Read only. Directory=Monitoring. File number=identifier
  segment                                                  = 34      # Read/write/erase. Multiple Files.  Directory=Segments
  segment_list                                             = 35      # Read/write/erase. Single File.  Directory=Segments
  exd_configuration                                        = 40      # Read/write/erase. Single File. Directory=Settings
  mfg_range_min                                            = 0xF7    # 0xF7 - 0xFE reserved for manufacturer specific file types
  mfg_range_max                                            = 0xFE    # 0xF7 - 0xFE reserved for manufacturer specific file types

  @staticmethod
  def basetype():
    return basetypes.enum

class mesg_num(Enum):
  file_id                                                  = 0       
  capabilities                                             = 1       
  device_settings                                          = 2       
  user_profile                                             = 3       
  hrm_profile                                              = 4       
  sdm_profile                                              = 5       
  bike_profile                                             = 6       
  zones_target                                             = 7       
  hr_zone                                                  = 8       
  power_zone                                               = 9       
  met_zone                                                 = 10      
  sport                                                    = 12      
  goal                                                     = 15      
  session                                                  = 18      
  lap                                                      = 19      
  record                                                   = 20      
  event                                                    = 21      
  device_info                                              = 23      
  workout                                                  = 26      
  workout_step                                             = 27      
  schedule                                                 = 28      
  weight_scale                                             = 30      
  course                                                   = 31      
  course_point                                             = 32      
  totals                                                   = 33      
  activity                                                 = 34      
  software                                                 = 35      
  file_capabilities                                        = 37      
  mesg_capabilities                                        = 38      
  field_capabilities                                       = 39      
  file_creator                                             = 49      
  blood_pressure                                           = 51      
  speed_zone                                               = 53      
  monitoring                                               = 55      
  training_file                                            = 72      
  hrv                                                      = 78      
  ant_rx                                                   = 80      
  ant_tx                                                   = 81      
  ant_channel_id                                           = 82      
  length                                                   = 101     
  monitoring_info                                          = 103     
  pad                                                      = 105     
  slave_device                                             = 106     
  connectivity                                             = 127     
  weather_conditions                                       = 128     
  weather_alert                                            = 129     
  cadence_zone                                             = 131     
  hr                                                       = 132     
  segment_lap                                              = 142     
  memo_glob                                                = 145     
  segment_id                                               = 148     
  segment_leaderboard_entry                                = 149     
  segment_point                                            = 150     
  segment_file                                             = 151     
  workout_session                                          = 158     
  watchface_settings                                       = 159     
  gps_metadata                                             = 160     
  camera_event                                             = 161     
  timestamp_correlation                                    = 162     
  gyroscope_data                                           = 164     
  accelerometer_data                                       = 165     
  three_d_sensor_calibration                               = 167     
  video_frame                                              = 169     
  obdii_data                                               = 174     
  nmea_sentence                                            = 177     
  aviation_attitude                                        = 178     
  video                                                    = 184     
  video_title                                              = 185     
  video_description                                        = 186     
  video_clip                                               = 187     
  ohr_settings                                             = 188     
  exd_screen_configuration                                 = 200     
  exd_data_field_configuration                             = 201     
  exd_data_concept_configuration                           = 202     
  field_description                                        = 206     
  developer_data_id                                        = 207     
  magnetometer_data                                        = 208     
  barometer_data                                           = 209     
  one_d_sensor_calibration                                 = 210     
  set                                                      = 225     
  stress_level                                             = 227     
  dive_settings                                            = 258     
  dive_gas                                                 = 259     
  dive_alarm                                               = 262     
  exercise_title                                           = 264     
  dive_summary                                             = 268     
  jump                                                     = 285     
  climb_pro                                                = 317     
  mfg_range_min                                            = 0xFF00  # 0xFF00 - 0xFFFE reserved for manufacturer specific messages
  mfg_range_max                                            = 0xFFFE  # 0xFF00 - 0xFFFE reserved for manufacturer specific messages

  @staticmethod
  def basetype():
    return basetypes.uint16

class checksum(Enum):
  clear                                                    = 0       # Allows clear of checksum for flash memory where can only write 1 to 0 without erasing sector.
  ok                                                       = 1       # Set to mark checksum as valid if computes to invalid values 0 or 0xFF.  Checksum can also be set to ok to save encoding computation time.

  @staticmethod
  def basetype():
    return basetypes.uint8

class file_flags(Enum):
  read                                                     = 0x02    
  write                                                    = 0x04    
  erase                                                    = 0x08    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class mesg_count(Enum):
  num_per_file                                             = 0       
  max_per_file                                             = 1       
  max_per_file_type                                        = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class date_time(Enum):
  min                                                      = 0x10000000# if date_time is < 0x10000000 then it is system time (seconds from device power on)

  @staticmethod
  def basetype():
    return basetypes.uint32

class local_date_time(Enum):
  min                                                      = 0x10000000# if date_time is < 0x10000000 then it is system time (seconds from device power on)

  @staticmethod
  def basetype():
    return basetypes.uint32

class message_index(Enum):
  selected                                                 = 0x8000  # message is selected if set
  reserved                                                 = 0x7000  # reserved (default 0)
  mask                                                     = 0x0FFF  # index

  @staticmethod
  def basetype():
    return basetypes.uint16

class device_index(Enum):
  creator                                                  = 0       # Creator of the file is always device index 0.

  @staticmethod
  def basetype():
    return basetypes.uint8

class gender(Enum):
  female                                                   = 0       
  male                                                     = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class language(Enum):
  english                                                  = 0       
  french                                                   = 1       
  italian                                                  = 2       
  german                                                   = 3       
  spanish                                                  = 4       
  croatian                                                 = 5       
  czech                                                    = 6       
  danish                                                   = 7       
  dutch                                                    = 8       
  finnish                                                  = 9       
  greek                                                    = 10      
  hungarian                                                = 11      
  norwegian                                                = 12      
  polish                                                   = 13      
  portuguese                                               = 14      
  slovakian                                                = 15      
  slovenian                                                = 16      
  swedish                                                  = 17      
  russian                                                  = 18      
  turkish                                                  = 19      
  latvian                                                  = 20      
  ukrainian                                                = 21      
  arabic                                                   = 22      
  farsi                                                    = 23      
  bulgarian                                                = 24      
  romanian                                                 = 25      
  chinese                                                  = 26      
  japanese                                                 = 27      
  korean                                                   = 28      
  taiwanese                                                = 29      
  thai                                                     = 30      
  hebrew                                                   = 31      
  brazilian_portuguese                                     = 32      
  indonesian                                               = 33      
  malaysian                                                = 34      
  vietnamese                                               = 35      
  burmese                                                  = 36      
  mongolian                                                = 37      
  custom                                                   = 254     

  @staticmethod
  def basetype():
    return basetypes.enum

class language_bits_0(Enum):
  english                                                  = 0x01    
  french                                                   = 0x02    
  italian                                                  = 0x04    
  german                                                   = 0x08    
  spanish                                                  = 0x10    
  croatian                                                 = 0x20    
  czech                                                    = 0x40    
  danish                                                   = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class language_bits_1(Enum):
  dutch                                                    = 0x01    
  finnish                                                  = 0x02    
  greek                                                    = 0x04    
  hungarian                                                = 0x08    
  norwegian                                                = 0x10    
  polish                                                   = 0x20    
  portuguese                                               = 0x40    
  slovakian                                                = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class language_bits_2(Enum):
  slovenian                                                = 0x01    
  swedish                                                  = 0x02    
  russian                                                  = 0x04    
  turkish                                                  = 0x08    
  latvian                                                  = 0x10    
  ukrainian                                                = 0x20    
  arabic                                                   = 0x40    
  farsi                                                    = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class language_bits_3(Enum):
  bulgarian                                                = 0x01    
  romanian                                                 = 0x02    
  chinese                                                  = 0x04    
  japanese                                                 = 0x08    
  korean                                                   = 0x10    
  taiwanese                                                = 0x20    
  thai                                                     = 0x40    
  hebrew                                                   = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class language_bits_4(Enum):
  brazilian_portuguese                                     = 0x01    
  indonesian                                               = 0x02    
  malaysian                                                = 0x04    
  vietnamese                                               = 0x08    
  burmese                                                  = 0x10    
  mongolian                                                = 0x20    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class time_zone(Enum):
  almaty                                                   = 0       
  bangkok                                                  = 1       
  bombay                                                   = 2       
  brasilia                                                 = 3       
  cairo                                                    = 4       
  cape_verde_is                                            = 5       
  darwin                                                   = 6       
  eniwetok                                                 = 7       
  fiji                                                     = 8       
  hong_kong                                                = 9       
  islamabad                                                = 10      
  kabul                                                    = 11      
  magadan                                                  = 12      
  mid_atlantic                                             = 13      
  moscow                                                   = 14      
  muscat                                                   = 15      
  newfoundland                                             = 16      
  samoa                                                    = 17      
  sydney                                                   = 18      
  tehran                                                   = 19      
  tokyo                                                    = 20      
  us_alaska                                                = 21      
  us_atlantic                                              = 22      
  us_central                                               = 23      
  us_eastern                                               = 24      
  us_hawaii                                                = 25      
  us_mountain                                              = 26      
  us_pacific                                               = 27      
  other                                                    = 28      
  auckland                                                 = 29      
  kathmandu                                                = 30      
  europe_western_wet                                       = 31      
  europe_central_cet                                       = 32      
  europe_eastern_eet                                       = 33      
  jakarta                                                  = 34      
  perth                                                    = 35      
  adelaide                                                 = 36      
  brisbane                                                 = 37      
  tasmania                                                 = 38      
  iceland                                                  = 39      
  amsterdam                                                = 40      
  athens                                                   = 41      
  barcelona                                                = 42      
  berlin                                                   = 43      
  brussels                                                 = 44      
  budapest                                                 = 45      
  copenhagen                                               = 46      
  dublin                                                   = 47      
  helsinki                                                 = 48      
  lisbon                                                   = 49      
  london                                                   = 50      
  madrid                                                   = 51      
  munich                                                   = 52      
  oslo                                                     = 53      
  paris                                                    = 54      
  prague                                                   = 55      
  reykjavik                                                = 56      
  rome                                                     = 57      
  stockholm                                                = 58      
  vienna                                                   = 59      
  warsaw                                                   = 60      
  zurich                                                   = 61      
  quebec                                                   = 62      
  ontario                                                  = 63      
  manitoba                                                 = 64      
  saskatchewan                                             = 65      
  alberta                                                  = 66      
  british_columbia                                         = 67      
  boise                                                    = 68      
  boston                                                   = 69      
  chicago                                                  = 70      
  dallas                                                   = 71      
  denver                                                   = 72      
  kansas_city                                              = 73      
  las_vegas                                                = 74      
  los_angeles                                              = 75      
  miami                                                    = 76      
  minneapolis                                              = 77      
  new_york                                                 = 78      
  new_orleans                                              = 79      
  phoenix                                                  = 80      
  santa_fe                                                 = 81      
  seattle                                                  = 82      
  washington_dc                                            = 83      
  us_arizona                                               = 84      
  chita                                                    = 85      
  ekaterinburg                                             = 86      
  irkutsk                                                  = 87      
  kaliningrad                                              = 88      
  krasnoyarsk                                              = 89      
  novosibirsk                                              = 90      
  petropavlovsk_kamchatskiy                                = 91      
  samara                                                   = 92      
  vladivostok                                              = 93      
  mexico_central                                           = 94      
  mexico_mountain                                          = 95      
  mexico_pacific                                           = 96      
  cape_town                                                = 97      
  winkhoek                                                 = 98      
  lagos                                                    = 99      
  riyahd                                                   = 100     
  venezuela                                                = 101     
  australia_lh                                             = 102     
  santiago                                                 = 103     
  manual                                                   = 253     
  automatic                                                = 254     

  @staticmethod
  def basetype():
    return basetypes.enum

class display_measure(Enum):
  metric                                                   = 0       
  statute                                                  = 1       
  nautical                                                 = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class display_heart(Enum):
  bpm                                                      = 0       
  max                                                      = 1       
  reserve                                                  = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class display_power(Enum):
  watts                                                    = 0       
  percent_ftp                                              = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class display_position(Enum):
  degree                                                   = 0       # dd.dddddd
  degree_minute                                            = 1       # dddmm.mmm
  degree_minute_second                                     = 2       # dddmmss
  austrian_grid                                            = 3       # Austrian Grid (BMN)
  british_grid                                             = 4       # British National Grid
  dutch_grid                                               = 5       # Dutch grid system
  hungarian_grid                                           = 6       # Hungarian grid system
  finnish_grid                                             = 7       # Finnish grid system Zone3 KKJ27
  german_grid                                              = 8       # Gausss Krueger (German)
  icelandic_grid                                           = 9       # Icelandic Grid
  indonesian_equatorial                                    = 10      # Indonesian Equatorial LCO
  indonesian_irian                                         = 11      # Indonesian Irian LCO
  indonesian_southern                                      = 12      # Indonesian Southern LCO
  india_zone_0                                             = 13      # India zone 0
  india_zone_IA                                            = 14      # India zone IA
  india_zone_IB                                            = 15      # India zone IB
  india_zone_IIA                                           = 16      # India zone IIA
  india_zone_IIB                                           = 17      # India zone IIB
  india_zone_IIIA                                          = 18      # India zone IIIA
  india_zone_IIIB                                          = 19      # India zone IIIB
  india_zone_IVA                                           = 20      # India zone IVA
  india_zone_IVB                                           = 21      # India zone IVB
  irish_transverse                                         = 22      # Irish Transverse Mercator
  irish_grid                                               = 23      # Irish Grid
  loran                                                    = 24      # Loran TD
  maidenhead_grid                                          = 25      # Maidenhead grid system
  mgrs_grid                                                = 26      # MGRS grid system
  new_zealand_grid                                         = 27      # New Zealand grid system
  new_zealand_transverse                                   = 28      # New Zealand Transverse Mercator
  qatar_grid                                               = 29      # Qatar National Grid
  modified_swedish_grid                                    = 30      # Modified RT-90 (Sweden)
  swedish_grid                                             = 31      # RT-90 (Sweden)
  south_african_grid                                       = 32      # South African Grid
  swiss_grid                                               = 33      # Swiss CH-1903 grid
  taiwan_grid                                              = 34      # Taiwan Grid
  united_states_grid                                       = 35      # United States National Grid
  utm_ups_grid                                             = 36      # UTM/UPS grid system
  west_malayan                                             = 37      # West Malayan RSO
  borneo_rso                                               = 38      # Borneo RSO
  estonian_grid                                            = 39      # Estonian grid system
  latvian_grid                                             = 40      # Latvian Transverse Mercator
  swedish_ref_99_grid                                      = 41      # Reference Grid 99 TM (Swedish)

  @staticmethod
  def basetype():
    return basetypes.enum

class switch(Enum):
  off                                                      = 0       
  on                                                       = 1       
  auto                                                     = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class sport(Enum):
  generic                                                  = 0       
  running                                                  = 1       
  cycling                                                  = 2       
  transition                                               = 3       # Mulitsport transition
  fitness_equipment                                        = 4       
  swimming                                                 = 5       
  basketball                                               = 6       
  soccer                                                   = 7       
  tennis                                                   = 8       
  american_football                                        = 9       
  training                                                 = 10      
  walking                                                  = 11      
  cross_country_skiing                                     = 12      
  alpine_skiing                                            = 13      
  snowboarding                                             = 14      
  rowing                                                   = 15      
  mountaineering                                           = 16      
  hiking                                                   = 17      
  multisport                                               = 18      
  paddling                                                 = 19      
  flying                                                   = 20      
  e_biking                                                 = 21      
  motorcycling                                             = 22      
  boating                                                  = 23      
  driving                                                  = 24      
  golf                                                     = 25      
  hang_gliding                                             = 26      
  horseback_riding                                         = 27      
  hunting                                                  = 28      
  fishing                                                  = 29      
  inline_skating                                           = 30      
  rock_climbing                                            = 31      
  sailing                                                  = 32      
  ice_skating                                              = 33      
  sky_diving                                               = 34      
  snowshoeing                                              = 35      
  snowmobiling                                             = 36      
  stand_up_paddleboarding                                  = 37      
  surfing                                                  = 38      
  wakeboarding                                             = 39      
  water_skiing                                             = 40      
  kayaking                                                 = 41      
  rafting                                                  = 42      
  windsurfing                                              = 43      
  kitesurfing                                              = 44      
  tactical                                                 = 45      
  jumpmaster                                               = 46      
  boxing                                                   = 47      
  floor_climbing                                           = 48      
  all                                                      = 254     # All is for goals only to include all sports.

  @staticmethod
  def basetype():
    return basetypes.enum

class sport_bits_0(Enum):
  generic                                                  = 0x01    
  running                                                  = 0x02    
  cycling                                                  = 0x04    
  transition                                               = 0x08    # Mulitsport transition
  fitness_equipment                                        = 0x10    
  swimming                                                 = 0x20    
  basketball                                               = 0x40    
  soccer                                                   = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sport_bits_1(Enum):
  tennis                                                   = 0x01    
  american_football                                        = 0x02    
  training                                                 = 0x04    
  walking                                                  = 0x08    
  cross_country_skiing                                     = 0x10    
  alpine_skiing                                            = 0x20    
  snowboarding                                             = 0x40    
  rowing                                                   = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sport_bits_2(Enum):
  mountaineering                                           = 0x01    
  hiking                                                   = 0x02    
  multisport                                               = 0x04    
  paddling                                                 = 0x08    
  flying                                                   = 0x10    
  e_biking                                                 = 0x20    
  motorcycling                                             = 0x40    
  boating                                                  = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sport_bits_3(Enum):
  driving                                                  = 0x01    
  golf                                                     = 0x02    
  hang_gliding                                             = 0x04    
  horseback_riding                                         = 0x08    
  hunting                                                  = 0x10    
  fishing                                                  = 0x20    
  inline_skating                                           = 0x40    
  rock_climbing                                            = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sport_bits_4(Enum):
  sailing                                                  = 0x01    
  ice_skating                                              = 0x02    
  sky_diving                                               = 0x04    
  snowshoeing                                              = 0x08    
  snowmobiling                                             = 0x10    
  stand_up_paddleboarding                                  = 0x20    
  surfing                                                  = 0x40    
  wakeboarding                                             = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sport_bits_5(Enum):
  water_skiing                                             = 0x01    
  kayaking                                                 = 0x02    
  rafting                                                  = 0x04    
  windsurfing                                              = 0x08    
  kitesurfing                                              = 0x10    
  tactical                                                 = 0x20    
  jumpmaster                                               = 0x40    
  boxing                                                   = 0x80    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sport_bits_6(Enum):
  floor_climbing                                           = 0x01    

  @staticmethod
  def basetype():
    return basetypes.uint8z

class sub_sport(Enum):
  generic                                                  = 0       
  treadmill                                                = 1       # Run/Fitness Equipment
  street                                                   = 2       # Run
  trail                                                    = 3       # Run
  track                                                    = 4       # Run
  spin                                                     = 5       # Cycling
  indoor_cycling                                           = 6       # Cycling/Fitness Equipment
  road                                                     = 7       # Cycling
  mountain                                                 = 8       # Cycling
  downhill                                                 = 9       # Cycling
  recumbent                                                = 10      # Cycling
  cyclocross                                               = 11      # Cycling
  hand_cycling                                             = 12      # Cycling
  track_cycling                                            = 13      # Cycling
  indoor_rowing                                            = 14      # Fitness Equipment
  elliptical                                               = 15      # Fitness Equipment
  stair_climbing                                           = 16      # Fitness Equipment
  lap_swimming                                             = 17      # Swimming
  open_water                                               = 18      # Swimming
  flexibility_training                                     = 19      # Training
  strength_training                                        = 20      # Training
  warm_up                                                  = 21      # Tennis
  match                                                    = 22      # Tennis
  exercise                                                 = 23      # Tennis
  challenge                                                = 24      
  indoor_skiing                                            = 25      # Fitness Equipment
  cardio_training                                          = 26      # Training
  indoor_walking                                           = 27      # Walking/Fitness Equipment
  e_bike_fitness                                           = 28      # E-Biking
  bmx                                                      = 29      # Cycling
  casual_walking                                           = 30      # Walking
  speed_walking                                            = 31      # Walking
  bike_to_run_transition                                   = 32      # Transition
  run_to_bike_transition                                   = 33      # Transition
  swim_to_bike_transition                                  = 34      # Transition
  atv                                                      = 35      # Motorcycling
  motocross                                                = 36      # Motorcycling
  backcountry                                              = 37      # Alpine Skiing/Snowboarding
  resort                                                   = 38      # Alpine Skiing/Snowboarding
  rc_drone                                                 = 39      # Flying
  wingsuit                                                 = 40      # Flying
  whitewater                                               = 41      # Kayaking/Rafting
  skate_skiing                                             = 42      # Cross Country Skiing
  yoga                                                     = 43      # Training
  pilates                                                  = 44      # Fitness Equipment
  indoor_running                                           = 45      # Run
  gravel_cycling                                           = 46      # Cycling
  e_bike_mountain                                          = 47      # Cycling
  commuting                                                = 48      # Cycling
  mixed_surface                                            = 49      # Cycling
  navigate                                                 = 50      
  track_me                                                 = 51      
  map                                                      = 52      
  single_gas_diving                                        = 53      # Diving
  multi_gas_diving                                         = 54      # Diving
  gauge_diving                                             = 55      # Diving
  apnea_diving                                             = 56      # Diving
  apnea_hunting                                            = 57      # Diving
  virtual_activity                                         = 58      
  obstacle                                                 = 59      # Used for events where participants run, crawl through mud, climb over walls, etc.
  all                                                      = 254     

  @staticmethod
  def basetype():
    return basetypes.enum

class sport_event(Enum):
  uncategorized                                            = 0       
  geocaching                                               = 1       
  fitness                                                  = 2       
  recreation                                               = 3       
  race                                                     = 4       
  special_event                                            = 5       
  training                                                 = 6       
  transportation                                           = 7       
  touring                                                  = 8       

  @staticmethod
  def basetype():
    return basetypes.enum

class activity(Enum):
  manual                                                   = 0       
  auto_multi_sport                                         = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class intensity(Enum):
  active                                                   = 0       
  rest                                                     = 1       
  warmup                                                   = 2       
  cooldown                                                 = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class session_trigger(Enum):
  activity_end                                             = 0       
  manual                                                   = 1       # User changed sport.
  auto_multi_sport                                         = 2       # Auto multi-sport feature is enabled and user pressed lap button to advance session.
  fitness_equipment                                        = 3       # Auto sport change caused by user linking to fitness equipment.

  @staticmethod
  def basetype():
    return basetypes.enum

class autolap_trigger(Enum):
  time                                                     = 0       
  distance                                                 = 1       
  position_start                                           = 2       
  position_lap                                             = 3       
  position_waypoint                                        = 4       
  position_marked                                          = 5       
  off                                                      = 6       

  @staticmethod
  def basetype():
    return basetypes.enum

class lap_trigger(Enum):
  manual                                                   = 0       
  time                                                     = 1       
  distance                                                 = 2       
  position_start                                           = 3       
  position_lap                                             = 4       
  position_waypoint                                        = 5       
  position_marked                                          = 6       
  session_end                                              = 7       
  fitness_equipment                                        = 8       

  @staticmethod
  def basetype():
    return basetypes.enum

class time_mode(Enum):
  hour12                                                   = 0       
  hour24                                                   = 1       # Does not use a leading zero and has a colon
  military                                                 = 2       # Uses a leading zero and does not have a colon
  hour_12_with_seconds                                     = 3       
  hour_24_with_seconds                                     = 4       
  utc                                                      = 5       

  @staticmethod
  def basetype():
    return basetypes.enum

class backlight_mode(Enum):
  off                                                      = 0       
  manual                                                   = 1       
  key_and_messages                                         = 2       
  auto_brightness                                          = 3       
  smart_notifications                                      = 4       
  key_and_messages_night                                   = 5       
  key_and_messages_and_smart_notifications                 = 6       

  @staticmethod
  def basetype():
    return basetypes.enum

class date_mode(Enum):
  day_month                                                = 0       
  month_day                                                = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class backlight_timeout(Enum):
  infinite                                                 = 0       # Backlight stays on forever.

  @staticmethod
  def basetype():
    return basetypes.uint8

class event(Enum):
  timer                                                    = 0       # Group 0.  Start / stop_all
  workout                                                  = 3       # start / stop
  workout_step                                             = 4       # Start at beginning of workout.  Stop at end of each step.
  power_down                                               = 5       # stop_all group 0
  power_up                                                 = 6       # stop_all group 0
  off_course                                               = 7       # start / stop group 0
  session                                                  = 8       # Stop at end of each session.
  lap                                                      = 9       # Stop at end of each lap.
  course_point                                             = 10      # marker
  battery                                                  = 11      # marker
  virtual_partner_pace                                     = 12      # Group 1. Start at beginning of activity if VP enabled, when VP pace is changed during activity or VP enabled mid activity.  stop_disable when VP disabled.
  hr_high_alert                                            = 13      # Group 0.  Start / stop when in alert condition.
  hr_low_alert                                             = 14      # Group 0.  Start / stop when in alert condition.
  speed_high_alert                                         = 15      # Group 0.  Start / stop when in alert condition.
  speed_low_alert                                          = 16      # Group 0.  Start / stop when in alert condition.
  cad_high_alert                                           = 17      # Group 0.  Start / stop when in alert condition.
  cad_low_alert                                            = 18      # Group 0.  Start / stop when in alert condition.
  power_high_alert                                         = 19      # Group 0.  Start / stop when in alert condition.
  power_low_alert                                          = 20      # Group 0.  Start / stop when in alert condition.
  recovery_hr                                              = 21      # marker
  battery_low                                              = 22      # marker
  time_duration_alert                                      = 23      # Group 1.  Start if enabled mid activity (not required at start of activity). Stop when duration is reached.  stop_disable if disabled.
  distance_duration_alert                                  = 24      # Group 1.  Start if enabled mid activity (not required at start of activity). Stop when duration is reached.  stop_disable if disabled.
  calorie_duration_alert                                   = 25      # Group 1.  Start if enabled mid activity (not required at start of activity). Stop when duration is reached.  stop_disable if disabled.
  activity                                                 = 26      # Group 1..  Stop at end of activity.
  fitness_equipment                                        = 27      # marker
  length                                                   = 28      # Stop at end of each length.
  user_marker                                              = 32      # marker
  sport_point                                              = 33      # marker
  calibration                                              = 36      # start/stop/marker
  front_gear_change                                        = 42      # marker
  rear_gear_change                                         = 43      # marker
  rider_position_change                                    = 44      # marker
  elev_high_alert                                          = 45      # Group 0.  Start / stop when in alert condition.
  elev_low_alert                                           = 46      # Group 0.  Start / stop when in alert condition.
  comm_timeout                                             = 47      # marker
  radar_threat_alert                                       = 75      # start/stop/marker

  @staticmethod
  def basetype():
    return basetypes.enum

class event_type(Enum):
  start                                                    = 0       
  stop                                                     = 1       
  consecutive_depreciated                                  = 2       
  marker                                                   = 3       
  stop_all                                                 = 4       
  begin_depreciated                                        = 5       
  end_depreciated                                          = 6       
  end_all_depreciated                                      = 7       
  stop_disable                                             = 8       
  stop_disable_all                                         = 9       

  @staticmethod
  def basetype():
    return basetypes.enum

class timer_trigger(Enum):
  manual                                                   = 0       
  auto                                                     = 1       
  fitness_equipment                                        = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class fitness_equipment_state(Enum):
  ready                                                    = 0       
  in_use                                                   = 1       
  paused                                                   = 2       
  unknown                                                  = 3       # lost connection to fitness equipment

  @staticmethod
  def basetype():
    return basetypes.enum

class tone(Enum):
  off                                                      = 0       
  tone                                                     = 1       
  vibrate                                                  = 2       
  tone_and_vibrate                                         = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class autoscroll(Enum):
  none                                                     = 0       
  slow                                                     = 1       
  medium                                                   = 2       
  fast                                                     = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class activity_class(Enum):
  level                                                    = 0x7F    # 0 to 100
  level_max                                                = 100     
  athlete                                                  = 0x80    

  @staticmethod
  def basetype():
    return basetypes.enum

class hr_zone_calc(Enum):
  custom                                                   = 0       
  percent_max_hr                                           = 1       
  percent_hrr                                              = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class pwr_zone_calc(Enum):
  custom                                                   = 0       
  percent_ftp                                              = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class wkt_step_duration(Enum):
  time                                                     = 0       
  distance                                                 = 1       
  hr_less_than                                             = 2       
  hr_greater_than                                          = 3       
  calories                                                 = 4       
  open                                                     = 5       
  repeat_until_steps_cmplt                                 = 6       
  repeat_until_time                                        = 7       
  repeat_until_distance                                    = 8       
  repeat_until_calories                                    = 9       
  repeat_until_hr_less_than                                = 10      
  repeat_until_hr_greater_than                             = 11      
  repeat_until_power_less_than                             = 12      
  repeat_until_power_greater_than                          = 13      
  power_less_than                                          = 14      
  power_greater_than                                       = 15      
  training_peaks_tss                                       = 16      
  repeat_until_power_last_lap_less_than                    = 17      
  repeat_until_max_power_last_lap_less_than                = 18      
  power_3s_less_than                                       = 19      
  power_10s_less_than                                      = 20      
  power_30s_less_than                                      = 21      
  power_3s_greater_than                                    = 22      
  power_10s_greater_than                                   = 23      
  power_30s_greater_than                                   = 24      
  power_lap_less_than                                      = 25      
  power_lap_greater_than                                   = 26      
  repeat_until_training_peaks_tss                          = 27      
  repetition_time                                          = 28      
  reps                                                     = 29      
  time_only                                                = 31      

  @staticmethod
  def basetype():
    return basetypes.enum

class wkt_step_target(Enum):
  speed                                                    = 0       
  heart_rate                                               = 1       
  open                                                     = 2       
  cadence                                                  = 3       
  power                                                    = 4       
  grade                                                    = 5       
  resistance                                               = 6       
  power_3s                                                 = 7       
  power_10s                                                = 8       
  power_30s                                                = 9       
  power_lap                                                = 10      
  swim_stroke                                              = 11      
  speed_lap                                                = 12      
  heart_rate_lap                                           = 13      

  @staticmethod
  def basetype():
    return basetypes.enum

class goal(Enum):
  time                                                     = 0       
  distance                                                 = 1       
  calories                                                 = 2       
  frequency                                                = 3       
  steps                                                    = 4       
  ascent                                                   = 5       
  active_minutes                                           = 6       

  @staticmethod
  def basetype():
    return basetypes.enum

class goal_recurrence(Enum):
  off                                                      = 0       
  daily                                                    = 1       
  weekly                                                   = 2       
  monthly                                                  = 3       
  yearly                                                   = 4       
  custom                                                   = 5       

  @staticmethod
  def basetype():
    return basetypes.enum

class goal_source(Enum):
  auto                                                     = 0       # Device generated
  community                                                = 1       # Social network sourced goal
  user                                                     = 2       # Manually generated

  @staticmethod
  def basetype():
    return basetypes.enum

class schedule(Enum):
  workout                                                  = 0       
  course                                                   = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class course_point(Enum):
  generic                                                  = 0       
  summit                                                   = 1       
  valley                                                   = 2       
  water                                                    = 3       
  food                                                     = 4       
  danger                                                   = 5       
  left                                                     = 6       
  right                                                    = 7       
  straight                                                 = 8       
  first_aid                                                = 9       
  fourth_category                                          = 10      
  third_category                                           = 11      
  second_category                                          = 12      
  first_category                                           = 13      
  hors_category                                            = 14      
  sprint                                                   = 15      
  left_fork                                                = 16      
  right_fork                                               = 17      
  middle_fork                                              = 18      
  slight_left                                              = 19      
  sharp_left                                               = 20      
  slight_right                                             = 21      
  sharp_right                                              = 22      
  u_turn                                                   = 23      
  segment_start                                            = 24      
  segment_end                                              = 25      

  @staticmethod
  def basetype():
    return basetypes.enum

class manufacturer(Enum):
  garmin                                                   = 1       
  garmin_fr405_antfs                                       = 2       # Do not use.  Used by FR405 for ANTFS man id.
  zephyr                                                   = 3       
  dayton                                                   = 4       
  idt                                                      = 5       
  srm                                                      = 6       
  quarq                                                    = 7       
  ibike                                                    = 8       
  saris                                                    = 9       
  spark_hk                                                 = 10      
  tanita                                                   = 11      
  echowell                                                 = 12      
  dynastream_oem                                           = 13      
  nautilus                                                 = 14      
  dynastream                                               = 15      
  timex                                                    = 16      
  metrigear                                                = 17      
  xelic                                                    = 18      
  beurer                                                   = 19      
  cardiosport                                              = 20      
  a_and_d                                                  = 21      
  hmm                                                      = 22      
  suunto                                                   = 23      
  thita_elektronik                                         = 24      
  gpulse                                                   = 25      
  clean_mobile                                             = 26      
  pedal_brain                                              = 27      
  peaksware                                                = 28      
  saxonar                                                  = 29      
  lemond_fitness                                           = 30      
  dexcom                                                   = 31      
  wahoo_fitness                                            = 32      
  octane_fitness                                           = 33      
  archinoetics                                             = 34      
  the_hurt_box                                             = 35      
  citizen_systems                                          = 36      
  magellan                                                 = 37      
  osynce                                                   = 38      
  holux                                                    = 39      
  concept2                                                 = 40      
  one_giant_leap                                           = 42      
  ace_sensor                                               = 43      
  brim_brothers                                            = 44      
  xplova                                                   = 45      
  perception_digital                                       = 46      
  bf1systems                                               = 47      
  pioneer                                                  = 48      
  spantec                                                  = 49      
  metalogics                                               = 50      
  _4iiiis                                                  = 51      
  seiko_epson                                              = 52      
  seiko_epson_oem                                          = 53      
  ifor_powell                                              = 54      
  maxwell_guider                                           = 55      
  star_trac                                                = 56      
  breakaway                                                = 57      
  alatech_technology_ltd                                   = 58      
  mio_technology_europe                                    = 59      
  rotor                                                    = 60      
  geonaute                                                 = 61      
  id_bike                                                  = 62      
  specialized                                              = 63      
  wtek                                                     = 64      
  physical_enterprises                                     = 65      
  north_pole_engineering                                   = 66      
  bkool                                                    = 67      
  cateye                                                   = 68      
  stages_cycling                                           = 69      
  sigmasport                                               = 70      
  tomtom                                                   = 71      
  peripedal                                                = 72      
  wattbike                                                 = 73      
  moxy                                                     = 76      
  ciclosport                                               = 77      
  powerbahn                                                = 78      
  acorn_projects_aps                                       = 79      
  lifebeam                                                 = 80      
  bontrager                                                = 81      
  wellgo                                                   = 82      
  scosche                                                  = 83      
  magura                                                   = 84      
  woodway                                                  = 85      
  elite                                                    = 86      
  nielsen_kellerman                                        = 87      
  dk_city                                                  = 88      
  tacx                                                     = 89      
  direction_technology                                     = 90      
  magtonic                                                 = 91      
  _1partcarbon                                             = 92      
  inside_ride_technologies                                 = 93      
  sound_of_motion                                          = 94      
  stryd                                                    = 95      
  icg                                                      = 96      # Indoorcycling Group
  MiPulse                                                  = 97      
  bsx_athletics                                            = 98      
  look                                                     = 99      
  campagnolo_srl                                           = 100     
  body_bike_smart                                          = 101     
  praxisworks                                              = 102     
  limits_technology                                        = 103     # Limits Technology Ltd.
  topaction_technology                                     = 104     # TopAction Technology Inc.
  cosinuss                                                 = 105     
  fitcare                                                  = 106     
  magene                                                   = 107     
  giant_manufacturing_co                                   = 108     
  tigrasport                                               = 109     # Tigrasport
  salutron                                                 = 110     
  technogym                                                = 111     
  bryton_sensors                                           = 112     
  latitude_limited                                         = 113     
  soaring_technology                                       = 114     
  igpsport                                                 = 115     
  thinkrider                                               = 116     
  gopher_sport                                             = 117     
  waterrower                                               = 118     
  orangetheory                                             = 119     
  inpeak                                                   = 120     
  kinetic                                                  = 121     
  johnson_health_tech                                      = 122     
  polar_electro                                            = 123     
  seesense                                                 = 124     
  nci_technology                                           = 125     
  iqsquare                                                 = 126     
  leomo                                                    = 127     
  ifit_com                                                 = 128     
  coros_byte                                               = 129     
  versa_design                                             = 130     
  chileaf                                                  = 131     
  cycplus                                                  = 132     
  development                                              = 255     
  healthandlife                                            = 257     
  lezyne                                                   = 258     
  scribe_labs                                              = 259     
  zwift                                                    = 260     
  watteam                                                  = 261     
  recon                                                    = 262     
  favero_electronics                                       = 263     
  dynovelo                                                 = 264     
  strava                                                   = 265     
  precor                                                   = 266     # Amer Sports
  bryton                                                   = 267     
  sram                                                     = 268     
  navman                                                   = 269     # MiTAC Global Corporation (Mio Technology)
  cobi                                                     = 270     # COBI GmbH
  spivi                                                    = 271     
  mio_magellan                                             = 272     
  evesports                                                = 273     
  sensitivus_gauge                                         = 274     
  podoon                                                   = 275     
  life_time_fitness                                        = 276     
  falco_e_motors                                           = 277     # Falco eMotors Inc.
  minoura                                                  = 278     
  cycliq                                                   = 279     
  luxottica                                                = 280     
  trainer_road                                             = 281     
  the_sufferfest                                           = 282     
  fullspeedahead                                           = 283     
  virtualtraining                                          = 284     
  feedbacksports                                           = 285     
  omata                                                    = 286     
  vdo                                                      = 287     
  magneticdays                                             = 288     
  hammerhead                                               = 289     
  kinetic_by_kurt                                          = 290     
  shapelog                                                 = 291     
  dabuziduo                                                = 292     
  jetblack                                                 = 293     
  coros                                                    = 294     
  virtugo                                                  = 295     
  velosense                                                = 296     
  cycligentinc                                             = 297     
  trailforks                                               = 298     
  mahle_ebikemotion                                        = 299     
  nurvv                                                    = 300     
  microprogram                                             = 301     
  zone5cloud                                               = 302     
  greenteg                                                 = 303     
  yamaha_motors                                            = 304     
  actigraphcorp                                            = 5759    

  @staticmethod
  def basetype():
    return basetypes.uint16

class garmin_product(Enum):
  hrm1                                                     = 1       
  axh01                                                    = 2       # AXH01 HRM chipset
  axb01                                                    = 3       
  axb02                                                    = 4       
  hrm2ss                                                   = 5       
  dsi_alf02                                                = 6       
  hrm3ss                                                   = 7       
  hrm_run_single_byte_product_id                           = 8       # hrm_run model for HRM ANT+ messaging
  bsm                                                      = 9       # BSM model for ANT+ messaging
  bcm                                                      = 10      # BCM model for ANT+ messaging
  axs01                                                    = 11      # AXS01 HRM Bike Chipset model for ANT+ messaging
  hrm_tri_single_byte_product_id                           = 12      # hrm_tri model for HRM ANT+ messaging
  hrm4_run_single_byte_product_id                          = 13      # hrm4 run model for HRM ANT+ messaging
  fr225_single_byte_product_id                             = 14      # fr225 model for HRM ANT+ messaging
  fr301_china                                              = 473     
  fr301_japan                                              = 474     
  fr301_korea                                              = 475     
  fr301_taiwan                                             = 494     
  fr405                                                    = 717     # Forerunner 405
  fr50                                                     = 782     # Forerunner 50
  fr405_japan                                              = 987     
  fr60                                                     = 988     # Forerunner 60
  dsi_alf01                                                = 1011    
  fr310xt                                                  = 1018    # Forerunner 310
  edge500                                                  = 1036    
  fr110                                                    = 1124    # Forerunner 110
  edge800                                                  = 1169    
  edge500_taiwan                                           = 1199    
  edge500_japan                                            = 1213    
  chirp                                                    = 1253    
  fr110_japan                                              = 1274    
  edge200                                                  = 1325    
  fr910xt                                                  = 1328    
  edge800_taiwan                                           = 1333    
  edge800_japan                                            = 1334    
  alf04                                                    = 1341    
  fr610                                                    = 1345    
  fr210_japan                                              = 1360    
  vector_ss                                                = 1380    
  vector_cp                                                = 1381    
  edge800_china                                            = 1386    
  edge500_china                                            = 1387    
  approach_g10                                             = 1405    
  fr610_japan                                              = 1410    
  edge500_korea                                            = 1422    
  fr70                                                     = 1436    
  fr310xt_4t                                               = 1446    
  amx                                                      = 1461    
  fr10                                                     = 1482    
  edge800_korea                                            = 1497    
  swim                                                     = 1499    
  fr910xt_china                                            = 1537    
  fenix                                                    = 1551    
  edge200_taiwan                                           = 1555    
  edge510                                                  = 1561    
  edge810                                                  = 1567    
  tempe                                                    = 1570    
  fr910xt_japan                                            = 1600    
  fr620                                                    = 1623    
  fr220                                                    = 1632    
  fr910xt_korea                                            = 1664    
  fr10_japan                                               = 1688    
  edge810_japan                                            = 1721    
  virb_elite                                               = 1735    
  edge_touring                                             = 1736    # Also Edge Touring Plus
  edge510_japan                                            = 1742    
  hrm_tri                                                  = 1743    
  hrm_run                                                  = 1752    
  fr920xt                                                  = 1765    
  edge510_asia                                             = 1821    
  edge810_china                                            = 1822    
  edge810_taiwan                                           = 1823    
  edge1000                                                 = 1836    
  vivo_fit                                                 = 1837    
  virb_remote                                              = 1853    
  vivo_ki                                                  = 1885    
  fr15                                                     = 1903    
  vivo_active                                              = 1907    
  edge510_korea                                            = 1918    
  fr620_japan                                              = 1928    
  fr620_china                                              = 1929    
  fr220_japan                                              = 1930    
  fr220_china                                              = 1931    
  approach_s6                                              = 1936    
  vivo_smart                                               = 1956    
  fenix2                                                   = 1967    
  epix                                                     = 1988    
  fenix3                                                   = 2050    
  edge1000_taiwan                                          = 2052    
  edge1000_japan                                           = 2053    
  fr15_japan                                               = 2061    
  edge520                                                  = 2067    
  edge1000_china                                           = 2070    
  fr620_russia                                             = 2072    
  fr220_russia                                             = 2073    
  vector_s                                                 = 2079    
  edge1000_korea                                           = 2100    
  fr920xt_taiwan                                           = 2130    
  fr920xt_china                                            = 2131    
  fr920xt_japan                                            = 2132    
  virbx                                                    = 2134    
  vivo_smart_apac                                          = 2135    
  etrex_touch                                              = 2140    
  edge25                                                   = 2147    
  fr25                                                     = 2148    
  vivo_fit2                                                = 2150    
  fr225                                                    = 2153    
  fr630                                                    = 2156    
  fr230                                                    = 2157    
  fr735xt                                                  = 2158    
  vivo_active_apac                                         = 2160    
  vector_2                                                 = 2161    
  vector_2s                                                = 2162    
  virbxe                                                   = 2172    
  fr620_taiwan                                             = 2173    
  fr220_taiwan                                             = 2174    
  truswing                                                 = 2175    
  fenix3_china                                             = 2188    
  fenix3_twn                                               = 2189    
  varia_headlight                                          = 2192    
  varia_taillight_old                                      = 2193    
  edge_explore_1000                                        = 2204    
  fr225_asia                                               = 2219    
  varia_radar_taillight                                    = 2225    
  varia_radar_display                                      = 2226    
  edge20                                                   = 2238    
  edge520_asia                                             = 2260    
  edge520_japan                                            = 2261    
  d2_bravo                                                 = 2262    
  approach_s20                                             = 2266    
  vivo_smart2                                              = 2271    
  edge1000_thai                                            = 2274    
  varia_remote                                             = 2276    
  edge25_asia                                              = 2288    
  edge25_jpn                                               = 2289    
  edge20_asia                                              = 2290    
  approach_x40                                             = 2292    
  fenix3_japan                                             = 2293    
  vivo_smart_emea                                          = 2294    
  fr630_asia                                               = 2310    
  fr630_jpn                                                = 2311    
  fr230_jpn                                                = 2313    
  hrm4_run                                                 = 2327    
  epix_japan                                               = 2332    
  vivo_active_hr                                           = 2337    
  vivo_smart_gps_hr                                        = 2347    
  vivo_smart_hr                                            = 2348    
  vivo_smart_hr_asia                                       = 2361    
  vivo_smart_gps_hr_asia                                   = 2362    
  vivo_move                                                = 2368    
  varia_taillight                                          = 2379    
  fr235_japan                                              = 2397    
  varia_vision                                             = 2398    
  vivo_fit3                                                = 2406    
  fenix3_korea                                             = 2407    
  fenix3_sea                                               = 2408    
  fenix3_hr                                                = 2413    
  virb_ultra_30                                            = 2417    
  index_smart_scale                                        = 2429    
  fr235                                                    = 2431    
  fenix3_chronos                                           = 2432    
  oregon7xx                                                = 2441    
  rino7xx                                                  = 2444    
  epix_korea                                               = 2457    
  fenix3_hr_chn                                            = 2473    
  fenix3_hr_twn                                            = 2474    
  fenix3_hr_jpn                                            = 2475    
  fenix3_hr_sea                                            = 2476    
  fenix3_hr_kor                                            = 2477    
  nautix                                                   = 2496    
  vivo_active_hr_apac                                      = 2497    
  oregon7xx_ww                                             = 2512    
  edge_820                                                 = 2530    
  edge_explore_820                                         = 2531    
  fr735xt_apac                                             = 2533    
  fr735xt_japan                                            = 2534    
  fenix5s                                                  = 2544    
  d2_bravo_titanium                                        = 2547    
  varia_ut800                                              = 2567    # Varia UT 800 SW
  running_dynamics_pod                                     = 2593    
  edge_820_china                                           = 2599    
  edge_820_japan                                           = 2600    
  fenix5x                                                  = 2604    
  vivo_fit_jr                                              = 2606    
  vivo_smart3                                              = 2622    
  vivo_sport                                               = 2623    
  edge_820_taiwan                                          = 2628    
  edge_820_korea                                           = 2629    
  edge_820_sea                                             = 2630    
  fr35_hebrew                                              = 2650    
  approach_s60                                             = 2656    
  fr35_apac                                                = 2667    
  fr35_japan                                               = 2668    
  fenix3_chronos_asia                                      = 2675    
  virb_360                                                 = 2687    
  fr935                                                    = 2691    
  fenix5                                                   = 2697    
  vivoactive3                                              = 2700    
  fr235_china_nfc                                          = 2733    
  foretrex_601_701                                         = 2769    
  vivo_move_hr                                             = 2772    
  edge_1030                                                = 2713    
  fenix5_asia                                              = 2796    
  fenix5s_asia                                             = 2797    
  fenix5x_asia                                             = 2798    
  approach_z80                                             = 2806    
  fr35_korea                                               = 2814    
  d2charlie                                                = 2819    
  vivo_smart3_apac                                         = 2831    
  vivo_sport_apac                                          = 2832    
  fr935_asia                                               = 2833    
  descent                                                  = 2859    
  fr645                                                    = 2886    
  fr645m                                                   = 2888    
  fr30                                                     = 2891    
  fenix5s_plus                                             = 2900    
  Edge_130                                                 = 2909    
  edge_1030_asia                                           = 2924    
  vivosmart_4                                              = 2927    
  vivo_move_hr_asia                                        = 2945    
  approach_x10                                             = 2962    
  fr30_asia                                                = 2977    
  vivoactive3m_w                                           = 2988    
  fr645_asia                                               = 3003    
  fr645m_asia                                              = 3004    
  edge_explore                                             = 3011    
  gpsmap66                                                 = 3028    
  approach_s10                                             = 3049    
  vivoactive3m_l                                           = 3066    
  approach_g80                                             = 3085    
  edge_130_asia                                            = 3092    
  edge_1030_bontrager                                      = 3095    
  fenix5_plus                                              = 3110    
  fenix5x_plus                                             = 3111    
  edge_520_plus                                            = 3112    
  edge_530                                                 = 3121    
  edge_830                                                 = 3122    
  fenix5s_plus_apac                                        = 3134    
  fenix5x_plus_apac                                        = 3135    
  edge_520_plus_apac                                       = 3142    
  fr235l_asia                                              = 3144    
  fr245_asia                                               = 3145    
  vivo_active3m_apac                                       = 3163    
  vivo_smart4_asia                                         = 3218    
  vivoactive4_small                                        = 3224    
  vivoactive4_large                                        = 3225    
  venu                                                     = 3226    
  marq_driver                                              = 3246    
  marq_aviator                                             = 3247    
  marq_captain                                             = 3248    
  marq_commander                                           = 3249    
  marq_expedition                                          = 3250    
  marq_athlete                                             = 3251    
  fenix6S_sport                                            = 3287    
  fenix6S                                                  = 3288    
  fenix6_sport                                             = 3289    
  fenix6                                                   = 3290    
  fenix6x                                                  = 3291    
  hrm_dual                                                 = 3299    # HRM-Dual
  vivo_move3_premium                                       = 3308    
  approach_s40                                             = 3314    
  fr245m_asia                                              = 3321    
  edge_530_apac                                            = 3349    
  edge_830_apac                                            = 3350    
  vivo_move3                                               = 3378    
  vivo_active4_small_asia                                  = 3387    
  vivo_active4_large_asia                                  = 3388    
  vivo_active4_oled_asia                                   = 3389    
  swim2                                                    = 3405    
  marq_driver_asia                                         = 3420    
  marq_aviator_asia                                        = 3421    
  vivo_move3_asia                                          = 3422    
  vivo_active3t_chn                                        = 3446    
  marq_captain_asia                                        = 3448    
  marq_commander_asia                                      = 3449    
  marq_expedition_asia                                     = 3450    
  marq_athlete_asia                                        = 3451    
  fr45_asia                                                = 3469    
  vivoactive3_daimler                                      = 3473    
  fenix6s_sport_asia                                       = 3512    
  fenix6s_asia                                             = 3513    
  fenix6_sport_asia                                        = 3514    
  fenix6_asia                                              = 3515    
  fenix6x_asia                                             = 3516    
  marq_adventurer                                          = 3624    
  marq_adventurer_asia                                     = 3648    
  swim2_apac                                               = 3639    
  venu_daimler_asia                                        = 3737    
  venu_daimler                                             = 3740    
  sdm4                                                     = 10007   # SDM4 footpod
  edge_remote                                              = 10014   
  training_center                                          = 20119   
  connectiq_simulator                                      = 65531   
  android_antplus_plugin                                   = 65532   
  connect                                                  = 65534   # Garmin Connect website

  @staticmethod
  def basetype():
    return basetypes.uint16

class antplus_device_type(Enum):
  antfs                                                    = 1       
  bike_power                                               = 11      
  environment_sensor_legacy                                = 12      
  multi_sport_speed_distance                               = 15      
  control                                                  = 16      
  fitness_equipment                                        = 17      
  blood_pressure                                           = 18      
  geocache_node                                            = 19      
  light_electric_vehicle                                   = 20      
  env_sensor                                               = 25      
  racquet                                                  = 26      
  control_hub                                              = 27      
  muscle_oxygen                                            = 31      
  bike_light_main                                          = 35      
  bike_light_shared                                        = 36      
  exd                                                      = 38      
  bike_radar                                               = 40      
  bike_aero                                                = 46      
  weight_scale                                             = 119     
  heart_rate                                               = 120     
  bike_speed_cadence                                       = 121     
  bike_cadence                                             = 122     
  bike_speed                                               = 123     
  stride_speed_distance                                    = 124     

  @staticmethod
  def basetype():
    return basetypes.uint8

class ant_network(Enum):
  public                                                   = 0       
  antplus                                                  = 1       
  antfs                                                    = 2       
  private                                                  = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class workout_capabilities(Enum):
  interval                                                 = 0x00000001
  custom                                                   = 0x00000002
  fitness_equipment                                        = 0x00000004
  firstbeat                                                = 0x00000008
  new_leaf                                                 = 0x00000010
  tcx                                                      = 0x00000020# For backwards compatibility.  Watch should add missing id fields then clear flag.
  speed                                                    = 0x00000080# Speed source required for workout step.
  heart_rate                                               = 0x00000100# Heart rate source required for workout step.
  distance                                                 = 0x00000200# Distance source required for workout step.
  cadence                                                  = 0x00000400# Cadence source required for workout step.
  power                                                    = 0x00000800# Power source required for workout step.
  grade                                                    = 0x00001000# Grade source required for workout step.
  resistance                                               = 0x00002000# Resistance source required for workout step.
  protected                                                = 0x00004000

  @staticmethod
  def basetype():
    return basetypes.uint32z

class battery_status(Enum):
  new                                                      = 1       
  good                                                     = 2       
  ok                                                       = 3       
  low                                                      = 4       
  critical                                                 = 5       
  charging                                                 = 6       
  unknown                                                  = 7       

  @staticmethod
  def basetype():
    return basetypes.uint8

class hr_type(Enum):
  normal                                                   = 0       
  irregular                                                = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class course_capabilities(Enum):
  processed                                                = 0x00000001
  valid                                                    = 0x00000002
  time                                                     = 0x00000004
  distance                                                 = 0x00000008
  position                                                 = 0x00000010
  heart_rate                                               = 0x00000020
  power                                                    = 0x00000040
  cadence                                                  = 0x00000080
  training                                                 = 0x00000100
  navigation                                               = 0x00000200
  bikeway                                                  = 0x00000400

  @staticmethod
  def basetype():
    return basetypes.uint32z

class weight(Enum):
  calculating                                              = 0xFFFE  

  @staticmethod
  def basetype():
    return basetypes.uint16

class workout_hr(Enum):
  bpm_offset                                               = 100     

  @staticmethod
  def basetype():
    return basetypes.uint32

class workout_power(Enum):
  watts_offset                                             = 1000    

  @staticmethod
  def basetype():
    return basetypes.uint32

class bp_status(Enum):
  no_error                                                 = 0       
  error_incomplete_data                                    = 1       
  error_no_measurement                                     = 2       
  error_data_out_of_range                                  = 3       
  error_irregular_heart_rate                               = 4       

  @staticmethod
  def basetype():
    return basetypes.enum

class user_local_id(Enum):
  local_min                                                = 0x0000  
  local_max                                                = 0x000F  
  stationary_min                                           = 0x0010  
  stationary_max                                           = 0x00FF  
  portable_min                                             = 0x0100  
  portable_max                                             = 0xFFFE  

  @staticmethod
  def basetype():
    return basetypes.uint16

class swim_stroke(Enum):
  freestyle                                                = 0       
  backstroke                                               = 1       
  breaststroke                                             = 2       
  butterfly                                                = 3       
  drill                                                    = 4       
  mixed                                                    = 5       
  im                                                       = 6       # IM is a mixed interval containing the same number of lengths for each of: Butterfly, Backstroke, Breaststroke, Freestyle, swam in that order.

  @staticmethod
  def basetype():
    return basetypes.enum

class activity_type(Enum):
  generic                                                  = 0       
  running                                                  = 1       
  cycling                                                  = 2       
  transition                                               = 3       # Mulitsport transition
  fitness_equipment                                        = 4       
  swimming                                                 = 5       
  walking                                                  = 6       
  sedentary                                                = 8       
  all                                                      = 254     # All is for goals only to include all sports.

  @staticmethod
  def basetype():
    return basetypes.enum

class activity_subtype(Enum):
  generic                                                  = 0       
  treadmill                                                = 1       # Run
  street                                                   = 2       # Run
  trail                                                    = 3       # Run
  track                                                    = 4       # Run
  spin                                                     = 5       # Cycling
  indoor_cycling                                           = 6       # Cycling
  road                                                     = 7       # Cycling
  mountain                                                 = 8       # Cycling
  downhill                                                 = 9       # Cycling
  recumbent                                                = 10      # Cycling
  cyclocross                                               = 11      # Cycling
  hand_cycling                                             = 12      # Cycling
  track_cycling                                            = 13      # Cycling
  indoor_rowing                                            = 14      # Fitness Equipment
  elliptical                                               = 15      # Fitness Equipment
  stair_climbing                                           = 16      # Fitness Equipment
  lap_swimming                                             = 17      # Swimming
  open_water                                               = 18      # Swimming
  all                                                      = 254     

  @staticmethod
  def basetype():
    return basetypes.enum

class activity_level(Enum):
  low                                                      = 0       
  medium                                                   = 1       
  high                                                     = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class side(Enum):
  right                                                    = 0       
  left                                                     = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class left_right_balance(Enum):
  mask                                                     = 0x7F    # % contribution
  right                                                    = 0x80    # data corresponds to right if set, otherwise unknown

  @staticmethod
  def basetype():
    return basetypes.uint8

class left_right_balance_100(Enum):
  mask                                                     = 0x3FFF  # % contribution scaled by 100
  right                                                    = 0x8000  # data corresponds to right if set, otherwise unknown

  @staticmethod
  def basetype():
    return basetypes.uint16

class length_type(Enum):
  idle                                                     = 0       # Rest period. Length with no strokes
  active                                                   = 1       # Length with strokes.

  @staticmethod
  def basetype():
    return basetypes.enum

class day_of_week(Enum):
  sunday                                                   = 0       
  monday                                                   = 1       
  tuesday                                                  = 2       
  wednesday                                                = 3       
  thursday                                                 = 4       
  friday                                                   = 5       
  saturday                                                 = 6       

  @staticmethod
  def basetype():
    return basetypes.enum

class connectivity_capabilities(Enum):
  bluetooth                                                = 0x00000001
  bluetooth_le                                             = 0x00000002
  ant                                                      = 0x00000004
  activity_upload                                          = 0x00000008
  course_download                                          = 0x00000010
  workout_download                                         = 0x00000020
  live_track                                               = 0x00000040
  weather_conditions                                       = 0x00000080
  weather_alerts                                           = 0x00000100
  gps_ephemeris_download                                   = 0x00000200
  explicit_archive                                         = 0x00000400
  setup_incomplete                                         = 0x00000800
  continue_sync_after_software_update                      = 0x00001000
  connect_iq_app_download                                  = 0x00002000
  golf_course_download                                     = 0x00004000
  device_initiates_sync                                    = 0x00008000# Indicates device is in control of initiating all syncs
  connect_iq_watch_app_download                            = 0x00010000
  connect_iq_widget_download                               = 0x00020000
  connect_iq_watch_face_download                           = 0x00040000
  connect_iq_data_field_download                           = 0x00080000
  connect_iq_app_managment                                 = 0x00100000# Device supports delete and reorder of apps via GCM
  swing_sensor                                             = 0x00200000
  swing_sensor_remote                                      = 0x00400000
  incident_detection                                       = 0x00800000# Device supports incident detection
  audio_prompts                                            = 0x01000000
  wifi_verification                                        = 0x02000000# Device supports reporting wifi verification via GCM
  true_up                                                  = 0x04000000# Device supports True Up
  find_my_watch                                            = 0x08000000# Device supports Find My Watch
  remote_manual_sync                                       = 0x10000000
  live_track_auto_start                                    = 0x20000000# Device supports LiveTrack auto start
  live_track_messaging                                     = 0x40000000# Device supports LiveTrack Messaging
  instant_input                                            = 0x80000000# Device supports instant input feature

  @staticmethod
  def basetype():
    return basetypes.uint32z

class weather_report(Enum):
  current                                                  = 0       
  forecast                                                 = 1       # Deprecated use hourly_forecast instead
  hourly_forecast                                          = 1       
  daily_forecast                                           = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class weather_status(Enum):
  clear                                                    = 0       
  partly_cloudy                                            = 1       
  mostly_cloudy                                            = 2       
  rain                                                     = 3       
  snow                                                     = 4       
  windy                                                    = 5       
  thunderstorms                                            = 6       
  wintry_mix                                               = 7       
  fog                                                      = 8       
  hazy                                                     = 11      
  hail                                                     = 12      
  scattered_showers                                        = 13      
  scattered_thunderstorms                                  = 14      
  unknown_precipitation                                    = 15      
  light_rain                                               = 16      
  heavy_rain                                               = 17      
  light_snow                                               = 18      
  heavy_snow                                               = 19      
  light_rain_snow                                          = 20      
  heavy_rain_snow                                          = 21      
  cloudy                                                   = 22      

  @staticmethod
  def basetype():
    return basetypes.enum

class weather_severity(Enum):
  unknown                                                  = 0       
  warning                                                  = 1       
  watch                                                    = 2       
  advisory                                                 = 3       
  statement                                                = 4       

  @staticmethod
  def basetype():
    return basetypes.enum

class weather_severe_type(Enum):
  unspecified                                              = 0       
  tornado                                                  = 1       
  tsunami                                                  = 2       
  hurricane                                                = 3       
  extreme_wind                                             = 4       
  typhoon                                                  = 5       
  inland_hurricane                                         = 6       
  hurricane_force_wind                                     = 7       
  waterspout                                               = 8       
  severe_thunderstorm                                      = 9       
  wreckhouse_winds                                         = 10      
  les_suetes_wind                                          = 11      
  avalanche                                                = 12      
  flash_flood                                              = 13      
  tropical_storm                                           = 14      
  inland_tropical_storm                                    = 15      
  blizzard                                                 = 16      
  ice_storm                                                = 17      
  freezing_rain                                            = 18      
  debris_flow                                              = 19      
  flash_freeze                                             = 20      
  dust_storm                                               = 21      
  high_wind                                                = 22      
  winter_storm                                             = 23      
  heavy_freezing_spray                                     = 24      
  extreme_cold                                             = 25      
  wind_chill                                               = 26      
  cold_wave                                                = 27      
  heavy_snow_alert                                         = 28      
  lake_effect_blowing_snow                                 = 29      
  snow_squall                                              = 30      
  lake_effect_snow                                         = 31      
  winter_weather                                           = 32      
  sleet                                                    = 33      
  snowfall                                                 = 34      
  snow_and_blowing_snow                                    = 35      
  blowing_snow                                             = 36      
  snow_alert                                               = 37      
  arctic_outflow                                           = 38      
  freezing_drizzle                                         = 39      
  storm                                                    = 40      
  storm_surge                                              = 41      
  rainfall                                                 = 42      
  areal_flood                                              = 43      
  coastal_flood                                            = 44      
  lakeshore_flood                                          = 45      
  excessive_heat                                           = 46      
  heat                                                     = 47      
  weather                                                  = 48      
  high_heat_and_humidity                                   = 49      
  humidex_and_health                                       = 50      
  humidex                                                  = 51      
  gale                                                     = 52      
  freezing_spray                                           = 53      
  special_marine                                           = 54      
  squall                                                   = 55      
  strong_wind                                              = 56      
  lake_wind                                                = 57      
  marine_weather                                           = 58      
  wind                                                     = 59      
  small_craft_hazardous_seas                               = 60      
  hazardous_seas                                           = 61      
  small_craft                                              = 62      
  small_craft_winds                                        = 63      
  small_craft_rough_bar                                    = 64      
  high_water_level                                         = 65      
  ashfall                                                  = 66      
  freezing_fog                                             = 67      
  dense_fog                                                = 68      
  dense_smoke                                              = 69      
  blowing_dust                                             = 70      
  hard_freeze                                              = 71      
  freeze                                                   = 72      
  frost                                                    = 73      
  fire_weather                                             = 74      
  flood                                                    = 75      
  rip_tide                                                 = 76      
  high_surf                                                = 77      
  smog                                                     = 78      
  air_quality                                              = 79      
  brisk_wind                                               = 80      
  air_stagnation                                           = 81      
  low_water                                                = 82      
  hydrological                                             = 83      
  special_weather                                          = 84      

  @staticmethod
  def basetype():
    return basetypes.enum

class time_into_day(Enum):

  @staticmethod
  def basetype():
    return basetypes.uint32

class localtime_into_day(Enum):

  @staticmethod
  def basetype():
    return basetypes.uint32

class stroke_type(Enum):
  no_event                                                 = 0       
  other                                                    = 1       # stroke was detected but cannot be identified
  serve                                                    = 2       
  forehand                                                 = 3       
  backhand                                                 = 4       
  smash                                                    = 5       

  @staticmethod
  def basetype():
    return basetypes.enum

class body_location(Enum):
  left_leg                                                 = 0       
  left_calf                                                = 1       
  left_shin                                                = 2       
  left_hamstring                                           = 3       
  left_quad                                                = 4       
  left_glute                                               = 5       
  right_leg                                                = 6       
  right_calf                                               = 7       
  right_shin                                               = 8       
  right_hamstring                                          = 9       
  right_quad                                               = 10      
  right_glute                                              = 11      
  torso_back                                               = 12      
  left_lower_back                                          = 13      
  left_upper_back                                          = 14      
  right_lower_back                                         = 15      
  right_upper_back                                         = 16      
  torso_front                                              = 17      
  left_abdomen                                             = 18      
  left_chest                                               = 19      
  right_abdomen                                            = 20      
  right_chest                                              = 21      
  left_arm                                                 = 22      
  left_shoulder                                            = 23      
  left_bicep                                               = 24      
  left_tricep                                              = 25      
  left_brachioradialis                                     = 26      # Left anterior forearm
  left_forearm_extensors                                   = 27      # Left posterior forearm
  right_arm                                                = 28      
  right_shoulder                                           = 29      
  right_bicep                                              = 30      
  right_tricep                                             = 31      
  right_brachioradialis                                    = 32      # Right anterior forearm
  right_forearm_extensors                                  = 33      # Right posterior forearm
  neck                                                     = 34      
  throat                                                   = 35      
  waist_mid_back                                           = 36      
  waist_front                                              = 37      
  waist_left                                               = 38      
  waist_right                                              = 39      

  @staticmethod
  def basetype():
    return basetypes.enum

class segment_lap_status(Enum):
  end                                                      = 0       
  fail                                                     = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class segment_leaderboard_type(Enum):
  overall                                                  = 0       
  personal_best                                            = 1       
  connections                                              = 2       
  group                                                    = 3       
  challenger                                               = 4       
  kom                                                      = 5       
  qom                                                      = 6       
  pr                                                       = 7       
  goal                                                     = 8       
  rival                                                    = 9       
  club_leader                                              = 10      

  @staticmethod
  def basetype():
    return basetypes.enum

class segment_delete_status(Enum):
  do_not_delete                                            = 0       
  delete_one                                               = 1       
  delete_all                                               = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class segment_selection_type(Enum):
  starred                                                  = 0       
  suggested                                                = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class source_type(Enum):
  ant                                                      = 0       # External device connected with ANT
  antplus                                                  = 1       # External device connected with ANT+
  bluetooth                                                = 2       # External device connected with BT
  bluetooth_low_energy                                     = 3       # External device connected with BLE
  wifi                                                     = 4       # External device connected with Wifi
  local                                                    = 5       # Onboard device

  @staticmethod
  def basetype():
    return basetypes.enum

class local_device_type(Enum):

  @staticmethod
  def basetype():
    return basetypes.uint8

class display_orientation(Enum):
  auto                                                     = 0       # automatic if the device supports it
  portrait                                                 = 1       
  landscape                                                = 2       
  portrait_flipped                                         = 3       # portrait mode but rotated 180 degrees
  landscape_flipped                                        = 4       # landscape mode but rotated 180 degrees

  @staticmethod
  def basetype():
    return basetypes.enum

class workout_equipment(Enum):
  none                                                     = 0       
  swim_fins                                                = 1       
  swim_kickboard                                           = 2       
  swim_paddles                                             = 3       
  swim_pull_buoy                                           = 4       
  swim_snorkel                                             = 5       

  @staticmethod
  def basetype():
    return basetypes.enum

class watchface_mode(Enum):
  digital                                                  = 0       
  analog                                                   = 1       
  connect_iq                                               = 2       
  disabled                                                 = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class digital_watchface_layout(Enum):
  traditional                                              = 0       
  modern                                                   = 1       
  bold                                                     = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class analog_watchface_layout(Enum):
  minimal                                                  = 0       
  traditional                                              = 1       
  modern                                                   = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class rider_position_type(Enum):
  seated                                                   = 0       
  standing                                                 = 1       
  transition_to_seated                                     = 2       
  transition_to_standing                                   = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class power_phase_type(Enum):
  power_phase_start_angle                                  = 0       
  power_phase_end_angle                                    = 1       
  power_phase_arc_length                                   = 2       
  power_phase_center                                       = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class camera_event_type(Enum):
  video_start                                              = 0       # Start of video recording
  video_split                                              = 1       # Mark of video file split (end of one file, beginning of the other)
  video_end                                                = 2       # End of video recording
  photo_taken                                              = 3       # Still photo taken
  video_second_stream_start                                = 4       
  video_second_stream_split                                = 5       
  video_second_stream_end                                  = 6       
  video_split_start                                        = 7       # Mark of video file split start
  video_second_stream_split_start                          = 8       
  video_pause                                              = 11      # Mark when a video recording has been paused
  video_second_stream_pause                                = 12      
  video_resume                                             = 13      # Mark when a video recording has been resumed
  video_second_stream_resume                               = 14      

  @staticmethod
  def basetype():
    return basetypes.enum

class sensor_type(Enum):
  accelerometer                                            = 0       
  gyroscope                                                = 1       
  compass                                                  = 2       # Magnetometer
  barometer                                                = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class bike_light_network_config_type(Enum):
  auto                                                     = 0       
  individual                                               = 4       
  high_visibility                                          = 5       
  trail                                                    = 6       

  @staticmethod
  def basetype():
    return basetypes.enum

class comm_timeout_type(Enum):
  wildcard_pairing_timeout                                 = 0       # Timeout pairing to any device
  pairing_timeout                                          = 1       # Timeout pairing to previously paired device
  connection_lost                                          = 2       # Temporary loss of communications
  connection_timeout                                       = 3       # Connection closed due to extended bad communications

  @staticmethod
  def basetype():
    return basetypes.uint16

class camera_orientation_type(Enum):
  camera_orientation_0                                     = 0       
  camera_orientation_90                                    = 1       
  camera_orientation_180                                   = 2       
  camera_orientation_270                                   = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class attitude_stage(Enum):
  failed                                                   = 0       
  aligning                                                 = 1       
  degraded                                                 = 2       
  valid                                                    = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class attitude_validity(Enum):
  track_angle_heading_valid                                = 0x0001  
  pitch_valid                                              = 0x0002  
  roll_valid                                               = 0x0004  
  lateral_body_accel_valid                                 = 0x0008  
  normal_body_accel_valid                                  = 0x0010  
  turn_rate_valid                                          = 0x0020  
  hw_fail                                                  = 0x0040  
  mag_invalid                                              = 0x0080  
  no_gps                                                   = 0x0100  
  gps_invalid                                              = 0x0200  
  solution_coasting                                        = 0x0400  
  true_track_angle                                         = 0x0800  
  magnetic_heading                                         = 0x1000  

  @staticmethod
  def basetype():
    return basetypes.uint16

class auto_sync_frequency(Enum):
  never                                                    = 0       
  occasionally                                             = 1       
  frequent                                                 = 2       
  once_a_day                                               = 3       
  remote                                                   = 4       

  @staticmethod
  def basetype():
    return basetypes.enum

class exd_layout(Enum):
  full_screen                                              = 0       
  half_vertical                                            = 1       
  half_horizontal                                          = 2       
  half_vertical_right_split                                = 3       
  half_horizontal_bottom_split                             = 4       
  full_quarter_split                                       = 5       
  half_vertical_left_split                                 = 6       
  half_horizontal_top_split                                = 7       

  @staticmethod
  def basetype():
    return basetypes.enum

class exd_display_type(Enum):
  numerical                                                = 0       
  simple                                                   = 1       
  graph                                                    = 2       
  bar                                                      = 3       
  circle_graph                                             = 4       
  virtual_partner                                          = 5       
  balance                                                  = 6       
  string_list                                              = 7       
  string                                                   = 8       
  simple_dynamic_icon                                      = 9       
  gauge                                                    = 10      

  @staticmethod
  def basetype():
    return basetypes.enum

class exd_data_units(Enum):
  no_units                                                 = 0       
  laps                                                     = 1       
  miles_per_hour                                           = 2       
  kilometers_per_hour                                      = 3       
  feet_per_hour                                            = 4       
  meters_per_hour                                          = 5       
  degrees_celsius                                          = 6       
  degrees_farenheit                                        = 7       
  zone                                                     = 8       
  gear                                                     = 9       
  rpm                                                      = 10      
  bpm                                                      = 11      
  degrees                                                  = 12      
  millimeters                                              = 13      
  meters                                                   = 14      
  kilometers                                               = 15      
  feet                                                     = 16      
  yards                                                    = 17      
  kilofeet                                                 = 18      
  miles                                                    = 19      
  time                                                     = 20      
  enum_turn_type                                           = 21      
  percent                                                  = 22      
  watts                                                    = 23      
  watts_per_kilogram                                       = 24      
  enum_battery_status                                      = 25      
  enum_bike_light_beam_angle_mode                          = 26      
  enum_bike_light_battery_status                           = 27      
  enum_bike_light_network_config_type                      = 28      
  lights                                                   = 29      
  seconds                                                  = 30      
  minutes                                                  = 31      
  hours                                                    = 32      
  calories                                                 = 33      
  kilojoules                                               = 34      
  milliseconds                                             = 35      
  second_per_mile                                          = 36      
  second_per_kilometer                                     = 37      
  centimeter                                               = 38      
  enum_course_point                                        = 39      
  bradians                                                 = 40      
  enum_sport                                               = 41      
  inches_hg                                                = 42      
  mm_hg                                                    = 43      
  mbars                                                    = 44      
  hecto_pascals                                            = 45      
  feet_per_min                                             = 46      
  meters_per_min                                           = 47      
  meters_per_sec                                           = 48      
  eight_cardinal                                           = 49      

  @staticmethod
  def basetype():
    return basetypes.enum

class exd_qualifiers(Enum):
  no_qualifier                                             = 0       
  instantaneous                                            = 1       
  average                                                  = 2       
  lap                                                      = 3       
  maximum                                                  = 4       
  maximum_average                                          = 5       
  maximum_lap                                              = 6       
  last_lap                                                 = 7       
  average_lap                                              = 8       
  to_destination                                           = 9       
  to_go                                                    = 10      
  to_next                                                  = 11      
  next_course_point                                        = 12      
  total                                                    = 13      
  three_second_average                                     = 14      
  ten_second_average                                       = 15      
  thirty_second_average                                    = 16      
  percent_maximum                                          = 17      
  percent_maximum_average                                  = 18      
  lap_percent_maximum                                      = 19      
  elapsed                                                  = 20      
  sunrise                                                  = 21      
  sunset                                                   = 22      
  compared_to_virtual_partner                              = 23      
  maximum_24h                                              = 24      
  minimum_24h                                              = 25      
  minimum                                                  = 26      
  first                                                    = 27      
  second                                                   = 28      
  third                                                    = 29      
  shifter                                                  = 30      
  last_sport                                               = 31      
  moving                                                   = 32      
  stopped                                                  = 33      
  estimated_total                                          = 34      
  zone_9                                                   = 242     
  zone_8                                                   = 243     
  zone_7                                                   = 244     
  zone_6                                                   = 245     
  zone_5                                                   = 246     
  zone_4                                                   = 247     
  zone_3                                                   = 248     
  zone_2                                                   = 249     
  zone_1                                                   = 250     

  @staticmethod
  def basetype():
    return basetypes.enum

class exd_descriptors(Enum):
  bike_light_battery_status                                = 0       
  beam_angle_status                                        = 1       
  batery_level                                             = 2       
  light_network_mode                                       = 3       
  number_lights_connected                                  = 4       
  cadence                                                  = 5       
  distance                                                 = 6       
  estimated_time_of_arrival                                = 7       
  heading                                                  = 8       
  time                                                     = 9       
  battery_level                                            = 10      
  trainer_resistance                                       = 11      
  trainer_target_power                                     = 12      
  time_seated                                              = 13      
  time_standing                                            = 14      
  elevation                                                = 15      
  grade                                                    = 16      
  ascent                                                   = 17      
  descent                                                  = 18      
  vertical_speed                                           = 19      
  di2_battery_level                                        = 20      
  front_gear                                               = 21      
  rear_gear                                                = 22      
  gear_ratio                                               = 23      
  heart_rate                                               = 24      
  heart_rate_zone                                          = 25      
  time_in_heart_rate_zone                                  = 26      
  heart_rate_reserve                                       = 27      
  calories                                                 = 28      
  gps_accuracy                                             = 29      
  gps_signal_strength                                      = 30      
  temperature                                              = 31      
  time_of_day                                              = 32      
  balance                                                  = 33      
  pedal_smoothness                                         = 34      
  power                                                    = 35      
  functional_threshold_power                               = 36      
  intensity_factor                                         = 37      
  work                                                     = 38      
  power_ratio                                              = 39      
  normalized_power                                         = 40      
  training_stress_Score                                    = 41      
  time_on_zone                                             = 42      
  speed                                                    = 43      
  laps                                                     = 44      
  reps                                                     = 45      
  workout_step                                             = 46      
  course_distance                                          = 47      
  navigation_distance                                      = 48      
  course_estimated_time_of_arrival                         = 49      
  navigation_estimated_time_of_arrival                     = 50      
  course_time                                              = 51      
  navigation_time                                          = 52      
  course_heading                                           = 53      
  navigation_heading                                       = 54      
  power_zone                                               = 55      
  torque_effectiveness                                     = 56      
  timer_time                                               = 57      
  power_weight_ratio                                       = 58      
  left_platform_center_offset                              = 59      
  right_platform_center_offset                             = 60      
  left_power_phase_start_angle                             = 61      
  right_power_phase_start_angle                            = 62      
  left_power_phase_finish_angle                            = 63      
  right_power_phase_finish_angle                           = 64      
  gears                                                    = 65      # Combined gear information
  pace                                                     = 66      
  training_effect                                          = 67      
  vertical_oscillation                                     = 68      
  vertical_ratio                                           = 69      
  ground_contact_time                                      = 70      
  left_ground_contact_time_balance                         = 71      
  right_ground_contact_time_balance                        = 72      
  stride_length                                            = 73      
  running_cadence                                          = 74      
  performance_condition                                    = 75      
  course_type                                              = 76      
  time_in_power_zone                                       = 77      
  navigation_turn                                          = 78      
  course_location                                          = 79      
  navigation_location                                      = 80      
  compass                                                  = 81      
  gear_combo                                               = 82      
  muscle_oxygen                                            = 83      
  icon                                                     = 84      
  compass_heading                                          = 85      
  gps_heading                                              = 86      
  gps_elevation                                            = 87      
  anaerobic_training_effect                                = 88      
  course                                                   = 89      
  off_course                                               = 90      
  glide_ratio                                              = 91      
  vertical_distance                                        = 92      
  vmg                                                      = 93      
  ambient_pressure                                         = 94      
  pressure                                                 = 95      
  vam                                                      = 96      

  @staticmethod
  def basetype():
    return basetypes.enum

class auto_activity_detect(Enum):
  none                                                     = 0x00000000
  running                                                  = 0x00000001
  cycling                                                  = 0x00000002
  swimming                                                 = 0x00000004
  walking                                                  = 0x00000008
  elliptical                                               = 0x00000020
  sedentary                                                = 0x00000400

  @staticmethod
  def basetype():
    return basetypes.uint32

class supported_exd_screen_layouts(Enum):
  full_screen                                              = 0x00000001
  half_vertical                                            = 0x00000002
  half_horizontal                                          = 0x00000004
  half_vertical_right_split                                = 0x00000008
  half_horizontal_bottom_split                             = 0x00000010
  full_quarter_split                                       = 0x00000020
  half_vertical_left_split                                 = 0x00000040
  half_horizontal_top_split                                = 0x00000080

  @staticmethod
  def basetype():
    return basetypes.uint32z

class fit_base_type(Enum):
  enum                                                     = 0       
  sint8                                                    = 1       
  uint8                                                    = 2       
  sint16                                                   = 131     
  uint16                                                   = 132     
  sint32                                                   = 133     
  uint32                                                   = 134     
  string                                                   = 7       
  float32                                                  = 136     
  float64                                                  = 137     
  uint8z                                                   = 10      
  uint16z                                                  = 139     
  uint32z                                                  = 140     
  byte                                                     = 13      
  sint64                                                   = 142     
  uint64                                                   = 143     
  uint64z                                                  = 144     

  @staticmethod
  def basetype():
    return basetypes.uint8

class turn_type(Enum):
  arriving_idx                                             = 0       
  arriving_left_idx                                        = 1       
  arriving_right_idx                                       = 2       
  arriving_via_idx                                         = 3       
  arriving_via_left_idx                                    = 4       
  arriving_via_right_idx                                   = 5       
  bear_keep_left_idx                                       = 6       
  bear_keep_right_idx                                      = 7       
  continue_idx                                             = 8       
  exit_left_idx                                            = 9       
  exit_right_idx                                           = 10      
  ferry_idx                                                = 11      
  roundabout_45_idx                                        = 12      
  roundabout_90_idx                                        = 13      
  roundabout_135_idx                                       = 14      
  roundabout_180_idx                                       = 15      
  roundabout_225_idx                                       = 16      
  roundabout_270_idx                                       = 17      
  roundabout_315_idx                                       = 18      
  roundabout_360_idx                                       = 19      
  roundabout_neg_45_idx                                    = 20      
  roundabout_neg_90_idx                                    = 21      
  roundabout_neg_135_idx                                   = 22      
  roundabout_neg_180_idx                                   = 23      
  roundabout_neg_225_idx                                   = 24      
  roundabout_neg_270_idx                                   = 25      
  roundabout_neg_315_idx                                   = 26      
  roundabout_neg_360_idx                                   = 27      
  roundabout_generic_idx                                   = 28      
  roundabout_neg_generic_idx                               = 29      
  sharp_turn_left_idx                                      = 30      
  sharp_turn_right_idx                                     = 31      
  turn_left_idx                                            = 32      
  turn_right_idx                                           = 33      
  uturn_left_idx                                           = 34      
  uturn_right_idx                                          = 35      
  icon_inv_idx                                             = 36      
  icon_idx_cnt                                             = 37      

  @staticmethod
  def basetype():
    return basetypes.enum

class bike_light_beam_angle_mode(Enum):
  manual                                                   = 0       
  auto                                                     = 1       

  @staticmethod
  def basetype():
    return basetypes.uint8

class fit_base_unit(Enum):
  other                                                    = 0       
  kilogram                                                 = 1       
  pound                                                    = 2       

  @staticmethod
  def basetype():
    return basetypes.uint16

class set_type(Enum):
  rest                                                     = 0       
  active                                                   = 1       

  @staticmethod
  def basetype():
    return basetypes.uint8

class exercise_category(Enum):
  bench_press                                              = 0       
  calf_raise                                               = 1       
  cardio                                                   = 2       
  carry                                                    = 3       
  chop                                                     = 4       
  core                                                     = 5       
  crunch                                                   = 6       
  curl                                                     = 7       
  deadlift                                                 = 8       
  flye                                                     = 9       
  hip_raise                                                = 10      
  hip_stability                                            = 11      
  hip_swing                                                = 12      
  hyperextension                                           = 13      
  lateral_raise                                            = 14      
  leg_curl                                                 = 15      
  leg_raise                                                = 16      
  lunge                                                    = 17      
  olympic_lift                                             = 18      
  plank                                                    = 19      
  plyo                                                     = 20      
  pull_up                                                  = 21      
  push_up                                                  = 22      
  row                                                      = 23      
  shoulder_press                                           = 24      
  shoulder_stability                                       = 25      
  shrug                                                    = 26      
  sit_up                                                   = 27      
  squat                                                    = 28      
  total_body                                               = 29      
  triceps_extension                                        = 30      
  warm_up                                                  = 31      
  run                                                      = 32      
  unknown                                                  = 65534   

  @staticmethod
  def basetype():
    return basetypes.uint16

class bench_press_exercise_name(Enum):
  alternating_dumbbell_chest_press_on_swiss_ball           = 0       
  barbell_bench_press                                      = 1       
  barbell_board_bench_press                                = 2       
  barbell_floor_press                                      = 3       
  close_grip_barbell_bench_press                           = 4       
  decline_dumbbell_bench_press                             = 5       
  dumbbell_bench_press                                     = 6       
  dumbbell_floor_press                                     = 7       
  incline_barbell_bench_press                              = 8       
  incline_dumbbell_bench_press                             = 9       
  incline_smith_machine_bench_press                        = 10      
  isometric_barbell_bench_press                            = 11      
  kettlebell_chest_press                                   = 12      
  neutral_grip_dumbbell_bench_press                        = 13      
  neutral_grip_dumbbell_incline_bench_press                = 14      
  one_arm_floor_press                                      = 15      
  weighted_one_arm_floor_press                             = 16      
  partial_lockout                                          = 17      
  reverse_grip_barbell_bench_press                         = 18      
  reverse_grip_incline_bench_press                         = 19      
  single_arm_cable_chest_press                             = 20      
  single_arm_dumbbell_bench_press                          = 21      
  smith_machine_bench_press                                = 22      
  swiss_ball_dumbbell_chest_press                          = 23      
  triple_stop_barbell_bench_press                          = 24      
  wide_grip_barbell_bench_press                            = 25      
  alternating_dumbbell_chest_press                         = 26      

  @staticmethod
  def basetype():
    return basetypes.uint16

class calf_raise_exercise_name(Enum):
  _3_way_calf_raise                                        = 0       
  _3_way_weighted_calf_raise                               = 1       
  _3_way_single_leg_calf_raise                             = 2       
  _3_way_weighted_single_leg_calf_raise                    = 3       
  donkey_calf_raise                                        = 4       
  weighted_donkey_calf_raise                               = 5       
  seated_calf_raise                                        = 6       
  weighted_seated_calf_raise                               = 7       
  seated_dumbbell_toe_raise                                = 8       
  single_leg_bent_knee_calf_raise                          = 9       
  weighted_single_leg_bent_knee_calf_raise                 = 10      
  single_leg_decline_push_up                               = 11      
  single_leg_donkey_calf_raise                             = 12      
  weighted_single_leg_donkey_calf_raise                    = 13      
  single_leg_hip_raise_with_knee_hold                      = 14      
  single_leg_standing_calf_raise                           = 15      
  single_leg_standing_dumbbell_calf_raise                  = 16      
  standing_barbell_calf_raise                              = 17      
  standing_calf_raise                                      = 18      
  weighted_standing_calf_raise                             = 19      
  standing_dumbbell_calf_raise                             = 20      

  @staticmethod
  def basetype():
    return basetypes.uint16

class cardio_exercise_name(Enum):
  bob_and_weave_circle                                     = 0       
  weighted_bob_and_weave_circle                            = 1       
  cardio_core_crawl                                        = 2       
  weighted_cardio_core_crawl                               = 3       
  double_under                                             = 4       
  weighted_double_under                                    = 5       
  jump_rope                                                = 6       
  weighted_jump_rope                                       = 7       
  jump_rope_crossover                                      = 8       
  weighted_jump_rope_crossover                             = 9       
  jump_rope_jog                                            = 10      
  weighted_jump_rope_jog                                   = 11      
  jumping_jacks                                            = 12      
  weighted_jumping_jacks                                   = 13      
  ski_moguls                                               = 14      
  weighted_ski_moguls                                      = 15      
  split_jacks                                              = 16      
  weighted_split_jacks                                     = 17      
  squat_jacks                                              = 18      
  weighted_squat_jacks                                     = 19      
  triple_under                                             = 20      
  weighted_triple_under                                    = 21      

  @staticmethod
  def basetype():
    return basetypes.uint16

class carry_exercise_name(Enum):
  bar_holds                                                = 0       
  farmers_walk                                             = 1       
  farmers_walk_on_toes                                     = 2       
  hex_dumbbell_hold                                        = 3       
  overhead_carry                                           = 4       

  @staticmethod
  def basetype():
    return basetypes.uint16

class chop_exercise_name(Enum):
  cable_pull_through                                       = 0       
  cable_rotational_lift                                    = 1       
  cable_woodchop                                           = 2       
  cross_chop_to_knee                                       = 3       
  weighted_cross_chop_to_knee                              = 4       
  dumbbell_chop                                            = 5       
  half_kneeling_rotation                                   = 6       
  weighted_half_kneeling_rotation                          = 7       
  half_kneeling_rotational_chop                            = 8       
  half_kneeling_rotational_reverse_chop                    = 9       
  half_kneeling_stability_chop                             = 10      
  half_kneeling_stability_reverse_chop                     = 11      
  kneeling_rotational_chop                                 = 12      
  kneeling_rotational_reverse_chop                         = 13      
  kneeling_stability_chop                                  = 14      
  kneeling_woodchopper                                     = 15      
  medicine_ball_wood_chops                                 = 16      
  power_squat_chops                                        = 17      
  weighted_power_squat_chops                               = 18      
  standing_rotational_chop                                 = 19      
  standing_split_rotational_chop                           = 20      
  standing_split_rotational_reverse_chop                   = 21      
  standing_stability_reverse_chop                          = 22      

  @staticmethod
  def basetype():
    return basetypes.uint16

class core_exercise_name(Enum):
  abs_jabs                                                 = 0       
  weighted_abs_jabs                                        = 1       
  alternating_plate_reach                                  = 2       
  barbell_rollout                                          = 3       
  weighted_barbell_rollout                                 = 4       
  body_bar_oblique_twist                                   = 5       
  cable_core_press                                         = 6       
  cable_side_bend                                          = 7       
  side_bend                                                = 8       
  weighted_side_bend                                       = 9       
  crescent_circle                                          = 10      
  weighted_crescent_circle                                 = 11      
  cycling_russian_twist                                    = 12      
  weighted_cycling_russian_twist                           = 13      
  elevated_feet_russian_twist                              = 14      
  weighted_elevated_feet_russian_twist                     = 15      
  half_turkish_get_up                                      = 16      
  kettlebell_windmill                                      = 17      
  kneeling_ab_wheel                                        = 18      
  weighted_kneeling_ab_wheel                               = 19      
  modified_front_lever                                     = 20      
  open_knee_tucks                                          = 21      
  weighted_open_knee_tucks                                 = 22      
  side_abs_leg_lift                                        = 23      
  weighted_side_abs_leg_lift                               = 24      
  swiss_ball_jackknife                                     = 25      
  weighted_swiss_ball_jackknife                            = 26      
  swiss_ball_pike                                          = 27      
  weighted_swiss_ball_pike                                 = 28      
  swiss_ball_rollout                                       = 29      
  weighted_swiss_ball_rollout                              = 30      
  triangle_hip_press                                       = 31      
  weighted_triangle_hip_press                              = 32      
  trx_suspended_jackknife                                  = 33      
  weighted_trx_suspended_jackknife                         = 34      
  u_boat                                                   = 35      
  weighted_u_boat                                          = 36      
  windmill_switches                                        = 37      
  weighted_windmill_switches                               = 38      
  alternating_slide_out                                    = 39      
  weighted_alternating_slide_out                           = 40      
  ghd_back_extensions                                      = 41      
  weighted_ghd_back_extensions                             = 42      
  overhead_walk                                            = 43      
  inchworm                                                 = 44      
  weighted_modified_front_lever                            = 45      
  russian_twist                                            = 46      
  abdominal_leg_rotations                                  = 47      
  arm_and_leg_extension_on_knees                           = 48      
  bicycle                                                  = 49      
  bicep_curl_with_leg_extension                            = 50      
  cat_cow                                                  = 51      
  corkscrew                                                = 52      
  criss_cross                                              = 53      
  criss_cross_with_ball                                    = 54      
  double_leg_stretch                                       = 55      
  knee_folds                                               = 56      
  lower_lift                                               = 57      
  neck_pull                                                = 58      
  pelvic_clocks                                            = 59      
  roll_over                                                = 60      
  roll_up                                                  = 61      
  rolling                                                  = 62      
  rowing_1                                                 = 63      
  rowing_2                                                 = 64      
  scissors                                                 = 65      
  single_leg_circles                                       = 66      
  single_leg_stretch                                       = 67      
  snake_twist_1_and_2                                      = 68      
  swan                                                     = 69      
  swimming                                                 = 70      
  teaser                                                   = 71      
  the_hundred                                              = 72      

  @staticmethod
  def basetype():
    return basetypes.uint16

class crunch_exercise_name(Enum):
  bicycle_crunch                                           = 0       
  cable_crunch                                             = 1       
  circular_arm_crunch                                      = 2       
  crossed_arms_crunch                                      = 3       
  weighted_crossed_arms_crunch                             = 4       
  cross_leg_reverse_crunch                                 = 5       
  weighted_cross_leg_reverse_crunch                        = 6       
  crunch_chop                                              = 7       
  weighted_crunch_chop                                     = 8       
  double_crunch                                            = 9       
  weighted_double_crunch                                   = 10      
  elbow_to_knee_crunch                                     = 11      
  weighted_elbow_to_knee_crunch                            = 12      
  flutter_kicks                                            = 13      
  weighted_flutter_kicks                                   = 14      
  foam_roller_reverse_crunch_on_bench                      = 15      
  weighted_foam_roller_reverse_crunch_on_bench             = 16      
  foam_roller_reverse_crunch_with_dumbbell                 = 17      
  foam_roller_reverse_crunch_with_medicine_ball            = 18      
  frog_press                                               = 19      
  hanging_knee_raise_oblique_crunch                        = 20      
  weighted_hanging_knee_raise_oblique_crunch               = 21      
  hip_crossover                                            = 22      
  weighted_hip_crossover                                   = 23      
  hollow_rock                                              = 24      
  weighted_hollow_rock                                     = 25      
  incline_reverse_crunch                                   = 26      
  weighted_incline_reverse_crunch                          = 27      
  kneeling_cable_crunch                                    = 28      
  kneeling_cross_crunch                                    = 29      
  weighted_kneeling_cross_crunch                           = 30      
  kneeling_oblique_cable_crunch                            = 31      
  knees_to_elbow                                           = 32      
  leg_extensions                                           = 33      
  weighted_leg_extensions                                  = 34      
  leg_levers                                               = 35      
  mcgill_curl_up                                           = 36      
  weighted_mcgill_curl_up                                  = 37      
  modified_pilates_roll_up_with_ball                       = 38      
  weighted_modified_pilates_roll_up_with_ball              = 39      
  pilates_crunch                                           = 40      
  weighted_pilates_crunch                                  = 41      
  pilates_roll_up_with_ball                                = 42      
  weighted_pilates_roll_up_with_ball                       = 43      
  raised_legs_crunch                                       = 44      
  weighted_raised_legs_crunch                              = 45      
  reverse_crunch                                           = 46      
  weighted_reverse_crunch                                  = 47      
  reverse_crunch_on_a_bench                                = 48      
  weighted_reverse_crunch_on_a_bench                       = 49      
  reverse_curl_and_lift                                    = 50      
  weighted_reverse_curl_and_lift                           = 51      
  rotational_lift                                          = 52      
  weighted_rotational_lift                                 = 53      
  seated_alternating_reverse_crunch                        = 54      
  weighted_seated_alternating_reverse_crunch               = 55      
  seated_leg_u                                             = 56      
  weighted_seated_leg_u                                    = 57      
  side_to_side_crunch_and_weave                            = 58      
  weighted_side_to_side_crunch_and_weave                   = 59      
  single_leg_reverse_crunch                                = 60      
  weighted_single_leg_reverse_crunch                       = 61      
  skater_crunch_cross                                      = 62      
  weighted_skater_crunch_cross                             = 63      
  standing_cable_crunch                                    = 64      
  standing_side_crunch                                     = 65      
  step_climb                                               = 66      
  weighted_step_climb                                      = 67      
  swiss_ball_crunch                                        = 68      
  swiss_ball_reverse_crunch                                = 69      
  weighted_swiss_ball_reverse_crunch                       = 70      
  swiss_ball_russian_twist                                 = 71      
  weighted_swiss_ball_russian_twist                        = 72      
  swiss_ball_side_crunch                                   = 73      
  weighted_swiss_ball_side_crunch                          = 74      
  thoracic_crunches_on_foam_roller                         = 75      
  weighted_thoracic_crunches_on_foam_roller                = 76      
  triceps_crunch                                           = 77      
  weighted_bicycle_crunch                                  = 78      
  weighted_crunch                                          = 79      
  weighted_swiss_ball_crunch                               = 80      
  toes_to_bar                                              = 81      
  weighted_toes_to_bar                                     = 82      
  crunch                                                   = 83      
  straight_leg_crunch_with_ball                            = 84      

  @staticmethod
  def basetype():
    return basetypes.uint16

class curl_exercise_name(Enum):
  alternating_dumbbell_biceps_curl                         = 0       
  alternating_dumbbell_biceps_curl_on_swiss_ball           = 1       
  alternating_incline_dumbbell_biceps_curl                 = 2       
  barbell_biceps_curl                                      = 3       
  barbell_reverse_wrist_curl                               = 4       
  barbell_wrist_curl                                       = 5       
  behind_the_back_barbell_reverse_wrist_curl               = 6       
  behind_the_back_one_arm_cable_curl                       = 7       
  cable_biceps_curl                                        = 8       
  cable_hammer_curl                                        = 9       
  cheating_barbell_biceps_curl                             = 10      
  close_grip_ez_bar_biceps_curl                            = 11      
  cross_body_dumbbell_hammer_curl                          = 12      
  dead_hang_biceps_curl                                    = 13      
  decline_hammer_curl                                      = 14      
  dumbbell_biceps_curl_with_static_hold                    = 15      
  dumbbell_hammer_curl                                     = 16      
  dumbbell_reverse_wrist_curl                              = 17      
  dumbbell_wrist_curl                                      = 18      
  ez_bar_preacher_curl                                     = 19      
  forward_bend_biceps_curl                                 = 20      
  hammer_curl_to_press                                     = 21      
  incline_dumbbell_biceps_curl                             = 22      
  incline_offset_thumb_dumbbell_curl                       = 23      
  kettlebell_biceps_curl                                   = 24      
  lying_concentration_cable_curl                           = 25      
  one_arm_preacher_curl                                    = 26      
  plate_pinch_curl                                         = 27      
  preacher_curl_with_cable                                 = 28      
  reverse_ez_bar_curl                                      = 29      
  reverse_grip_wrist_curl                                  = 30      
  reverse_grip_barbell_biceps_curl                         = 31      
  seated_alternating_dumbbell_biceps_curl                  = 32      
  seated_dumbbell_biceps_curl                              = 33      
  seated_reverse_dumbbell_curl                             = 34      
  split_stance_offset_pinky_dumbbell_curl                  = 35      
  standing_alternating_dumbbell_curls                      = 36      
  standing_dumbbell_biceps_curl                            = 37      
  standing_ez_bar_biceps_curl                              = 38      
  static_curl                                              = 39      
  swiss_ball_dumbbell_overhead_triceps_extension           = 40      
  swiss_ball_ez_bar_preacher_curl                          = 41      
  twisting_standing_dumbbell_biceps_curl                   = 42      
  wide_grip_ez_bar_biceps_curl                             = 43      

  @staticmethod
  def basetype():
    return basetypes.uint16

class deadlift_exercise_name(Enum):
  barbell_deadlift                                         = 0       
  barbell_straight_leg_deadlift                            = 1       
  dumbbell_deadlift                                        = 2       
  dumbbell_single_leg_deadlift_to_row                      = 3       
  dumbbell_straight_leg_deadlift                           = 4       
  kettlebell_floor_to_shelf                                = 5       
  one_arm_one_leg_deadlift                                 = 6       
  rack_pull                                                = 7       
  rotational_dumbbell_straight_leg_deadlift                = 8       
  single_arm_deadlift                                      = 9       
  single_leg_barbell_deadlift                              = 10      
  single_leg_barbell_straight_leg_deadlift                 = 11      
  single_leg_deadlift_with_barbell                         = 12      
  single_leg_rdl_circuit                                   = 13      
  single_leg_romanian_deadlift_with_dumbbell               = 14      
  sumo_deadlift                                            = 15      
  sumo_deadlift_high_pull                                  = 16      
  trap_bar_deadlift                                        = 17      
  wide_grip_barbell_deadlift                               = 18      

  @staticmethod
  def basetype():
    return basetypes.uint16

class flye_exercise_name(Enum):
  cable_crossover                                          = 0       
  decline_dumbbell_flye                                    = 1       
  dumbbell_flye                                            = 2       
  incline_dumbbell_flye                                    = 3       
  kettlebell_flye                                          = 4       
  kneeling_rear_flye                                       = 5       
  single_arm_standing_cable_reverse_flye                   = 6       
  swiss_ball_dumbbell_flye                                 = 7       
  arm_rotations                                            = 8       
  hug_a_tree                                               = 9       

  @staticmethod
  def basetype():
    return basetypes.uint16

class hip_raise_exercise_name(Enum):
  barbell_hip_thrust_on_floor                              = 0       
  barbell_hip_thrust_with_bench                            = 1       
  bent_knee_swiss_ball_reverse_hip_raise                   = 2       
  weighted_bent_knee_swiss_ball_reverse_hip_raise          = 3       
  bridge_with_leg_extension                                = 4       
  weighted_bridge_with_leg_extension                       = 5       
  clam_bridge                                              = 6       
  front_kick_tabletop                                      = 7       
  weighted_front_kick_tabletop                             = 8       
  hip_extension_and_cross                                  = 9       
  weighted_hip_extension_and_cross                         = 10      
  hip_raise                                                = 11      
  weighted_hip_raise                                       = 12      
  hip_raise_with_feet_on_swiss_ball                        = 13      
  weighted_hip_raise_with_feet_on_swiss_ball               = 14      
  hip_raise_with_head_on_bosu_ball                         = 15      
  weighted_hip_raise_with_head_on_bosu_ball                = 16      
  hip_raise_with_head_on_swiss_ball                        = 17      
  weighted_hip_raise_with_head_on_swiss_ball               = 18      
  hip_raise_with_knee_squeeze                              = 19      
  weighted_hip_raise_with_knee_squeeze                     = 20      
  incline_rear_leg_extension                               = 21      
  weighted_incline_rear_leg_extension                      = 22      
  kettlebell_swing                                         = 23      
  marching_hip_raise                                       = 24      
  weighted_marching_hip_raise                              = 25      
  marching_hip_raise_with_feet_on_a_swiss_ball             = 26      
  weighted_marching_hip_raise_with_feet_on_a_swiss_ball    = 27      
  reverse_hip_raise                                        = 28      
  weighted_reverse_hip_raise                               = 29      
  single_leg_hip_raise                                     = 30      
  weighted_single_leg_hip_raise                            = 31      
  single_leg_hip_raise_with_foot_on_bench                  = 32      
  weighted_single_leg_hip_raise_with_foot_on_bench         = 33      
  single_leg_hip_raise_with_foot_on_bosu_ball              = 34      
  weighted_single_leg_hip_raise_with_foot_on_bosu_ball     = 35      
  single_leg_hip_raise_with_foot_on_foam_roller            = 36      
  weighted_single_leg_hip_raise_with_foot_on_foam_roller   = 37      
  single_leg_hip_raise_with_foot_on_medicine_ball          = 38      
  weighted_single_leg_hip_raise_with_foot_on_medicine_ball = 39      
  single_leg_hip_raise_with_head_on_bosu_ball              = 40      
  weighted_single_leg_hip_raise_with_head_on_bosu_ball     = 41      
  weighted_clam_bridge                                     = 42      
  single_leg_swiss_ball_hip_raise_and_leg_curl             = 43      
  clams                                                    = 44      
  inner_thigh_circles                                      = 45      
  inner_thigh_side_lift                                    = 46      
  leg_circles                                              = 47      
  leg_lift                                                 = 48      
  leg_lift_in_external_rotation                            = 49      

  @staticmethod
  def basetype():
    return basetypes.uint16

class hip_stability_exercise_name(Enum):
  band_side_lying_leg_raise                                = 0       
  dead_bug                                                 = 1       
  weighted_dead_bug                                        = 2       
  external_hip_raise                                       = 3       
  weighted_external_hip_raise                              = 4       
  fire_hydrant_kicks                                       = 5       
  weighted_fire_hydrant_kicks                              = 6       
  hip_circles                                              = 7       
  weighted_hip_circles                                     = 8       
  inner_thigh_lift                                         = 9       
  weighted_inner_thigh_lift                                = 10      
  lateral_walks_with_band_at_ankles                        = 11      
  pretzel_side_kick                                        = 12      
  weighted_pretzel_side_kick                               = 13      
  prone_hip_internal_rotation                              = 14      
  weighted_prone_hip_internal_rotation                     = 15      
  quadruped                                                = 16      
  quadruped_hip_extension                                  = 17      
  weighted_quadruped_hip_extension                         = 18      
  quadruped_with_leg_lift                                  = 19      
  weighted_quadruped_with_leg_lift                         = 20      
  side_lying_leg_raise                                     = 21      
  weighted_side_lying_leg_raise                            = 22      
  sliding_hip_adduction                                    = 23      
  weighted_sliding_hip_adduction                           = 24      
  standing_adduction                                       = 25      
  weighted_standing_adduction                              = 26      
  standing_cable_hip_abduction                             = 27      
  standing_hip_abduction                                   = 28      
  weighted_standing_hip_abduction                          = 29      
  standing_rear_leg_raise                                  = 30      
  weighted_standing_rear_leg_raise                         = 31      
  supine_hip_internal_rotation                             = 32      
  weighted_supine_hip_internal_rotation                    = 33      

  @staticmethod
  def basetype():
    return basetypes.uint16

class hip_swing_exercise_name(Enum):
  single_arm_kettlebell_swing                              = 0       
  single_arm_dumbbell_swing                                = 1       
  step_out_swing                                           = 2       

  @staticmethod
  def basetype():
    return basetypes.uint16

class hyperextension_exercise_name(Enum):
  back_extension_with_opposite_arm_and_leg_reach           = 0       
  weighted_back_extension_with_opposite_arm_and_leg_reach  = 1       
  base_rotations                                           = 2       
  weighted_base_rotations                                  = 3       
  bent_knee_reverse_hyperextension                         = 4       
  weighted_bent_knee_reverse_hyperextension                = 5       
  hollow_hold_and_roll                                     = 6       
  weighted_hollow_hold_and_roll                            = 7       
  kicks                                                    = 8       
  weighted_kicks                                           = 9       
  knee_raises                                              = 10      
  weighted_knee_raises                                     = 11      
  kneeling_superman                                        = 12      
  weighted_kneeling_superman                               = 13      
  lat_pull_down_with_row                                   = 14      
  medicine_ball_deadlift_to_reach                          = 15      
  one_arm_one_leg_row                                      = 16      
  one_arm_row_with_band                                    = 17      
  overhead_lunge_with_medicine_ball                        = 18      
  plank_knee_tucks                                         = 19      
  weighted_plank_knee_tucks                                = 20      
  side_step                                                = 21      
  weighted_side_step                                       = 22      
  single_leg_back_extension                                = 23      
  weighted_single_leg_back_extension                       = 24      
  spine_extension                                          = 25      
  weighted_spine_extension                                 = 26      
  static_back_extension                                    = 27      
  weighted_static_back_extension                           = 28      
  superman_from_floor                                      = 29      
  weighted_superman_from_floor                             = 30      
  swiss_ball_back_extension                                = 31      
  weighted_swiss_ball_back_extension                       = 32      
  swiss_ball_hyperextension                                = 33      
  weighted_swiss_ball_hyperextension                       = 34      
  swiss_ball_opposite_arm_and_leg_lift                     = 35      
  weighted_swiss_ball_opposite_arm_and_leg_lift            = 36      
  superman_on_swiss_ball                                   = 37      
  cobra                                                    = 38      
  supine_floor_barre                                       = 39      

  @staticmethod
  def basetype():
    return basetypes.uint16

class lateral_raise_exercise_name(Enum):
  _45_degree_cable_external_rotation                       = 0       
  alternating_lateral_raise_with_static_hold               = 1       
  bar_muscle_up                                            = 2       
  bent_over_lateral_raise                                  = 3       
  cable_diagonal_raise                                     = 4       
  cable_front_raise                                        = 5       
  calorie_row                                              = 6       
  combo_shoulder_raise                                     = 7       
  dumbbell_diagonal_raise                                  = 8       
  dumbbell_v_raise                                         = 9       
  front_raise                                              = 10      
  leaning_dumbbell_lateral_raise                           = 11      
  lying_dumbbell_raise                                     = 12      
  muscle_up                                                = 13      
  one_arm_cable_lateral_raise                              = 14      
  overhand_grip_rear_lateral_raise                         = 15      
  plate_raises                                             = 16      
  ring_dip                                                 = 17      
  weighted_ring_dip                                        = 18      
  ring_muscle_up                                           = 19      
  weighted_ring_muscle_up                                  = 20      
  rope_climb                                               = 21      
  weighted_rope_climb                                      = 22      
  scaption                                                 = 23      
  seated_lateral_raise                                     = 24      
  seated_rear_lateral_raise                                = 25      
  side_lying_lateral_raise                                 = 26      
  standing_lift                                            = 27      
  suspended_row                                            = 28      
  underhand_grip_rear_lateral_raise                        = 29      
  wall_slide                                               = 30      
  weighted_wall_slide                                      = 31      
  arm_circles                                              = 32      
  shaving_the_head                                         = 33      

  @staticmethod
  def basetype():
    return basetypes.uint16

class leg_curl_exercise_name(Enum):
  leg_curl                                                 = 0       
  weighted_leg_curl                                        = 1       
  good_morning                                             = 2       
  seated_barbell_good_morning                              = 3       
  single_leg_barbell_good_morning                          = 4       
  single_leg_sliding_leg_curl                              = 5       
  sliding_leg_curl                                         = 6       
  split_barbell_good_morning                               = 7       
  split_stance_extension                                   = 8       
  staggered_stance_good_morning                            = 9       
  swiss_ball_hip_raise_and_leg_curl                        = 10      
  zercher_good_morning                                     = 11      

  @staticmethod
  def basetype():
    return basetypes.uint16

class leg_raise_exercise_name(Enum):
  hanging_knee_raise                                       = 0       
  hanging_leg_raise                                        = 1       
  weighted_hanging_leg_raise                               = 2       
  hanging_single_leg_raise                                 = 3       
  weighted_hanging_single_leg_raise                        = 4       
  kettlebell_leg_raises                                    = 5       
  leg_lowering_drill                                       = 6       
  weighted_leg_lowering_drill                              = 7       
  lying_straight_leg_raise                                 = 8       
  weighted_lying_straight_leg_raise                        = 9       
  medicine_ball_leg_drops                                  = 10      
  quadruped_leg_raise                                      = 11      
  weighted_quadruped_leg_raise                             = 12      
  reverse_leg_raise                                        = 13      
  weighted_reverse_leg_raise                               = 14      
  reverse_leg_raise_on_swiss_ball                          = 15      
  weighted_reverse_leg_raise_on_swiss_ball                 = 16      
  single_leg_lowering_drill                                = 17      
  weighted_single_leg_lowering_drill                       = 18      
  weighted_hanging_knee_raise                              = 19      
  lateral_stepover                                         = 20      
  weighted_lateral_stepover                                = 21      

  @staticmethod
  def basetype():
    return basetypes.uint16

class lunge_exercise_name(Enum):
  overhead_lunge                                           = 0       
  lunge_matrix                                             = 1       
  weighted_lunge_matrix                                    = 2       
  alternating_barbell_forward_lunge                        = 3       
  alternating_dumbbell_lunge_with_reach                    = 4       
  back_foot_elevated_dumbbell_split_squat                  = 5       
  barbell_box_lunge                                        = 6       
  barbell_bulgarian_split_squat                            = 7       
  barbell_crossover_lunge                                  = 8       
  barbell_front_split_squat                                = 9       
  barbell_lunge                                            = 10      
  barbell_reverse_lunge                                    = 11      
  barbell_side_lunge                                       = 12      
  barbell_split_squat                                      = 13      
  core_control_rear_lunge                                  = 14      
  diagonal_lunge                                           = 15      
  drop_lunge                                               = 16      
  dumbbell_box_lunge                                       = 17      
  dumbbell_bulgarian_split_squat                           = 18      
  dumbbell_crossover_lunge                                 = 19      
  dumbbell_diagonal_lunge                                  = 20      
  dumbbell_lunge                                           = 21      
  dumbbell_lunge_and_rotation                              = 22      
  dumbbell_overhead_bulgarian_split_squat                  = 23      
  dumbbell_reverse_lunge_to_high_knee_and_press            = 24      
  dumbbell_side_lunge                                      = 25      
  elevated_front_foot_barbell_split_squat                  = 26      
  front_foot_elevated_dumbbell_split_squat                 = 27      
  gunslinger_lunge                                         = 28      
  lawnmower_lunge                                          = 29      
  low_lunge_with_isometric_adduction                       = 30      
  low_side_to_side_lunge                                   = 31      
  lunge                                                    = 32      
  weighted_lunge                                           = 33      
  lunge_with_arm_reach                                     = 34      
  lunge_with_diagonal_reach                                = 35      
  lunge_with_side_bend                                     = 36      
  offset_dumbbell_lunge                                    = 37      
  offset_dumbbell_reverse_lunge                            = 38      
  overhead_bulgarian_split_squat                           = 39      
  overhead_dumbbell_reverse_lunge                          = 40      
  overhead_dumbbell_split_squat                            = 41      
  overhead_lunge_with_rotation                             = 42      
  reverse_barbell_box_lunge                                = 43      
  reverse_box_lunge                                        = 44      
  reverse_dumbbell_box_lunge                               = 45      
  reverse_dumbbell_crossover_lunge                         = 46      
  reverse_dumbbell_diagonal_lunge                          = 47      
  reverse_lunge_with_reach_back                            = 48      
  weighted_reverse_lunge_with_reach_back                   = 49      
  reverse_lunge_with_twist_and_overhead_reach              = 50      
  weighted_reverse_lunge_with_twist_and_overhead_reach     = 51      
  reverse_sliding_box_lunge                                = 52      
  weighted_reverse_sliding_box_lunge                       = 53      
  reverse_sliding_lunge                                    = 54      
  weighted_reverse_sliding_lunge                           = 55      
  runners_lunge_to_balance                                 = 56      
  weighted_runners_lunge_to_balance                        = 57      
  shifting_side_lunge                                      = 58      
  side_and_crossover_lunge                                 = 59      
  weighted_side_and_crossover_lunge                        = 60      
  side_lunge                                               = 61      
  weighted_side_lunge                                      = 62      
  side_lunge_and_press                                     = 63      
  side_lunge_jump_off                                      = 64      
  side_lunge_sweep                                         = 65      
  weighted_side_lunge_sweep                                = 66      
  side_lunge_to_crossover_tap                              = 67      
  weighted_side_lunge_to_crossover_tap                     = 68      
  side_to_side_lunge_chops                                 = 69      
  weighted_side_to_side_lunge_chops                        = 70      
  siff_jump_lunge                                          = 71      
  weighted_siff_jump_lunge                                 = 72      
  single_arm_reverse_lunge_and_press                       = 73      
  sliding_lateral_lunge                                    = 74      
  weighted_sliding_lateral_lunge                           = 75      
  walking_barbell_lunge                                    = 76      
  walking_dumbbell_lunge                                   = 77      
  walking_lunge                                            = 78      
  weighted_walking_lunge                                   = 79      
  wide_grip_overhead_barbell_split_squat                   = 80      

  @staticmethod
  def basetype():
    return basetypes.uint16

class olympic_lift_exercise_name(Enum):
  barbell_hang_power_clean                                 = 0       
  barbell_hang_squat_clean                                 = 1       
  barbell_power_clean                                      = 2       
  barbell_power_snatch                                     = 3       
  barbell_squat_clean                                      = 4       
  clean_and_jerk                                           = 5       
  barbell_hang_power_snatch                                = 6       
  barbell_hang_pull                                        = 7       
  barbell_high_pull                                        = 8       
  barbell_snatch                                           = 9       
  barbell_split_jerk                                       = 10      
  clean                                                    = 11      
  dumbbell_clean                                           = 12      
  dumbbell_hang_pull                                       = 13      
  one_hand_dumbbell_split_snatch                           = 14      
  push_jerk                                                = 15      
  single_arm_dumbbell_snatch                               = 16      
  single_arm_hang_snatch                                   = 17      
  single_arm_kettlebell_snatch                             = 18      
  split_jerk                                               = 19      
  squat_clean_and_jerk                                     = 20      

  @staticmethod
  def basetype():
    return basetypes.uint16

class plank_exercise_name(Enum):
  _45_degree_plank                                         = 0       
  weighted_45_degree_plank                                 = 1       
  _90_degree_static_hold                                   = 2       
  weighted_90_degree_static_hold                           = 3       
  bear_crawl                                               = 4       
  weighted_bear_crawl                                      = 5       
  cross_body_mountain_climber                              = 6       
  weighted_cross_body_mountain_climber                     = 7       
  elbow_plank_pike_jacks                                   = 8       
  weighted_elbow_plank_pike_jacks                          = 9       
  elevated_feet_plank                                      = 10      
  weighted_elevated_feet_plank                             = 11      
  elevator_abs                                             = 12      
  weighted_elevator_abs                                    = 13      
  extended_plank                                           = 14      
  weighted_extended_plank                                  = 15      
  full_plank_passe_twist                                   = 16      
  weighted_full_plank_passe_twist                          = 17      
  inching_elbow_plank                                      = 18      
  weighted_inching_elbow_plank                             = 19      
  inchworm_to_side_plank                                   = 20      
  weighted_inchworm_to_side_plank                          = 21      
  kneeling_plank                                           = 22      
  weighted_kneeling_plank                                  = 23      
  kneeling_side_plank_with_leg_lift                        = 24      
  weighted_kneeling_side_plank_with_leg_lift               = 25      
  lateral_roll                                             = 26      
  weighted_lateral_roll                                    = 27      
  lying_reverse_plank                                      = 28      
  weighted_lying_reverse_plank                             = 29      
  medicine_ball_mountain_climber                           = 30      
  weighted_medicine_ball_mountain_climber                  = 31      
  modified_mountain_climber_and_extension                  = 32      
  weighted_modified_mountain_climber_and_extension         = 33      
  mountain_climber                                         = 34      
  weighted_mountain_climber                                = 35      
  mountain_climber_on_sliding_discs                        = 36      
  weighted_mountain_climber_on_sliding_discs               = 37      
  mountain_climber_with_feet_on_bosu_ball                  = 38      
  weighted_mountain_climber_with_feet_on_bosu_ball         = 39      
  mountain_climber_with_hands_on_bench                     = 40      
  mountain_climber_with_hands_on_swiss_ball                = 41      
  weighted_mountain_climber_with_hands_on_swiss_ball       = 42      
  plank                                                    = 43      
  plank_jacks_with_feet_on_sliding_discs                   = 44      
  weighted_plank_jacks_with_feet_on_sliding_discs          = 45      
  plank_knee_twist                                         = 46      
  weighted_plank_knee_twist                                = 47      
  plank_pike_jumps                                         = 48      
  weighted_plank_pike_jumps                                = 49      
  plank_pikes                                              = 50      
  weighted_plank_pikes                                     = 51      
  plank_to_stand_up                                        = 52      
  weighted_plank_to_stand_up                               = 53      
  plank_with_arm_raise                                     = 54      
  weighted_plank_with_arm_raise                            = 55      
  plank_with_knee_to_elbow                                 = 56      
  weighted_plank_with_knee_to_elbow                        = 57      
  plank_with_oblique_crunch                                = 58      
  weighted_plank_with_oblique_crunch                       = 59      
  plyometric_side_plank                                    = 60      
  weighted_plyometric_side_plank                           = 61      
  rolling_side_plank                                       = 62      
  weighted_rolling_side_plank                              = 63      
  side_kick_plank                                          = 64      
  weighted_side_kick_plank                                 = 65      
  side_plank                                               = 66      
  weighted_side_plank                                      = 67      
  side_plank_and_row                                       = 68      
  weighted_side_plank_and_row                              = 69      
  side_plank_lift                                          = 70      
  weighted_side_plank_lift                                 = 71      
  side_plank_with_elbow_on_bosu_ball                       = 72      
  weighted_side_plank_with_elbow_on_bosu_ball              = 73      
  side_plank_with_feet_on_bench                            = 74      
  weighted_side_plank_with_feet_on_bench                   = 75      
  side_plank_with_knee_circle                              = 76      
  weighted_side_plank_with_knee_circle                     = 77      
  side_plank_with_knee_tuck                                = 78      
  weighted_side_plank_with_knee_tuck                       = 79      
  side_plank_with_leg_lift                                 = 80      
  weighted_side_plank_with_leg_lift                        = 81      
  side_plank_with_reach_under                              = 82      
  weighted_side_plank_with_reach_under                     = 83      
  single_leg_elevated_feet_plank                           = 84      
  weighted_single_leg_elevated_feet_plank                  = 85      
  single_leg_flex_and_extend                               = 86      
  weighted_single_leg_flex_and_extend                      = 87      
  single_leg_side_plank                                    = 88      
  weighted_single_leg_side_plank                           = 89      
  spiderman_plank                                          = 90      
  weighted_spiderman_plank                                 = 91      
  straight_arm_plank                                       = 92      
  weighted_straight_arm_plank                              = 93      
  straight_arm_plank_with_shoulder_touch                   = 94      
  weighted_straight_arm_plank_with_shoulder_touch          = 95      
  swiss_ball_plank                                         = 96      
  weighted_swiss_ball_plank                                = 97      
  swiss_ball_plank_leg_lift                                = 98      
  weighted_swiss_ball_plank_leg_lift                       = 99      
  swiss_ball_plank_leg_lift_and_hold                       = 100     
  swiss_ball_plank_with_feet_on_bench                      = 101     
  weighted_swiss_ball_plank_with_feet_on_bench             = 102     
  swiss_ball_prone_jackknife                               = 103     
  weighted_swiss_ball_prone_jackknife                      = 104     
  swiss_ball_side_plank                                    = 105     
  weighted_swiss_ball_side_plank                           = 106     
  three_way_plank                                          = 107     
  weighted_three_way_plank                                 = 108     
  towel_plank_and_knee_in                                  = 109     
  weighted_towel_plank_and_knee_in                         = 110     
  t_stabilization                                          = 111     
  weighted_t_stabilization                                 = 112     
  turkish_get_up_to_side_plank                             = 113     
  weighted_turkish_get_up_to_side_plank                    = 114     
  two_point_plank                                          = 115     
  weighted_two_point_plank                                 = 116     
  weighted_plank                                           = 117     
  wide_stance_plank_with_diagonal_arm_lift                 = 118     
  weighted_wide_stance_plank_with_diagonal_arm_lift        = 119     
  wide_stance_plank_with_diagonal_leg_lift                 = 120     
  weighted_wide_stance_plank_with_diagonal_leg_lift        = 121     
  wide_stance_plank_with_leg_lift                          = 122     
  weighted_wide_stance_plank_with_leg_lift                 = 123     
  wide_stance_plank_with_opposite_arm_and_leg_lift         = 124     
  weighted_mountain_climber_with_hands_on_bench            = 125     
  weighted_swiss_ball_plank_leg_lift_and_hold              = 126     
  weighted_wide_stance_plank_with_opposite_arm_and_leg_lift= 127     
  plank_with_feet_on_swiss_ball                            = 128     
  side_plank_to_plank_with_reach_under                     = 129     
  bridge_with_glute_lower_lift                             = 130     
  bridge_one_leg_bridge                                    = 131     
  plank_with_arm_variations                                = 132     
  plank_with_leg_lift                                      = 133     
  reverse_plank_with_leg_pull                              = 134     

  @staticmethod
  def basetype():
    return basetypes.uint16

class plyo_exercise_name(Enum):
  alternating_jump_lunge                                   = 0       
  weighted_alternating_jump_lunge                          = 1       
  barbell_jump_squat                                       = 2       
  body_weight_jump_squat                                   = 3       
  weighted_jump_squat                                      = 4       
  cross_knee_strike                                        = 5       
  weighted_cross_knee_strike                               = 6       
  depth_jump                                               = 7       
  weighted_depth_jump                                      = 8       
  dumbbell_jump_squat                                      = 9       
  dumbbell_split_jump                                      = 10      
  front_knee_strike                                        = 11      
  weighted_front_knee_strike                               = 12      
  high_box_jump                                            = 13      
  weighted_high_box_jump                                   = 14      
  isometric_explosive_body_weight_jump_squat               = 15      
  weighted_isometric_explosive_jump_squat                  = 16      
  lateral_leap_and_hop                                     = 17      
  weighted_lateral_leap_and_hop                            = 18      
  lateral_plyo_squats                                      = 19      
  weighted_lateral_plyo_squats                             = 20      
  lateral_slide                                            = 21      
  weighted_lateral_slide                                   = 22      
  medicine_ball_overhead_throws                            = 23      
  medicine_ball_side_throw                                 = 24      
  medicine_ball_slam                                       = 25      
  side_to_side_medicine_ball_throws                        = 26      
  side_to_side_shuffle_jump                                = 27      
  weighted_side_to_side_shuffle_jump                       = 28      
  squat_jump_onto_box                                      = 29      
  weighted_squat_jump_onto_box                             = 30      
  squat_jumps_in_and_out                                   = 31      
  weighted_squat_jumps_in_and_out                          = 32      

  @staticmethod
  def basetype():
    return basetypes.uint16

class pull_up_exercise_name(Enum):
  banded_pull_ups                                          = 0       
  _30_degree_lat_pulldown                                  = 1       
  band_assisted_chin_up                                    = 2       
  close_grip_chin_up                                       = 3       
  weighted_close_grip_chin_up                              = 4       
  close_grip_lat_pulldown                                  = 5       
  crossover_chin_up                                        = 6       
  weighted_crossover_chin_up                               = 7       
  ez_bar_pullover                                          = 8       
  hanging_hurdle                                           = 9       
  weighted_hanging_hurdle                                  = 10      
  kneeling_lat_pulldown                                    = 11      
  kneeling_underhand_grip_lat_pulldown                     = 12      
  lat_pulldown                                             = 13      
  mixed_grip_chin_up                                       = 14      
  weighted_mixed_grip_chin_up                              = 15      
  mixed_grip_pull_up                                       = 16      
  weighted_mixed_grip_pull_up                              = 17      
  reverse_grip_pulldown                                    = 18      
  standing_cable_pullover                                  = 19      
  straight_arm_pulldown                                    = 20      
  swiss_ball_ez_bar_pullover                               = 21      
  towel_pull_up                                            = 22      
  weighted_towel_pull_up                                   = 23      
  weighted_pull_up                                         = 24      
  wide_grip_lat_pulldown                                   = 25      
  wide_grip_pull_up                                        = 26      
  weighted_wide_grip_pull_up                               = 27      
  burpee_pull_up                                           = 28      
  weighted_burpee_pull_up                                  = 29      
  jumping_pull_ups                                         = 30      
  weighted_jumping_pull_ups                                = 31      
  kipping_pull_up                                          = 32      
  weighted_kipping_pull_up                                 = 33      
  l_pull_up                                                = 34      
  weighted_l_pull_up                                       = 35      
  suspended_chin_up                                        = 36      
  weighted_suspended_chin_up                               = 37      
  pull_up                                                  = 38      

  @staticmethod
  def basetype():
    return basetypes.uint16

class push_up_exercise_name(Enum):
  chest_press_with_band                                    = 0       
  alternating_staggered_push_up                            = 1       
  weighted_alternating_staggered_push_up                   = 2       
  alternating_hands_medicine_ball_push_up                  = 3       
  weighted_alternating_hands_medicine_ball_push_up         = 4       
  bosu_ball_push_up                                        = 5       
  weighted_bosu_ball_push_up                               = 6       
  clapping_push_up                                         = 7       
  weighted_clapping_push_up                                = 8       
  close_grip_medicine_ball_push_up                         = 9       
  weighted_close_grip_medicine_ball_push_up                = 10      
  close_hands_push_up                                      = 11      
  weighted_close_hands_push_up                             = 12      
  decline_push_up                                          = 13      
  weighted_decline_push_up                                 = 14      
  diamond_push_up                                          = 15      
  weighted_diamond_push_up                                 = 16      
  explosive_crossover_push_up                              = 17      
  weighted_explosive_crossover_push_up                     = 18      
  explosive_push_up                                        = 19      
  weighted_explosive_push_up                               = 20      
  feet_elevated_side_to_side_push_up                       = 21      
  weighted_feet_elevated_side_to_side_push_up              = 22      
  hand_release_push_up                                     = 23      
  weighted_hand_release_push_up                            = 24      
  handstand_push_up                                        = 25      
  weighted_handstand_push_up                               = 26      
  incline_push_up                                          = 27      
  weighted_incline_push_up                                 = 28      
  isometric_explosive_push_up                              = 29      
  weighted_isometric_explosive_push_up                     = 30      
  judo_push_up                                             = 31      
  weighted_judo_push_up                                    = 32      
  kneeling_push_up                                         = 33      
  weighted_kneeling_push_up                                = 34      
  medicine_ball_chest_pass                                 = 35      
  medicine_ball_push_up                                    = 36      
  weighted_medicine_ball_push_up                           = 37      
  one_arm_push_up                                          = 38      
  weighted_one_arm_push_up                                 = 39      
  weighted_push_up                                         = 40      
  push_up_and_row                                          = 41      
  weighted_push_up_and_row                                 = 42      
  push_up_plus                                             = 43      
  weighted_push_up_plus                                    = 44      
  push_up_with_feet_on_swiss_ball                          = 45      
  weighted_push_up_with_feet_on_swiss_ball                 = 46      
  push_up_with_one_hand_on_medicine_ball                   = 47      
  weighted_push_up_with_one_hand_on_medicine_ball          = 48      
  shoulder_push_up                                         = 49      
  weighted_shoulder_push_up                                = 50      
  single_arm_medicine_ball_push_up                         = 51      
  weighted_single_arm_medicine_ball_push_up                = 52      
  spiderman_push_up                                        = 53      
  weighted_spiderman_push_up                               = 54      
  stacked_feet_push_up                                     = 55      
  weighted_stacked_feet_push_up                            = 56      
  staggered_hands_push_up                                  = 57      
  weighted_staggered_hands_push_up                         = 58      
  suspended_push_up                                        = 59      
  weighted_suspended_push_up                               = 60      
  swiss_ball_push_up                                       = 61      
  weighted_swiss_ball_push_up                              = 62      
  swiss_ball_push_up_plus                                  = 63      
  weighted_swiss_ball_push_up_plus                         = 64      
  t_push_up                                                = 65      
  weighted_t_push_up                                       = 66      
  triple_stop_push_up                                      = 67      
  weighted_triple_stop_push_up                             = 68      
  wide_hands_push_up                                       = 69      
  weighted_wide_hands_push_up                              = 70      
  parallette_handstand_push_up                             = 71      
  weighted_parallette_handstand_push_up                    = 72      
  ring_handstand_push_up                                   = 73      
  weighted_ring_handstand_push_up                          = 74      
  ring_push_up                                             = 75      
  weighted_ring_push_up                                    = 76      
  push_up                                                  = 77      
  pilates_pushup                                           = 78      

  @staticmethod
  def basetype():
    return basetypes.uint16

class row_exercise_name(Enum):
  barbell_straight_leg_deadlift_to_row                     = 0       
  cable_row_standing                                       = 1       
  dumbbell_row                                             = 2       
  elevated_feet_inverted_row                               = 3       
  weighted_elevated_feet_inverted_row                      = 4       
  face_pull                                                = 5       
  face_pull_with_external_rotation                         = 6       
  inverted_row_with_feet_on_swiss_ball                     = 7       
  weighted_inverted_row_with_feet_on_swiss_ball            = 8       
  kettlebell_row                                           = 9       
  modified_inverted_row                                    = 10      
  weighted_modified_inverted_row                           = 11      
  neutral_grip_alternating_dumbbell_row                    = 12      
  one_arm_bent_over_row                                    = 13      
  one_legged_dumbbell_row                                  = 14      
  renegade_row                                             = 15      
  reverse_grip_barbell_row                                 = 16      
  rope_handle_cable_row                                    = 17      
  seated_cable_row                                         = 18      
  seated_dumbbell_row                                      = 19      
  single_arm_cable_row                                     = 20      
  single_arm_cable_row_and_rotation                        = 21      
  single_arm_inverted_row                                  = 22      
  weighted_single_arm_inverted_row                         = 23      
  single_arm_neutral_grip_dumbbell_row                     = 24      
  single_arm_neutral_grip_dumbbell_row_and_rotation        = 25      
  suspended_inverted_row                                   = 26      
  weighted_suspended_inverted_row                          = 27      
  t_bar_row                                                = 28      
  towel_grip_inverted_row                                  = 29      
  weighted_towel_grip_inverted_row                         = 30      
  underhand_grip_cable_row                                 = 31      
  v_grip_cable_row                                         = 32      
  wide_grip_seated_cable_row                               = 33      

  @staticmethod
  def basetype():
    return basetypes.uint16

class shoulder_press_exercise_name(Enum):
  alternating_dumbbell_shoulder_press                      = 0       
  arnold_press                                             = 1       
  barbell_front_squat_to_push_press                        = 2       
  barbell_push_press                                       = 3       
  barbell_shoulder_press                                   = 4       
  dead_curl_press                                          = 5       
  dumbbell_alternating_shoulder_press_and_twist            = 6       
  dumbbell_hammer_curl_to_lunge_to_press                   = 7       
  dumbbell_push_press                                      = 8       
  floor_inverted_shoulder_press                            = 9       
  weighted_floor_inverted_shoulder_press                   = 10      
  inverted_shoulder_press                                  = 11      
  weighted_inverted_shoulder_press                         = 12      
  one_arm_push_press                                       = 13      
  overhead_barbell_press                                   = 14      
  overhead_dumbbell_press                                  = 15      
  seated_barbell_shoulder_press                            = 16      
  seated_dumbbell_shoulder_press                           = 17      
  single_arm_dumbbell_shoulder_press                       = 18      
  single_arm_step_up_and_press                             = 19      
  smith_machine_overhead_press                             = 20      
  split_stance_hammer_curl_to_press                        = 21      
  swiss_ball_dumbbell_shoulder_press                       = 22      
  weight_plate_front_raise                                 = 23      

  @staticmethod
  def basetype():
    return basetypes.uint16

class shoulder_stability_exercise_name(Enum):
  _90_degree_cable_external_rotation                       = 0       
  band_external_rotation                                   = 1       
  band_internal_rotation                                   = 2       
  bent_arm_lateral_raise_and_external_rotation             = 3       
  cable_external_rotation                                  = 4       
  dumbbell_face_pull_with_external_rotation                = 5       
  floor_i_raise                                            = 6       
  weighted_floor_i_raise                                   = 7       
  floor_t_raise                                            = 8       
  weighted_floor_t_raise                                   = 9       
  floor_y_raise                                            = 10      
  weighted_floor_y_raise                                   = 11      
  incline_i_raise                                          = 12      
  weighted_incline_i_raise                                 = 13      
  incline_l_raise                                          = 14      
  weighted_incline_l_raise                                 = 15      
  incline_t_raise                                          = 16      
  weighted_incline_t_raise                                 = 17      
  incline_w_raise                                          = 18      
  weighted_incline_w_raise                                 = 19      
  incline_y_raise                                          = 20      
  weighted_incline_y_raise                                 = 21      
  lying_external_rotation                                  = 22      
  seated_dumbbell_external_rotation                        = 23      
  standing_l_raise                                         = 24      
  swiss_ball_i_raise                                       = 25      
  weighted_swiss_ball_i_raise                              = 26      
  swiss_ball_t_raise                                       = 27      
  weighted_swiss_ball_t_raise                              = 28      
  swiss_ball_w_raise                                       = 29      
  weighted_swiss_ball_w_raise                              = 30      
  swiss_ball_y_raise                                       = 31      
  weighted_swiss_ball_y_raise                              = 32      

  @staticmethod
  def basetype():
    return basetypes.uint16

class shrug_exercise_name(Enum):
  barbell_jump_shrug                                       = 0       
  barbell_shrug                                            = 1       
  barbell_upright_row                                      = 2       
  behind_the_back_smith_machine_shrug                      = 3       
  dumbbell_jump_shrug                                      = 4       
  dumbbell_shrug                                           = 5       
  dumbbell_upright_row                                     = 6       
  incline_dumbbell_shrug                                   = 7       
  overhead_barbell_shrug                                   = 8       
  overhead_dumbbell_shrug                                  = 9       
  scaption_and_shrug                                       = 10      
  scapular_retraction                                      = 11      
  serratus_chair_shrug                                     = 12      
  weighted_serratus_chair_shrug                            = 13      
  serratus_shrug                                           = 14      
  weighted_serratus_shrug                                  = 15      
  wide_grip_jump_shrug                                     = 16      

  @staticmethod
  def basetype():
    return basetypes.uint16

class sit_up_exercise_name(Enum):
  alternating_sit_up                                       = 0       
  weighted_alternating_sit_up                              = 1       
  bent_knee_v_up                                           = 2       
  weighted_bent_knee_v_up                                  = 3       
  butterfly_sit_up                                         = 4       
  weighted_butterfly_situp                                 = 5       
  cross_punch_roll_up                                      = 6       
  weighted_cross_punch_roll_up                             = 7       
  crossed_arms_sit_up                                      = 8       
  weighted_crossed_arms_sit_up                             = 9       
  get_up_sit_up                                            = 10      
  weighted_get_up_sit_up                                   = 11      
  hovering_sit_up                                          = 12      
  weighted_hovering_sit_up                                 = 13      
  kettlebell_sit_up                                        = 14      
  medicine_ball_alternating_v_up                           = 15      
  medicine_ball_sit_up                                     = 16      
  medicine_ball_v_up                                       = 17      
  modified_sit_up                                          = 18      
  negative_sit_up                                          = 19      
  one_arm_full_sit_up                                      = 20      
  reclining_circle                                         = 21      
  weighted_reclining_circle                                = 22      
  reverse_curl_up                                          = 23      
  weighted_reverse_curl_up                                 = 24      
  single_leg_swiss_ball_jackknife                          = 25      
  weighted_single_leg_swiss_ball_jackknife                 = 26      
  the_teaser                                               = 27      
  the_teaser_weighted                                      = 28      
  three_part_roll_down                                     = 29      
  weighted_three_part_roll_down                            = 30      
  v_up                                                     = 31      
  weighted_v_up                                            = 32      
  weighted_russian_twist_on_swiss_ball                     = 33      
  weighted_sit_up                                          = 34      
  x_abs                                                    = 35      
  weighted_x_abs                                           = 36      
  sit_up                                                   = 37      

  @staticmethod
  def basetype():
    return basetypes.uint16

class squat_exercise_name(Enum):
  leg_press                                                = 0       
  back_squat_with_body_bar                                 = 1       
  back_squats                                              = 2       
  weighted_back_squats                                     = 3       
  balancing_squat                                          = 4       
  weighted_balancing_squat                                 = 5       
  barbell_back_squat                                       = 6       
  barbell_box_squat                                        = 7       
  barbell_front_squat                                      = 8       
  barbell_hack_squat                                       = 9       
  barbell_hang_squat_snatch                                = 10      
  barbell_lateral_step_up                                  = 11      
  barbell_quarter_squat                                    = 12      
  barbell_siff_squat                                       = 13      
  barbell_squat_snatch                                     = 14      
  barbell_squat_with_heels_raised                          = 15      
  barbell_stepover                                         = 16      
  barbell_step_up                                          = 17      
  bench_squat_with_rotational_chop                         = 18      
  weighted_bench_squat_with_rotational_chop                = 19      
  body_weight_wall_squat                                   = 20      
  weighted_wall_squat                                      = 21      
  box_step_squat                                           = 22      
  weighted_box_step_squat                                  = 23      
  braced_squat                                             = 24      
  crossed_arm_barbell_front_squat                          = 25      
  crossover_dumbbell_step_up                               = 26      
  dumbbell_front_squat                                     = 27      
  dumbbell_split_squat                                     = 28      
  dumbbell_squat                                           = 29      
  dumbbell_squat_clean                                     = 30      
  dumbbell_stepover                                        = 31      
  dumbbell_step_up                                         = 32      
  elevated_single_leg_squat                                = 33      
  weighted_elevated_single_leg_squat                       = 34      
  figure_four_squats                                       = 35      
  weighted_figure_four_squats                              = 36      
  goblet_squat                                             = 37      
  kettlebell_squat                                         = 38      
  kettlebell_swing_overhead                                = 39      
  kettlebell_swing_with_flip_to_squat                      = 40      
  lateral_dumbbell_step_up                                 = 41      
  one_legged_squat                                         = 42      
  overhead_dumbbell_squat                                  = 43      
  overhead_squat                                           = 44      
  partial_single_leg_squat                                 = 45      
  weighted_partial_single_leg_squat                        = 46      
  pistol_squat                                             = 47      
  weighted_pistol_squat                                    = 48      
  plie_slides                                              = 49      
  weighted_plie_slides                                     = 50      
  plie_squat                                               = 51      
  weighted_plie_squat                                      = 52      
  prisoner_squat                                           = 53      
  weighted_prisoner_squat                                  = 54      
  single_leg_bench_get_up                                  = 55      
  weighted_single_leg_bench_get_up                         = 56      
  single_leg_bench_squat                                   = 57      
  weighted_single_leg_bench_squat                          = 58      
  single_leg_squat_on_swiss_ball                           = 59      
  weighted_single_leg_squat_on_swiss_ball                  = 60      
  squat                                                    = 61      
  weighted_squat                                           = 62      
  squats_with_band                                         = 63      
  staggered_squat                                          = 64      
  weighted_staggered_squat                                 = 65      
  step_up                                                  = 66      
  weighted_step_up                                         = 67      
  suitcase_squats                                          = 68      
  sumo_squat                                               = 69      
  sumo_squat_slide_in                                      = 70      
  weighted_sumo_squat_slide_in                             = 71      
  sumo_squat_to_high_pull                                  = 72      
  sumo_squat_to_stand                                      = 73      
  weighted_sumo_squat_to_stand                             = 74      
  sumo_squat_with_rotation                                 = 75      
  weighted_sumo_squat_with_rotation                        = 76      
  swiss_ball_body_weight_wall_squat                        = 77      
  weighted_swiss_ball_wall_squat                           = 78      
  thrusters                                                = 79      
  uneven_squat                                             = 80      
  weighted_uneven_squat                                    = 81      
  waist_slimming_squat                                     = 82      
  wall_ball                                                = 83      
  wide_stance_barbell_squat                                = 84      
  wide_stance_goblet_squat                                 = 85      
  zercher_squat                                            = 86      
  kbs_overhead                                             = 87      
  squat_and_side_kick                                      = 88      
  squat_jumps_in_n_out                                     = 89      
  pilates_plie_squats_parallel_turned_out_flat_and_heels   = 90      
  releve_straight_leg_and_knee_bent_with_one_leg_variation = 91      

  @staticmethod
  def basetype():
    return basetypes.uint16

class total_body_exercise_name(Enum):
  burpee                                                   = 0       
  weighted_burpee                                          = 1       
  burpee_box_jump                                          = 2       
  weighted_burpee_box_jump                                 = 3       
  high_pull_burpee                                         = 4       
  man_makers                                               = 5       
  one_arm_burpee                                           = 6       
  squat_thrusts                                            = 7       
  weighted_squat_thrusts                                   = 8       
  squat_plank_push_up                                      = 9       
  weighted_squat_plank_push_up                             = 10      
  standing_t_rotation_balance                              = 11      
  weighted_standing_t_rotation_balance                     = 12      

  @staticmethod
  def basetype():
    return basetypes.uint16

class triceps_extension_exercise_name(Enum):
  bench_dip                                                = 0       
  weighted_bench_dip                                       = 1       
  body_weight_dip                                          = 2       
  cable_kickback                                           = 3       
  cable_lying_triceps_extension                            = 4       
  cable_overhead_triceps_extension                         = 5       
  dumbbell_kickback                                        = 6       
  dumbbell_lying_triceps_extension                         = 7       
  ez_bar_overhead_triceps_extension                        = 8       
  incline_dip                                              = 9       
  weighted_incline_dip                                     = 10      
  incline_ez_bar_lying_triceps_extension                   = 11      
  lying_dumbbell_pullover_to_extension                     = 12      
  lying_ez_bar_triceps_extension                           = 13      
  lying_triceps_extension_to_close_grip_bench_press        = 14      
  overhead_dumbbell_triceps_extension                      = 15      
  reclining_triceps_press                                  = 16      
  reverse_grip_pressdown                                   = 17      
  reverse_grip_triceps_pressdown                           = 18      
  rope_pressdown                                           = 19      
  seated_barbell_overhead_triceps_extension                = 20      
  seated_dumbbell_overhead_triceps_extension               = 21      
  seated_ez_bar_overhead_triceps_extension                 = 22      
  seated_single_arm_overhead_dumbbell_extension            = 23      
  single_arm_dumbbell_overhead_triceps_extension           = 24      
  single_dumbbell_seated_overhead_triceps_extension        = 25      
  single_leg_bench_dip_and_kick                            = 26      
  weighted_single_leg_bench_dip_and_kick                   = 27      
  single_leg_dip                                           = 28      
  weighted_single_leg_dip                                  = 29      
  static_lying_triceps_extension                           = 30      
  suspended_dip                                            = 31      
  weighted_suspended_dip                                   = 32      
  swiss_ball_dumbbell_lying_triceps_extension              = 33      
  swiss_ball_ez_bar_lying_triceps_extension                = 34      
  swiss_ball_ez_bar_overhead_triceps_extension             = 35      
  tabletop_dip                                             = 36      
  weighted_tabletop_dip                                    = 37      
  triceps_extension_on_floor                               = 38      
  triceps_pressdown                                        = 39      
  weighted_dip                                             = 40      

  @staticmethod
  def basetype():
    return basetypes.uint16

class warm_up_exercise_name(Enum):
  quadruped_rocking                                        = 0       
  neck_tilts                                               = 1       
  ankle_circles                                            = 2       
  ankle_dorsiflexion_with_band                             = 3       
  ankle_internal_rotation                                  = 4       
  arm_circles                                              = 5       
  bent_over_reach_to_sky                                   = 6       
  cat_camel                                                = 7       
  elbow_to_foot_lunge                                      = 8       
  forward_and_backward_leg_swings                          = 9       
  groiners                                                 = 10      
  inverted_hamstring_stretch                               = 11      
  lateral_duck_under                                       = 12      
  neck_rotations                                           = 13      
  opposite_arm_and_leg_balance                             = 14      
  reach_roll_and_lift                                      = 15      
  scorpion                                                 = 16      
  shoulder_circles                                         = 17      
  side_to_side_leg_swings                                  = 18      
  sleeper_stretch                                          = 19      
  slide_out                                                = 20      
  swiss_ball_hip_crossover                                 = 21      
  swiss_ball_reach_roll_and_lift                           = 22      
  swiss_ball_windshield_wipers                             = 23      
  thoracic_rotation                                        = 24      
  walking_high_kicks                                       = 25      
  walking_high_knees                                       = 26      
  walking_knee_hugs                                        = 27      
  walking_leg_cradles                                      = 28      
  walkout                                                  = 29      
  walkout_from_push_up_position                            = 30      

  @staticmethod
  def basetype():
    return basetypes.uint16

class run_exercise_name(Enum):
  run                                                      = 0       
  walk                                                     = 1       
  jog                                                      = 2       
  sprint                                                   = 3       

  @staticmethod
  def basetype():
    return basetypes.uint16

class water_type(Enum):
  fresh                                                    = 0       
  salt                                                     = 1       
  en13319                                                  = 2       
  custom                                                   = 3       

  @staticmethod
  def basetype():
    return basetypes.enum

class tissue_model_type(Enum):
  zhl_16c                                                  = 0       # Buhlmann's decompression algorithm, version C

  @staticmethod
  def basetype():
    return basetypes.enum

class dive_gas_status(Enum):
  disabled                                                 = 0       
  enabled                                                  = 1       
  backup_only                                              = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class dive_alarm_type(Enum):
  depth                                                    = 0       
  time                                                     = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class dive_backlight_mode(Enum):
  at_depth                                                 = 0       
  always_on                                                = 1       

  @staticmethod
  def basetype():
    return basetypes.enum

class favero_product(Enum):
  assioma_uno                                              = 10      
  assioma_duo                                              = 12      

  @staticmethod
  def basetype():
    return basetypes.uint16

class climb_pro_event(Enum):
  approach                                                 = 0       
  start                                                    = 1       
  complete                                                 = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class tap_sensitivity(Enum):
  high                                                     = 0       
  medium                                                   = 1       
  low                                                      = 2       

  @staticmethod
  def basetype():
    return basetypes.enum

class radar_threat_level_type(Enum):
  threat_unknown                                           = 0       
  threat_none                                              = 1       
  threat_approaching                                       = 2       
  threat_approaching_fast                                  = 3       

  @staticmethod
  def basetype():
    return basetypes.enum
