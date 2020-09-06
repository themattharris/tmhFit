### THIS FILE IS AUTO-GENERATED ###
# Garmin FIT message types from profile.xslx in the SDK
# Version: FitSDKRelease_21.32.00
import basetypes
import profile
import sys
from enum import Enum, unique

def by_name(name):
  return sys.modules[__name__].__getattribute__(name)

@unique
class file_id(Enum):
  # Must be first message in file.
  type                                   = 0       
  manufacturer                           = 1       
  product                                = 2       
  serial_number                          = 3       
  time_created                           = 4       # Only set for files that are can be created/erased.
  number                                 = 5       # Only set for files that are not created/erased.
  product_name                           = 8       # Optional free form string to indicate the devices name or model

@unique
class file_creator(Enum):
  software_version                       = 0       
  hardware_version                       = 1       

@unique
class timestamp_correlation(Enum):
  timestamp                              = 253     # Whole second part of UTC timestamp at the time the system timestamp was recorded.
  fractional_timestamp                   = 0       # Fractional part of the UTC timestamp at the time the system timestamp was recorded.
  system_timestamp                       = 1       # Whole second part of the system timestamp
  fractional_system_timestamp            = 2       # Fractional part of the system timestamp
  local_timestamp                        = 3       # timestamp epoch expressed in local time used to convert timestamps to local time
  timestamp_ms                           = 4       # Millisecond part of the UTC timestamp at the time the system timestamp was recorded.
  system_timestamp_ms                    = 5       # Millisecond part of the system timestamp

@unique
class software(Enum):
  message_index                          = 254     
  version                                = 3       
  part_number                            = 5       

@unique
class slave_device(Enum):
  manufacturer                           = 0       
  product                                = 1       

@unique
class capabilities(Enum):
  languages                              = 0       # Use language_bits_x types where x is index of array.
  sports                                 = 1       # Use sport_bits_x types where x is index of array.
  workouts_supported                     = 21      
  connectivity_supported                 = 23      

@unique
class file_capabilities(Enum):
  message_index                          = 254     
  type                                   = 0       
  flags                                  = 1       
  directory                              = 2       
  max_count                              = 3       
  max_size                               = 4       

@unique
class mesg_capabilities(Enum):
  message_index                          = 254     
  file                                   = 0       
  mesg_num                               = 1       
  count_type                             = 2       
  count                                  = 3       

@unique
class field_capabilities(Enum):
  message_index                          = 254     
  file                                   = 0       
  mesg_num                               = 1       
  field_num                              = 2       
  count                                  = 3       

@unique
class device_settings(Enum):
  active_time_zone                       = 0       # Index into time zone arrays.
  utc_offset                             = 1       # Offset from system time. Required to convert timestamp from system time to UTC.
  time_offset                            = 2       # Offset from system time.
  time_mode                              = 4       # Display mode for the time
  time_zone_offset                       = 5       # timezone offset in 1/4 hour increments
  backlight_mode                         = 12      # Mode for backlight
  activity_tracker_enabled               = 36      # Enabled state of the activity tracker functionality
  clock_time                             = 39      # UTC timestamp used to set the devices clock and date
  pages_enabled                          = 40      # Bitfield  to configure enabled screens for each supported loop
  move_alert_enabled                     = 46      # Enabled state of the move alert
  date_mode                              = 47      # Display mode for the date
  display_orientation                    = 55      
  mounting_side                          = 56      
  default_page                           = 57      # Bitfield to indicate one page as default for each supported loop
  autosync_min_steps                     = 58      # Minimum steps before an autosync can occur
  autosync_min_time                      = 59      # Minimum minutes before an autosync can occur
  lactate_threshold_autodetect_enabled   = 80      # Enable auto-detect setting for the lactate threshold feature.
  ble_auto_upload_enabled                = 86      # Automatically upload using BLE
  auto_sync_frequency                    = 89      # Helps to conserve battery by changing modes
  auto_activity_detect                   = 90      # Allows setting specific activities auto-activity detect enabled/disabled settings
  number_of_screens                      = 94      # Number of screens configured to display
  smart_notification_display_orientation = 95      # Smart Notification display orientation
  tap_interface                          = 134     
  tap_sensitivity                        = 174     # Used to hold the tap threshold setting

@unique
class user_profile(Enum):
  message_index                          = 254     
  friendly_name                          = 0       
  gender                                 = 1       
  age                                    = 2       
  height                                 = 3       
  weight                                 = 4       
  language                               = 5       
  elev_setting                           = 6       
  weight_setting                         = 7       
  resting_heart_rate                     = 8       
  default_max_running_heart_rate         = 9       
  default_max_biking_heart_rate          = 10      
  default_max_heart_rate                 = 11      
  hr_setting                             = 12      
  speed_setting                          = 13      
  dist_setting                           = 14      
  power_setting                          = 16      
  activity_class                         = 17      
  position_setting                       = 18      
  temperature_setting                    = 21      
  local_id                               = 22      
  global_id                              = 23      
  wake_time                              = 28      # Typical wake time
  sleep_time                             = 29      # Typical bed time
  height_setting                         = 30      
  user_running_step_length               = 31      # User defined running step length set to 0 for auto length
  user_walking_step_length               = 32      # User defined walking step length set to 0 for auto length
  depth_setting                          = 47      
  dive_count                             = 49      

@unique
class hrm_profile(Enum):
  message_index                          = 254     
  enabled                                = 0       
  hrm_ant_id                             = 1       
  log_hrv                                = 2       
  hrm_ant_id_trans_type                  = 3       

@unique
class sdm_profile(Enum):
  message_index                          = 254     
  enabled                                = 0       
  sdm_ant_id                             = 1       
  sdm_cal_factor                         = 2       
  odometer                               = 3       
  speed_source                           = 4       # Use footpod for speed source instead of GPS
  sdm_ant_id_trans_type                  = 5       
  odometer_rollover                      = 7       # Rollover counter that can be used to extend the odometer

@unique
class bike_profile(Enum):
  message_index                          = 254     
  name                                   = 0       
  sport                                  = 1       
  sub_sport                              = 2       
  odometer                               = 3       
  bike_spd_ant_id                        = 4       
  bike_cad_ant_id                        = 5       
  bike_spdcad_ant_id                     = 6       
  bike_power_ant_id                      = 7       
  custom_wheelsize                       = 8       
  auto_wheelsize                         = 9       
  bike_weight                            = 10      
  power_cal_factor                       = 11      
  auto_wheel_cal                         = 12      
  auto_power_zero                        = 13      
  id                                     = 14      
  spd_enabled                            = 15      
  cad_enabled                            = 16      
  spdcad_enabled                         = 17      
  power_enabled                          = 18      
  crank_length                           = 19      
  enabled                                = 20      
  bike_spd_ant_id_trans_type             = 21      
  bike_cad_ant_id_trans_type             = 22      
  bike_spdcad_ant_id_trans_type          = 23      
  bike_power_ant_id_trans_type           = 24      
  odometer_rollover                      = 37      # Rollover counter that can be used to extend the odometer
  front_gear_num                         = 38      # Number of front gears
  front_gear                             = 39      # Number of teeth on each gear 0 is innermost
  rear_gear_num                          = 40      # Number of rear gears
  rear_gear                              = 41      # Number of teeth on each gear 0 is innermost
  shimano_di2_enabled                    = 44      

@unique
class connectivity(Enum):
  bluetooth_enabled                      = 0       # Use Bluetooth for connectivity features
  bluetooth_le_enabled                   = 1       # Use Bluetooth Low Energy for connectivity features
  ant_enabled                            = 2       # Use ANT for connectivity features
  name                                   = 3       
  live_tracking_enabled                  = 4       
  weather_conditions_enabled             = 5       
  weather_alerts_enabled                 = 6       
  auto_activity_upload_enabled           = 7       
  course_download_enabled                = 8       
  workout_download_enabled               = 9       
  gps_ephemeris_download_enabled         = 10      
  incident_detection_enabled             = 11      
  grouptrack_enabled                     = 12      

@unique
class watchface_settings(Enum):
  message_index                          = 254     
  mode                                   = 0       
  layout                                 = 1       

@unique
class ohr_settings(Enum):
  timestamp                              = 253     
  enabled                                = 0       

@unique
class zones_target(Enum):
  max_heart_rate                         = 1       
  threshold_heart_rate                   = 2       
  functional_threshold_power             = 3       
  hr_calc_type                           = 5       
  pwr_calc_type                          = 7       

@unique
class sport(Enum):
  sport                                  = 0       
  sub_sport                              = 1       
  name                                   = 3       

@unique
class hr_zone(Enum):
  message_index                          = 254     
  high_bpm                               = 1       
  name                                   = 2       

@unique
class speed_zone(Enum):
  message_index                          = 254     
  high_value                             = 0       
  name                                   = 1       

@unique
class cadence_zone(Enum):
  message_index                          = 254     
  high_value                             = 0       
  name                                   = 1       

@unique
class power_zone(Enum):
  message_index                          = 254     
  high_value                             = 1       
  name                                   = 2       

@unique
class met_zone(Enum):
  message_index                          = 254     
  high_bpm                               = 1       
  calories                               = 2       
  fat_calories                           = 3       

@unique
class dive_settings(Enum):
  message_index                          = 254     
  name                                   = 0       
  model                                  = 1       
  gf_low                                 = 2       
  gf_high                                = 3       
  water_type                             = 4       
  water_density                          = 5       # Fresh water is usually 1000; salt water is usually 1025
  po2_warn                               = 6       # Typically 1.40
  po2_critical                           = 7       # Typically 1.60
  po2_deco                               = 8       
  safety_stop_enabled                    = 9       
  bottom_depth                           = 10      
  bottom_time                            = 11      
  apnea_countdown_enabled                = 12      
  apnea_countdown_time                   = 13      
  backlight_mode                         = 14      
  backlight_brightness                   = 15      
  backlight_timeout                      = 16      
  repeat_dive_interval                   = 17      # Time between surfacing and ending the activity
  safety_stop_time                       = 18      # Time at safety stop (if enabled)
  heart_rate_source_type                 = 19      
  heart_rate_source                      = 20      

@unique
class dive_alarm(Enum):
  message_index                          = 254     # Index of the alarm
  depth                                  = 0       
  time                                   = 1       
  enabled                                = 2       
  alarm_type                             = 3       
  sound                                  = 4       
  dive_types                             = 5       

@unique
class dive_gas(Enum):
  message_index                          = 254     
  helium_content                         = 0       
  oxygen_content                         = 1       
  status                                 = 2       

@unique
class goal(Enum):
  message_index                          = 254     
  sport                                  = 0       
  sub_sport                              = 1       
  start_date                             = 2       
  end_date                               = 3       
  type                                   = 4       
  value                                  = 5       
  repeat                                 = 6       
  target_value                           = 7       
  recurrence                             = 8       
  recurrence_value                       = 9       
  enabled                                = 10      
  source                                 = 11      

@unique
class activity(Enum):
  timestamp                              = 253     
  total_timer_time                       = 0       # Exclude pauses
  num_sessions                           = 1       
  type                                   = 2       
  event                                  = 3       
  event_type                             = 4       
  local_timestamp                        = 5       # timestamp epoch expressed in local time, used to convert activity timestamps to local time 
  event_group                            = 6       

@unique
class session(Enum):
  message_index                          = 254     # Selected bit is set for the current session.
  timestamp                              = 253     # Sesson end time.
  event                                  = 0       # session
  event_type                             = 1       # stop
  start_time                             = 2       
  start_position_lat                     = 3       
  start_position_long                    = 4       
  sport                                  = 5       
  sub_sport                              = 6       
  total_elapsed_time                     = 7       # Time (includes pauses)
  total_timer_time                       = 8       # Timer Time (excludes pauses)
  total_distance                         = 9       
  total_cycles                           = 10      
  total_calories                         = 11      
  total_fat_calories                     = 13      
  avg_speed                              = 14      # total_distance / total_timer_time
  max_speed                              = 15      
  avg_heart_rate                         = 16      # average heart rate (excludes pause time)
  max_heart_rate                         = 17      
  avg_cadence                            = 18      # total_cycles / total_timer_time if non_zero_avg_cadence otherwise total_cycles / total_elapsed_time
  max_cadence                            = 19      
  avg_power                              = 20      # total_power / total_timer_time if non_zero_avg_power otherwise total_power / total_elapsed_time
  max_power                              = 21      
  total_ascent                           = 22      
  total_descent                          = 23      
  total_training_effect                  = 24      
  first_lap_index                        = 25      
  num_laps                               = 26      
  event_group                            = 27      
  trigger                                = 28      
  nec_lat                                = 29      # North east corner latitude
  nec_long                               = 30      # North east corner longitude
  swc_lat                                = 31      # South west corner latitude
  swc_long                               = 32      # South west corner longitude
  normalized_power                       = 34      
  training_stress_score                  = 35      
  intensity_factor                       = 36      
  left_right_balance                     = 37      
  avg_stroke_count                       = 41      
  avg_stroke_distance                    = 42      
  swim_stroke                            = 43      
  pool_length                            = 44      
  threshold_power                        = 45      
  pool_length_unit                       = 46      
  num_active_lengths                     = 47      # # of active lengths of swim pool
  total_work                             = 48      
  avg_altitude                           = 49      
  max_altitude                           = 50      
  gps_accuracy                           = 51      
  avg_grade                              = 52      
  avg_pos_grade                          = 53      
  avg_neg_grade                          = 54      
  max_pos_grade                          = 55      
  max_neg_grade                          = 56      
  avg_temperature                        = 57      
  max_temperature                        = 58      
  total_moving_time                      = 59      
  avg_pos_vertical_speed                 = 60      
  avg_neg_vertical_speed                 = 61      
  max_pos_vertical_speed                 = 62      
  max_neg_vertical_speed                 = 63      
  min_heart_rate                         = 64      
  time_in_hr_zone                        = 65      
  time_in_speed_zone                     = 66      
  time_in_cadence_zone                   = 67      
  time_in_power_zone                     = 68      
  avg_lap_time                           = 69      
  best_lap_index                         = 70      
  min_altitude                           = 71      
  player_score                           = 82      
  opponent_score                         = 83      
  opponent_name                          = 84      
  stroke_count                           = 85      # stroke_type enum used as the index
  zone_count                             = 86      # zone number used as the index
  max_ball_speed                         = 87      
  avg_ball_speed                         = 88      
  avg_vertical_oscillation               = 89      
  avg_stance_time_percent                = 90      
  avg_stance_time                        = 91      
  avg_fractional_cadence                 = 92      # fractional part of the avg_cadence
  max_fractional_cadence                 = 93      # fractional part of the max_cadence
  total_fractional_cycles                = 94      # fractional part of the total_cycles
  avg_total_hemoglobin_conc              = 95      # Avg saturated and unsaturated hemoglobin
  min_total_hemoglobin_conc              = 96      # Min saturated and unsaturated hemoglobin
  max_total_hemoglobin_conc              = 97      # Max saturated and unsaturated hemoglobin
  avg_saturated_hemoglobin_percent       = 98      # Avg percentage of hemoglobin saturated with oxygen
  min_saturated_hemoglobin_percent       = 99      # Min percentage of hemoglobin saturated with oxygen
  max_saturated_hemoglobin_percent       = 100     # Max percentage of hemoglobin saturated with oxygen
  avg_left_torque_effectiveness          = 101     
  avg_right_torque_effectiveness         = 102     
  avg_left_pedal_smoothness              = 103     
  avg_right_pedal_smoothness             = 104     
  avg_combined_pedal_smoothness          = 105     
  sport_index                            = 111     
  time_standing                          = 112     # Total time spend in the standing position
  stand_count                            = 113     # Number of transitions to the standing state
  avg_left_pco                           = 114     # Average platform center offset Left
  avg_right_pco                          = 115     # Average platform center offset Right
  avg_left_power_phase                   = 116     # Average left power phase angles. Indexes defined by power_phase_type.
  avg_left_power_phase_peak              = 117     # Average left power phase peak angles. Data value indexes defined by power_phase_type.
  avg_right_power_phase                  = 118     # Average right power phase angles. Data value indexes defined by power_phase_type.
  avg_right_power_phase_peak             = 119     # Average right power phase peak angles data value indexes  defined by power_phase_type.
  avg_power_position                     = 120     # Average power by position. Data value indexes defined by rider_position_type.
  max_power_position                     = 121     # Maximum power by position. Data value indexes defined by rider_position_type.
  avg_cadence_position                   = 122     # Average cadence by position. Data value indexes defined by rider_position_type.
  max_cadence_position                   = 123     # Maximum cadence by position. Data value indexes defined by rider_position_type.
  enhanced_avg_speed                     = 124     # total_distance / total_timer_time
  enhanced_max_speed                     = 125     
  enhanced_avg_altitude                  = 126     
  enhanced_min_altitude                  = 127     
  enhanced_max_altitude                  = 128     
  avg_lev_motor_power                    = 129     # lev average motor power during session
  max_lev_motor_power                    = 130     # lev maximum motor power during session
  lev_battery_consumption                = 131     # lev battery consumption during session
  avg_vertical_ratio                     = 132     
  avg_stance_time_balance                = 133     
  avg_step_length                        = 134     
  total_anaerobic_training_effect        = 137     
  avg_vam                                = 139     
  total_grit                             = 181     # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  total_flow                             = 182     # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.
  jump_count                             = 183     
  avg_grit                               = 186     # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  avg_flow                               = 187     # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.

@unique
class lap(Enum):
  message_index                          = 254     
  timestamp                              = 253     # Lap end time.
  event                                  = 0       
  event_type                             = 1       
  start_time                             = 2       
  start_position_lat                     = 3       
  start_position_long                    = 4       
  end_position_lat                       = 5       
  end_position_long                      = 6       
  total_elapsed_time                     = 7       # Time (includes pauses)
  total_timer_time                       = 8       # Timer Time (excludes pauses)
  total_distance                         = 9       
  total_cycles                           = 10      
  total_calories                         = 11      
  total_fat_calories                     = 12      # If New Leaf
  avg_speed                              = 13      
  max_speed                              = 14      
  avg_heart_rate                         = 15      
  max_heart_rate                         = 16      
  avg_cadence                            = 17      # total_cycles / total_timer_time if non_zero_avg_cadence otherwise total_cycles / total_elapsed_time
  max_cadence                            = 18      
  avg_power                              = 19      # total_power / total_timer_time if non_zero_avg_power otherwise total_power / total_elapsed_time
  max_power                              = 20      
  total_ascent                           = 21      
  total_descent                          = 22      
  intensity                              = 23      
  lap_trigger                            = 24      
  sport                                  = 25      
  event_group                            = 26      
  num_lengths                            = 32      # # of lengths of swim pool
  normalized_power                       = 33      
  left_right_balance                     = 34      
  first_length_index                     = 35      
  avg_stroke_distance                    = 37      
  swim_stroke                            = 38      
  sub_sport                              = 39      
  num_active_lengths                     = 40      # # of active lengths of swim pool
  total_work                             = 41      
  avg_altitude                           = 42      
  max_altitude                           = 43      
  gps_accuracy                           = 44      
  avg_grade                              = 45      
  avg_pos_grade                          = 46      
  avg_neg_grade                          = 47      
  max_pos_grade                          = 48      
  max_neg_grade                          = 49      
  avg_temperature                        = 50      
  max_temperature                        = 51      
  total_moving_time                      = 52      
  avg_pos_vertical_speed                 = 53      
  avg_neg_vertical_speed                 = 54      
  max_pos_vertical_speed                 = 55      
  max_neg_vertical_speed                 = 56      
  time_in_hr_zone                        = 57      
  time_in_speed_zone                     = 58      
  time_in_cadence_zone                   = 59      
  time_in_power_zone                     = 60      
  repetition_num                         = 61      
  min_altitude                           = 62      
  min_heart_rate                         = 63      
  wkt_step_index                         = 71      
  opponent_score                         = 74      
  stroke_count                           = 75      # stroke_type enum used as the index
  zone_count                             = 76      # zone number used as the index
  avg_vertical_oscillation               = 77      
  avg_stance_time_percent                = 78      
  avg_stance_time                        = 79      
  avg_fractional_cadence                 = 80      # fractional part of the avg_cadence
  max_fractional_cadence                 = 81      # fractional part of the max_cadence
  total_fractional_cycles                = 82      # fractional part of the total_cycles
  player_score                           = 83      
  avg_total_hemoglobin_conc              = 84      # Avg saturated and unsaturated hemoglobin
  min_total_hemoglobin_conc              = 85      # Min saturated and unsaturated hemoglobin
  max_total_hemoglobin_conc              = 86      # Max saturated and unsaturated hemoglobin
  avg_saturated_hemoglobin_percent       = 87      # Avg percentage of hemoglobin saturated with oxygen
  min_saturated_hemoglobin_percent       = 88      # Min percentage of hemoglobin saturated with oxygen
  max_saturated_hemoglobin_percent       = 89      # Max percentage of hemoglobin saturated with oxygen
  avg_left_torque_effectiveness          = 91      
  avg_right_torque_effectiveness         = 92      
  avg_left_pedal_smoothness              = 93      
  avg_right_pedal_smoothness             = 94      
  avg_combined_pedal_smoothness          = 95      
  time_standing                          = 98      # Total time spent in the standing position
  stand_count                            = 99      # Number of transitions to the standing state
  avg_left_pco                           = 100     # Average left platform center offset
  avg_right_pco                          = 101     # Average right platform center offset
  avg_left_power_phase                   = 102     # Average left power phase angles. Data value indexes defined by power_phase_type.
  avg_left_power_phase_peak              = 103     # Average left power phase peak angles. Data value indexes  defined by power_phase_type.
  avg_right_power_phase                  = 104     # Average right power phase angles. Data value indexes defined by power_phase_type.
  avg_right_power_phase_peak             = 105     # Average right power phase peak angles. Data value indexes  defined by power_phase_type.
  avg_power_position                     = 106     # Average power by position. Data value indexes defined by rider_position_type.
  max_power_position                     = 107     # Maximum power by position. Data value indexes defined by rider_position_type.
  avg_cadence_position                   = 108     # Average cadence by position. Data value indexes defined by rider_position_type.
  max_cadence_position                   = 109     # Maximum cadence by position. Data value indexes defined by rider_position_type.
  enhanced_avg_speed                     = 110     
  enhanced_max_speed                     = 111     
  enhanced_avg_altitude                  = 112     
  enhanced_min_altitude                  = 113     
  enhanced_max_altitude                  = 114     
  avg_lev_motor_power                    = 115     # lev average motor power during lap
  max_lev_motor_power                    = 116     # lev maximum motor power during lap
  lev_battery_consumption                = 117     # lev battery consumption during lap
  avg_vertical_ratio                     = 118     
  avg_stance_time_balance                = 119     
  avg_step_length                        = 120     
  avg_vam                                = 121     
  total_grit                             = 149     # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  total_flow                             = 150     # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.
  jump_count                             = 151     
  avg_grit                               = 153     # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  avg_flow                               = 154     # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.

@unique
class length(Enum):
  message_index                          = 254     
  timestamp                              = 253     
  event                                  = 0       
  event_type                             = 1       
  start_time                             = 2       
  total_elapsed_time                     = 3       
  total_timer_time                       = 4       
  total_strokes                          = 5       
  avg_speed                              = 6       
  swim_stroke                            = 7       
  avg_swimming_cadence                   = 9       
  event_group                            = 10      
  total_calories                         = 11      
  length_type                            = 12      
  player_score                           = 18      
  opponent_score                         = 19      
  stroke_count                           = 20      # stroke_type enum used as the index
  zone_count                             = 21      # zone number used as the index

@unique
class record(Enum):
  timestamp                              = 253     
  position_lat                           = 0       
  position_long                          = 1       
  altitude                               = 2       
  heart_rate                             = 3       
  cadence                                = 4       
  distance                               = 5       
  speed                                  = 6       
  power                                  = 7       
  compressed_speed_distance              = 8       
  grade                                  = 9       
  resistance                             = 10      # Relative. 0 is none  254 is Max.
  time_from_course                       = 11      
  cycle_length                           = 12      
  temperature                            = 13      
  speed_1s                               = 17      # Speed at 1s intervals.  Timestamp field indicates time of last array element.
  cycles                                 = 18      
  total_cycles                           = 19      
  compressed_accumulated_power           = 28      
  accumulated_power                      = 29      
  left_right_balance                     = 30      
  gps_accuracy                           = 31      
  vertical_speed                         = 32      
  calories                               = 33      
  vertical_oscillation                   = 39      
  stance_time_percent                    = 40      
  stance_time                            = 41      
  activity_type                          = 42      
  left_torque_effectiveness              = 43      
  right_torque_effectiveness             = 44      
  left_pedal_smoothness                  = 45      
  right_pedal_smoothness                 = 46      
  combined_pedal_smoothness              = 47      
  time128                                = 48      
  stroke_type                            = 49      
  zone                                   = 50      
  ball_speed                             = 51      
  cadence256                             = 52      # Log cadence and fractional cadence for backwards compatability
  fractional_cadence                     = 53      
  total_hemoglobin_conc                  = 54      # Total saturated and unsaturated hemoglobin
  total_hemoglobin_conc_min              = 55      # Min saturated and unsaturated hemoglobin
  total_hemoglobin_conc_max              = 56      # Max saturated and unsaturated hemoglobin
  saturated_hemoglobin_percent           = 57      # Percentage of hemoglobin saturated with oxygen
  saturated_hemoglobin_percent_min       = 58      # Min percentage of hemoglobin saturated with oxygen
  saturated_hemoglobin_percent_max       = 59      # Max percentage of hemoglobin saturated with oxygen
  device_index                           = 62      
  left_pco                               = 67      # Left platform center offset
  right_pco                              = 68      # Right platform center offset
  left_power_phase                       = 69      # Left power phase angles. Data value indexes defined by power_phase_type.
  left_power_phase_peak                  = 70      # Left power phase peak angles. Data value indexes defined by power_phase_type.
  right_power_phase                      = 71      # Right power phase angles. Data value indexes defined by power_phase_type.
  right_power_phase_peak                 = 72      # Right power phase peak angles. Data value indexes defined by power_phase_type.
  enhanced_speed                         = 73      
  enhanced_altitude                      = 78      
  battery_soc                            = 81      # lev battery state of charge
  motor_power                            = 82      # lev motor power
  vertical_ratio                         = 83      
  stance_time_balance                    = 84      
  step_length                            = 85      
  absolute_pressure                      = 91      # Includes atmospheric pressure
  depth                                  = 92      # 0 if above water
  next_stop_depth                        = 93      # 0 if above water
  next_stop_time                         = 94      
  time_to_surface                        = 95      
  ndl_time                               = 96      
  cns_load                               = 97      
  n2_load                                = 98      
  grit                                   = 114     # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  flow                                   = 115     # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.
  ebike_travel_range                     = 117     
  ebike_battery_level                    = 118     
  ebike_assist_mode                      = 119     
  ebike_assist_level_percent             = 120     

@unique
class event(Enum):
  timestamp                              = 253     
  event                                  = 0       
  event_type                             = 1       
  data16                                 = 2       
  data                                   = 3       
  event_group                            = 4       
  score                                  = 7       # Do not populate directly. Autogenerated by decoder for sport_point subfield components
  opponent_score                         = 8       # Do not populate directly. Autogenerated by decoder for sport_point subfield components
  front_gear_num                         = 9       # Do not populate directly. Autogenerated by decoder for gear_change subfield components.  Front gear number. 1 is innermost.
  front_gear                             = 10      # Do not populate directly. Autogenerated by decoder for gear_change subfield components.  Number of front teeth.
  rear_gear_num                          = 11      # Do not populate directly. Autogenerated by decoder for gear_change subfield components.  Rear gear number. 1 is innermost.
  rear_gear                              = 12      # Do not populate directly. Autogenerated by decoder for gear_change subfield components.  Number of rear teeth.
  device_index                           = 13      
  radar_threat_level_max                 = 21      # Do not populate directly. Autogenerated by decoder for threat_alert subfield components.
  radar_threat_count                     = 22      # Do not populate directly. Autogenerated by decoder for threat_alert subfield components.

@unique
class device_info(Enum):
  timestamp                              = 253     
  device_index                           = 0       
  device_type                            = 1       
  manufacturer                           = 2       
  serial_number                          = 3       
  product                                = 4       
  software_version                       = 5       
  hardware_version                       = 6       
  cum_operating_time                     = 7       # Reset by new battery or charge.
  battery_voltage                        = 10      
  battery_status                         = 11      
  sensor_position                        = 18      # Indicates the location of the sensor
  descriptor                             = 19      # Used to describe the sensor or location
  ant_transmission_type                  = 20      
  ant_device_number                      = 21      
  ant_network                            = 22      
  source_type                            = 25      
  product_name                           = 27      # Optional free form string to indicate the devices name or model

@unique
class training_file(Enum):
  # Corresponds to file_id of workout or course.
  timestamp                              = 253     
  type                                   = 0       
  manufacturer                           = 1       
  product                                = 2       
  serial_number                          = 3       
  time_created                           = 4       

@unique
class hrv(Enum):
  # Heart rate variability
  time                                   = 0       # Time between beats

@unique
class weather_conditions(Enum):
  timestamp                              = 253     # time of update for current conditions, else forecast time
  weather_report                         = 0       # Current or forecast
  temperature                            = 1       
  condition                              = 2       # Corresponds to GSC Response weatherIcon field
  wind_direction                         = 3       
  wind_speed                             = 4       
  precipitation_probability              = 5       # range 0-100
  temperature_feels_like                 = 6       # Heat Index if  GCS heatIdx above or equal to 90F or wind chill if GCS windChill below or equal to 32F
  relative_humidity                      = 7       
  location                               = 8       # string corresponding to GCS response location string
  observed_at_time                       = 9       
  observed_location_lat                  = 10      
  observed_location_long                 = 11      
  day_of_week                            = 12      
  high_temperature                       = 13      
  low_temperature                        = 14      

@unique
class weather_alert(Enum):
  timestamp                              = 253     
  report_id                              = 0       # Unique identifier from GCS report ID string, length is 12
  issue_time                             = 1       # Time alert was issued
  expire_time                            = 2       # Time alert expires
  severity                               = 3       # Warning, Watch, Advisory, Statement
  type                                   = 4       # Tornado, Severe Thunderstorm, etc.

@unique
class gps_metadata(Enum):
  timestamp                              = 253     # Whole second part of the timestamp.
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  position_lat                           = 1       
  position_long                          = 2       
  enhanced_altitude                      = 3       
  enhanced_speed                         = 4       
  heading                                = 5       
  utc_timestamp                          = 6       # Used to correlate UTC to system time if the timestamp of the message is in system time.  This UTC time is derived from the GPS data.
  velocity                               = 7       # velocity[0] is lon velocity.  Velocity[1] is lat velocity.  Velocity[2] is altitude velocity.

@unique
class camera_event(Enum):
  timestamp                              = 253     # Whole second part of the timestamp.
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  camera_event_type                      = 1       
  camera_file_uuid                       = 2       
  camera_orientation                     = 3       

@unique
class gyroscope_data(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  sample_time_offset                     = 1       # Each time in the array describes the time at which the gyro sample with the corrosponding index was taken. Limited to 30 samples in each message. The samples may span across seconds. Array size must match the number of samples in gyro_x and gyro_y and gyro_z
  gyro_x                                 = 2       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  gyro_y                                 = 3       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  gyro_z                                 = 4       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  calibrated_gyro_x                      = 5       # Calibrated gyro reading
  calibrated_gyro_y                      = 6       # Calibrated gyro reading
  calibrated_gyro_z                      = 7       # Calibrated gyro reading

@unique
class accelerometer_data(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  sample_time_offset                     = 1       # Each time in the array describes the time at which the accelerometer sample with the corrosponding index was taken. Limited to 30 samples in each message. The samples may span across seconds. Array size must match the number of samples in accel_x and accel_y and accel_z
  accel_x                                = 2       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  accel_y                                = 3       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  accel_z                                = 4       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  calibrated_accel_x                     = 5       # Calibrated accel reading
  calibrated_accel_y                     = 6       # Calibrated accel reading
  calibrated_accel_z                     = 7       # Calibrated accel reading
  compressed_calibrated_accel_x          = 8       # Calibrated accel reading
  compressed_calibrated_accel_y          = 9       # Calibrated accel reading
  compressed_calibrated_accel_z          = 10      # Calibrated accel reading

@unique
class magnetometer_data(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  sample_time_offset                     = 1       # Each time in the array describes the time at which the compass sample with the corrosponding index was taken. Limited to 30 samples in each message. The samples may span across seconds. Array size must match the number of samples in cmps_x and cmps_y and cmps_z
  mag_x                                  = 2       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  mag_y                                  = 3       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  mag_z                                  = 4       # These are the raw ADC reading. Maximum number of samples is 30 in each message. The samples may span across seconds. A conversion will need to be done on this data once read.
  calibrated_mag_x                       = 5       # Calibrated Magnetometer reading
  calibrated_mag_y                       = 6       # Calibrated Magnetometer reading
  calibrated_mag_z                       = 7       # Calibrated Magnetometer reading

@unique
class barometer_data(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  sample_time_offset                     = 1       # Each time in the array describes the time at which the barometer sample with the corrosponding index was taken. The samples may span across seconds. Array size must match the number of samples in baro_cal
  baro_pres                              = 2       # These are the raw ADC reading. The samples may span across seconds. A conversion will need to be done on this data once read.

@unique
class three_d_sensor_calibration(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  sensor_type                            = 0       # Indicates which sensor the calibration is for
  calibration_factor                     = 1       # Calibration factor used to convert from raw ADC value to degrees, g,  etc.
  calibration_divisor                    = 2       # Calibration factor divisor
  level_shift                            = 3       # Level shift value used to shift the ADC value back into range
  offset_cal                             = 4       # Internal calibration factors, one for each: xy, yx, zx
  orientation_matrix                     = 5       # 3 x 3 rotation matrix (row major)

@unique
class one_d_sensor_calibration(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  sensor_type                            = 0       # Indicates which sensor the calibration is for
  calibration_factor                     = 1       # Calibration factor used to convert from raw ADC value to degrees, g,  etc.
  calibration_divisor                    = 2       # Calibration factor divisor
  level_shift                            = 3       # Level shift value used to shift the ADC value back into range
  offset_cal                             = 4       # Internal Calibration factor

@unique
class video_frame(Enum):
  timestamp                              = 253     # Whole second part of the timestamp
  timestamp_ms                           = 0       # Millisecond part of the timestamp.
  frame_number                           = 1       # Number of the frame that the timestamp and timestamp_ms correlate to

@unique
class obdii_data(Enum):
  timestamp                              = 253     # Timestamp message was output
  timestamp_ms                           = 0       # Fractional part of timestamp, added to timestamp
  time_offset                            = 1       # Offset of PID reading [i] from start_timestamp+start_timestamp_ms. Readings may span accross seconds.
  pid                                    = 2       # Parameter ID
  raw_data                               = 3       # Raw parameter data
  pid_data_size                          = 4       # Optional, data size of PID[i].  If not specified refer to SAE J1979.
  system_time                            = 5       # System time associated with sample expressed in ms, can be used instead of time_offset.  There will be a system_time value for each raw_data element.  For multibyte pids the system_time is repeated.
  start_timestamp                        = 6       # Timestamp of first sample recorded in the message.  Used with time_offset to generate time of each sample
  start_timestamp_ms                     = 7       # Fractional part of start_timestamp

@unique
class nmea_sentence(Enum):
  timestamp                              = 253     # Timestamp message was output
  timestamp_ms                           = 0       # Fractional part of timestamp, added to timestamp
  sentence                               = 1       # NMEA sentence

@unique
class aviation_attitude(Enum):
  timestamp                              = 253     # Timestamp message was output
  timestamp_ms                           = 0       # Fractional part of timestamp, added to timestamp
  system_time                            = 1       # System time associated with sample expressed in ms.
  pitch                                  = 2       # Range -PI/2 to +PI/2
  roll                                   = 3       # Range -PI to +PI
  accel_lateral                          = 4       # Range -78.4 to +78.4 (-8 Gs to 8 Gs)
  accel_normal                           = 5       # Range -78.4 to +78.4 (-8 Gs to 8 Gs)
  turn_rate                              = 6       # Range -8.727 to +8.727 (-500 degs/sec to +500 degs/sec)
  stage                                  = 7       
  attitude_stage_complete                = 8       # The percent complete of the current attitude stage.  Set to 0 for attitude stages 0, 1 and 2 and to 100 for attitude stage 3 by AHRS modules that do not support it.  Range - 100
  track                                  = 9       # Track Angle/Heading Range 0 - 2pi
  validity                               = 10      

@unique
class video(Enum):
  url                                    = 0       
  hosting_provider                       = 1       
  duration                               = 2       # Playback time of video

@unique
class video_title(Enum):
  message_index                          = 254     # Long titles will be split into multiple parts
  message_count                          = 0       # Total number of title parts
  text                                   = 1       

@unique
class video_description(Enum):
  message_index                          = 254     # Long descriptions will be split into multiple parts
  message_count                          = 0       # Total number of description parts
  text                                   = 1       

@unique
class video_clip(Enum):
  clip_number                            = 0       
  start_timestamp                        = 1       
  start_timestamp_ms                     = 2       
  end_timestamp                          = 3       
  end_timestamp_ms                       = 4       
  clip_start                             = 6       # Start of clip in video time
  clip_end                               = 7       # End of clip in video time

@unique
class set(Enum):
  timestamp                              = 254     # Timestamp of the set
  duration                               = 0       
  repetitions                            = 3       # # of repitions of the movement
  weight                                 = 4       # Amount of weight applied for the set
  set_type                               = 5       
  start_time                             = 6       # Start time of the set
  category                               = 7       
  category_subtype                       = 8       # Based on the associated category, see [category]_exercise_names
  weight_display_unit                    = 9       
  message_index                          = 10      
  wkt_step_index                         = 11      

@unique
class jump(Enum):
  timestamp                              = 253     
  distance                               = 0       
  height                                 = 1       
  rotations                              = 2       
  hang_time                              = 3       
  score                                  = 4       # A score for a jump calculated based on hang time, rotations, and distance.
  position_lat                           = 5       
  position_long                          = 6       
  speed                                  = 7       
  enhanced_speed                         = 8       

@unique
class course(Enum):
  sport                                  = 4       
  name                                   = 5       
  capabilities                           = 6       
  sub_sport                              = 7       

@unique
class course_point(Enum):
  message_index                          = 254     
  timestamp                              = 1       
  position_lat                           = 2       
  position_long                          = 3       
  distance                               = 4       
  type                                   = 5       
  name                                   = 6       
  favorite                               = 8       

@unique
class segment_id(Enum):
  # Unique Identification data for a segment file
  name                                   = 0       # Friendly name assigned to segment
  uuid                                   = 1       # UUID of the segment
  sport                                  = 2       # Sport associated with the segment
  enabled                                = 3       # Segment enabled for evaluation
  user_profile_primary_key               = 4       # Primary key of the user that created the segment
  device_id                              = 5       # ID of the device that created the segment
  default_race_leader                    = 6       # Index for the Leader Board entry selected as the default race participant
  delete_status                          = 7       # Indicates if any segments should be deleted
  selection_type                         = 8       # Indicates how the segment was selected to be sent to the device

@unique
class segment_leaderboard_entry(Enum):
  # Unique Identification data for an individual segment leader within a segment file
  message_index                          = 254     
  name                                   = 0       # Friendly name assigned to leader
  type                                   = 1       # Leader classification
  group_primary_key                      = 2       # Primary user ID of this leader
  activity_id                            = 3       # ID of the activity associated with this leader time
  segment_time                           = 4       # Segment Time (includes pauses)
  activity_id_string                     = 5       # String version of the activity_id. 21 characters long, express in decimal

@unique
class segment_point(Enum):
  # Navigation and race evaluation point for a segment decribing a point along the segment path and time it took each segment leader to reach that point
  message_index                          = 254     
  position_lat                           = 1       
  position_long                          = 2       
  distance                               = 3       # Accumulated distance along the segment at the described point
  altitude                               = 4       # Accumulated altitude along the segment at the described point
  leader_time                            = 5       # Accumualted time each leader board member required to reach the described point. This value is zero for all leader board members at the starting point of the segment.

@unique
class segment_lap(Enum):
  message_index                          = 254     
  timestamp                              = 253     # Lap end time.
  event                                  = 0       
  event_type                             = 1       
  start_time                             = 2       
  start_position_lat                     = 3       
  start_position_long                    = 4       
  end_position_lat                       = 5       
  end_position_long                      = 6       
  total_elapsed_time                     = 7       # Time (includes pauses)
  total_timer_time                       = 8       # Timer Time (excludes pauses)
  total_distance                         = 9       
  total_cycles                           = 10      
  total_calories                         = 11      
  total_fat_calories                     = 12      # If New Leaf
  avg_speed                              = 13      
  max_speed                              = 14      
  avg_heart_rate                         = 15      
  max_heart_rate                         = 16      
  avg_cadence                            = 17      # total_cycles / total_timer_time if non_zero_avg_cadence otherwise total_cycles / total_elapsed_time
  max_cadence                            = 18      
  avg_power                              = 19      # total_power / total_timer_time if non_zero_avg_power otherwise total_power / total_elapsed_time
  max_power                              = 20      
  total_ascent                           = 21      
  total_descent                          = 22      
  sport                                  = 23      
  event_group                            = 24      
  nec_lat                                = 25      # North east corner latitude.
  nec_long                               = 26      # North east corner longitude.
  swc_lat                                = 27      # South west corner latitude.
  swc_long                               = 28      # South west corner latitude.
  name                                   = 29      
  normalized_power                       = 30      
  left_right_balance                     = 31      
  sub_sport                              = 32      
  total_work                             = 33      
  avg_altitude                           = 34      
  max_altitude                           = 35      
  gps_accuracy                           = 36      
  avg_grade                              = 37      
  avg_pos_grade                          = 38      
  avg_neg_grade                          = 39      
  max_pos_grade                          = 40      
  max_neg_grade                          = 41      
  avg_temperature                        = 42      
  max_temperature                        = 43      
  total_moving_time                      = 44      
  avg_pos_vertical_speed                 = 45      
  avg_neg_vertical_speed                 = 46      
  max_pos_vertical_speed                 = 47      
  max_neg_vertical_speed                 = 48      
  time_in_hr_zone                        = 49      
  time_in_speed_zone                     = 50      
  time_in_cadence_zone                   = 51      
  time_in_power_zone                     = 52      
  repetition_num                         = 53      
  min_altitude                           = 54      
  min_heart_rate                         = 55      
  active_time                            = 56      
  wkt_step_index                         = 57      
  sport_event                            = 58      
  avg_left_torque_effectiveness          = 59      
  avg_right_torque_effectiveness         = 60      
  avg_left_pedal_smoothness              = 61      
  avg_right_pedal_smoothness             = 62      
  avg_combined_pedal_smoothness          = 63      
  status                                 = 64      
  uuid                                   = 65      
  avg_fractional_cadence                 = 66      # fractional part of the avg_cadence
  max_fractional_cadence                 = 67      # fractional part of the max_cadence
  total_fractional_cycles                = 68      # fractional part of the total_cycles
  front_gear_shift_count                 = 69      
  rear_gear_shift_count                  = 70      
  time_standing                          = 71      # Total time spent in the standing position
  stand_count                            = 72      # Number of transitions to the standing state
  avg_left_pco                           = 73      # Average left platform center offset
  avg_right_pco                          = 74      # Average right platform center offset
  avg_left_power_phase                   = 75      # Average left power phase angles. Data value indexes defined by power_phase_type.
  avg_left_power_phase_peak              = 76      # Average left power phase peak angles. Data value indexes defined by power_phase_type.
  avg_right_power_phase                  = 77      # Average right power phase angles. Data value indexes defined by power_phase_type.
  avg_right_power_phase_peak             = 78      # Average right power phase peak angles. Data value indexes defined by power_phase_type.
  avg_power_position                     = 79      # Average power by position. Data value indexes defined by rider_position_type.
  max_power_position                     = 80      # Maximum power by position. Data value indexes defined by rider_position_type.
  avg_cadence_position                   = 81      # Average cadence by position. Data value indexes defined by rider_position_type.
  max_cadence_position                   = 82      # Maximum cadence by position. Data value indexes defined by rider_position_type.
  manufacturer                           = 83      # Manufacturer that produced the segment
  total_grit                             = 84      # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  total_flow                             = 85      # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.
  avg_grit                               = 86      # The grit score estimates how challenging a route could be for a cyclist in terms of time spent going over sharp turns or large grade slopes.
  avg_flow                               = 87      # The flow score estimates how long distance wise a cyclist deaccelerates over intervals where deacceleration is unnecessary such as smooth turns or small grade angle intervals.

@unique
class segment_file(Enum):
  # Summary of the unique segment and leaderboard information associated with a segment file. This message is used to compile a segment list file describing all segment files on a device. The segment list file is used when refreshing the contents of a segment file with the latest available leaderboard information.
  message_index                          = 254     
  file_uuid                              = 1       # UUID of the segment file
  enabled                                = 3       # Enabled state of the segment file
  user_profile_primary_key               = 4       # Primary key of the user that created the segment file
  leader_type                            = 7       # Leader type of each leader in the segment file
  leader_group_primary_key               = 8       # Group primary key of each leader in the segment file
  leader_activity_id                     = 9       # Activity ID of each leader in the segment file
  leader_activity_id_string              = 10      # String version of the activity ID of each leader in the segment file. 21 characters long for each ID, express in decimal
  default_race_leader                    = 11      # Index for the Leader Board entry selected as the default race participant

@unique
class workout(Enum):
  sport                                  = 4       
  capabilities                           = 5       
  num_valid_steps                        = 6       # number of valid steps
  wkt_name                               = 8       
  sub_sport                              = 11      
  pool_length                            = 14      
  pool_length_unit                       = 15      

@unique
class workout_session(Enum):
  message_index                          = 254     
  sport                                  = 0       
  sub_sport                              = 1       
  num_valid_steps                        = 2       
  first_step_index                       = 3       
  pool_length                            = 4       
  pool_length_unit                       = 5       

@unique
class workout_step(Enum):
  message_index                          = 254     
  wkt_step_name                          = 0       
  duration_type                          = 1       
  duration_value                         = 2       
  target_type                            = 3       
  target_value                           = 4       
  custom_target_value_low                = 5       
  custom_target_value_high               = 6       
  intensity                              = 7       
  notes                                  = 8       
  equipment                              = 9       
  exercise_category                      = 10      
  exercise_name                          = 11      
  exercise_weight                        = 12      
  weight_display_unit                    = 13      

@unique
class exercise_title(Enum):
  message_index                          = 254     
  exercise_category                      = 0       
  exercise_name                          = 1       
  wkt_step_name                          = 2       

@unique
class schedule(Enum):
  manufacturer                           = 0       # Corresponds to file_id of scheduled workout / course.
  product                                = 1       # Corresponds to file_id of scheduled workout / course.
  serial_number                          = 2       # Corresponds to file_id of scheduled workout / course.
  time_created                           = 3       # Corresponds to file_id of scheduled workout / course.
  completed                              = 4       # TRUE if this activity has been started
  type                                   = 5       
  scheduled_time                         = 6       

@unique
class totals(Enum):
  message_index                          = 254     
  timestamp                              = 253     
  timer_time                             = 0       # Excludes pauses
  distance                               = 1       
  calories                               = 2       
  sport                                  = 3       
  elapsed_time                           = 4       # Includes pauses
  sessions                               = 5       
  active_time                            = 6       
  sport_index                            = 9       

@unique
class weight_scale(Enum):
  timestamp                              = 253     
  weight                                 = 0       
  percent_fat                            = 1       
  percent_hydration                      = 2       
  visceral_fat_mass                      = 3       
  bone_mass                              = 4       
  muscle_mass                            = 5       
  basal_met                              = 7       
  physique_rating                        = 8       
  active_met                             = 9       # ~4kJ per kcal, 0.25 allows max 16384 kcal
  metabolic_age                          = 10      
  visceral_fat_rating                    = 11      
  user_profile_index                     = 12      # Associates this weight scale message to a user.  This corresponds to the index of the user profile message in the weight scale file.

@unique
class blood_pressure(Enum):
  timestamp                              = 253     
  systolic_pressure                      = 0       
  diastolic_pressure                     = 1       
  mean_arterial_pressure                 = 2       
  map_3_sample_mean                      = 3       
  map_morning_values                     = 4       
  map_evening_values                     = 5       
  heart_rate                             = 6       
  heart_rate_type                        = 7       
  status                                 = 8       
  user_profile_index                     = 9       # Associates this blood pressure message to a user.  This corresponds to the index of the user profile message in the blood pressure file.

@unique
class monitoring_info(Enum):
  timestamp                              = 253     
  local_timestamp                        = 0       # Use to convert activity timestamps to local time if device does not support time zone and daylight savings time correction.
  activity_type                          = 1       
  cycles_to_distance                     = 3       # Indexed by activity_type
  cycles_to_calories                     = 4       # Indexed by activity_type
  resting_metabolic_rate                 = 5       

@unique
class monitoring(Enum):
  timestamp                              = 253     # Must align to logging interval, for example, time must be 00:00:00 for daily log.
  device_index                           = 0       # Associates this data to device_info message.  Not required for file with single device (sensor).
  calories                               = 1       # Accumulated total calories.  Maintained by MonitoringReader for each activity_type.  See SDK documentation
  distance                               = 2       # Accumulated distance.  Maintained by MonitoringReader for each activity_type.  See SDK documentation.
  cycles                                 = 3       # Accumulated cycles.  Maintained by MonitoringReader for each activity_type.  See SDK documentation.
  active_time                            = 4       
  activity_type                          = 5       
  activity_subtype                       = 6       
  activity_level                         = 7       
  distance_16                            = 8       
  cycles_16                              = 9       
  active_time_16                         = 10      
  local_timestamp                        = 11      # Must align to logging interval, for example, time must be 00:00:00 for daily log.
  temperature                            = 12      # Avg temperature during the logging interval ended at timestamp
  temperature_min                        = 14      # Min temperature during the logging interval ended at timestamp
  temperature_max                        = 15      # Max temperature during the logging interval ended at timestamp
  activity_time                          = 16      # Indexed using minute_activity_level enum
  active_calories                        = 19      
  current_activity_type_intensity        = 24      # Indicates single type / intensity for duration since last monitoring message.
  timestamp_min_8                        = 25      
  timestamp_16                           = 26      
  heart_rate                             = 27      
  intensity                              = 28      
  duration_min                           = 29      
  duration                               = 30      
  ascent                                 = 31      
  descent                                = 32      
  moderate_activity_minutes              = 33      
  vigorous_activity_minutes              = 34      

@unique
class hr(Enum):
  timestamp                              = 253     
  fractional_timestamp                   = 0       
  time256                                = 1       
  filtered_bpm                           = 6       
  event_timestamp                        = 9       
  event_timestamp_12                     = 10      

@unique
class stress_level(Enum):
  # Value from 1 to 100 calculated by FirstBeat
  stress_level_value                     = 0       
  stress_level_time                      = 1       # Time stress score was calculated

@unique
class memo_glob(Enum):
  part_index                             = 250     # Sequence number of memo blocks
  memo                                   = 0       # Block of utf8 bytes
  message_number                         = 1       # Allows relating glob to another mesg  If used only required for first part of each memo_glob
  message_index                          = 2       # Index of external mesg

@unique
class ant_channel_id(Enum):
  channel_number                         = 0       
  device_type                            = 1       
  device_number                          = 2       
  transmission_type                      = 3       
  device_index                           = 4       

@unique
class ant_rx(Enum):
  timestamp                              = 253     
  fractional_timestamp                   = 0       
  mesg_id                                = 1       
  mesg_data                              = 2       
  channel_number                         = 3       
  data                                   = 4       

@unique
class ant_tx(Enum):
  timestamp                              = 253     
  fractional_timestamp                   = 0       
  mesg_id                                = 1       
  mesg_data                              = 2       
  channel_number                         = 3       
  data                                   = 4       

@unique
class exd_screen_configuration(Enum):
  screen_index                           = 0       
  field_count                            = 1       # number of fields in screen
  layout                                 = 2       
  screen_enabled                         = 3       

@unique
class exd_data_field_configuration(Enum):
  screen_index                           = 0       
  concept_field                          = 1       
  field_id                               = 2       
  concept_count                          = 3       
  display_type                           = 4       
  title                                  = 5       

@unique
class exd_data_concept_configuration(Enum):
  screen_index                           = 0       
  concept_field                          = 1       
  field_id                               = 2       
  concept_index                          = 3       
  data_page                              = 4       
  concept_key                            = 5       
  scaling                                = 6       
  data_units                             = 8       
  qualifier                              = 9       
  descriptor                             = 10      
  is_signed                              = 11      

@unique
class field_description(Enum):
  # Must be logged before developer field is used
  developer_data_index                   = 0       
  field_definition_number                = 1       
  fit_base_type_id                       = 2       
  field_name                             = 3       
  array                                  = 4       
  components                             = 5       
  scale                                  = 6       
  offset                                 = 7       
  units                                  = 8       
  bits                                   = 9       
  accumulate                             = 10      
  fit_base_unit_id                       = 13      
  native_mesg_num                        = 14      
  native_field_num                       = 15      

@unique
class developer_data_id(Enum):
  # Must be logged before field description
  developer_id                           = 0       
  application_id                         = 1       
  manufacturer_id                        = 2       
  developer_data_index                   = 3       
  application_version                    = 4       

@unique
class dive_summary(Enum):
  timestamp                              = 253     
  reference_mesg                         = 0       
  reference_index                        = 1       
  avg_depth                              = 2       # 0 if above water
  max_depth                              = 3       # 0 if above water
  surface_interval                       = 4       # Time since end of last dive
  start_cns                              = 5       
  end_cns                                = 6       
  start_n2                               = 7       
  end_n2                                 = 8       
  o2_toxicity                            = 9       
  dive_number                            = 10      
  bottom_time                            = 11      

@unique
class climb_pro(Enum):
  timestamp                              = 253     
  position_lat                           = 0       
  position_long                          = 1       
  climb_pro_event                        = 2       
  climb_number                           = 3       
  climb_category                         = 4       
  current_dist                           = 5       
