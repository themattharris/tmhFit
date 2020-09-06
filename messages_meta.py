### THIS FILE IS AUTO-GENERATED ###
# Garmin FIT message types from profile.xslx in the SDK
# Version: FitSDKRelease_21.32.00
import basetypes
import profile
import sys

def by_name(name):
  return sys.modules[__name__].__getattribute__(name)

class file_id():
  type = {
    'type'          : profile.file,
  }
  manufacturer = {
    'type'          : profile.manufacturer,
  }
  product = {
    'type'          : basetypes.Field.uint16,
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
  }
  time_created = {
    'type'          : profile.date_time,
  }
  number = {
    'type'          : basetypes.Field.uint16,
  }
  product_name = {
    'type'          : basetypes.Field.string,
  }

class file_creator():
  software_version = {
    'type'          : basetypes.Field.uint16,
  }
  hardware_version = {
    'type'          : basetypes.Field.uint8,
  }

class timestamp_correlation():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'units'         : "s",
  }
  system_timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  fractional_system_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'units'         : "s",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  system_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }

class software():
  message_index = {
    'type'          : profile.message_index,
  }
  version = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
  }
  part_number = {
    'type'          : basetypes.Field.string,
  }

class slave_device():
  manufacturer = {
    'type'          : profile.manufacturer,
  }
  product = {
    'type'          : basetypes.Field.uint16,
  }

class capabilities():
  languages = {
    'type'          : basetypes.Field.uint8z,
    'array'         : "[N]",
  }
  sports = {
    'type'          : profile.sport_bits_0,
    'array'         : "[N]",
  }
  workouts_supported = {
    'type'          : profile.workout_capabilities,
  }
  connectivity_supported = {
    'type'          : profile.connectivity_capabilities,
  }

class file_capabilities():
  message_index = {
    'type'          : profile.message_index,
  }
  type = {
    'type'          : profile.file,
  }
  flags = {
    'type'          : profile.file_flags,
  }
  directory = {
    'type'          : basetypes.Field.string,
  }
  max_count = {
    'type'          : basetypes.Field.uint16,
  }
  max_size = {
    'type'          : basetypes.Field.uint32,
    'units'         : "bytes",
  }

class mesg_capabilities():
  message_index = {
    'type'          : profile.message_index,
  }
  file = {
    'type'          : profile.file,
  }
  mesg_num = {
    'type'          : profile.mesg_num,
  }
  count_type = {
    'type'          : profile.mesg_count,
  }
  count = {
    'type'          : basetypes.Field.uint16,
  }

class field_capabilities():
  message_index = {
    'type'          : profile.message_index,
  }
  file = {
    'type'          : profile.file,
  }
  mesg_num = {
    'type'          : profile.mesg_num,
  }
  field_num = {
    'type'          : basetypes.Field.uint8,
  }
  count = {
    'type'          : basetypes.Field.uint16,
  }

class device_settings():
  active_time_zone = {
    'type'          : basetypes.Field.uint8,
  }
  utc_offset = {
    'type'          : basetypes.Field.uint32,
  }
  time_offset = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'units'         : "s",
  }
  time_mode = {
    'type'          : profile.time_mode,
    'array'         : "[N]",
  }
  time_zone_offset = {
    'type'          : basetypes.Field.sint8,
    'array'         : "[N]",
    'scale'         : 4,
    'units'         : "hr",
  }
  backlight_mode = {
    'type'          : profile.backlight_mode,
  }
  activity_tracker_enabled = {
    'type'          : profile.bool,
  }
  clock_time = {
    'type'          : profile.date_time,
  }
  pages_enabled = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
  }
  move_alert_enabled = {
    'type'          : profile.bool,
  }
  date_mode = {
    'type'          : profile.date_mode,
  }
  display_orientation = {
    'type'          : profile.display_orientation,
  }
  mounting_side = {
    'type'          : profile.side,
  }
  default_page = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
  }
  autosync_min_steps = {
    'type'          : basetypes.Field.uint16,
    'units'         : "steps",
  }
  autosync_min_time = {
    'type'          : basetypes.Field.uint16,
    'units'         : "minutes",
  }
  lactate_threshold_autodetect_enabled = {
    'type'          : profile.bool,
  }
  ble_auto_upload_enabled = {
    'type'          : profile.bool,
  }
  auto_sync_frequency = {
    'type'          : profile.auto_sync_frequency,
  }
  auto_activity_detect = {
    'type'          : profile.auto_activity_detect,
  }
  number_of_screens = {
    'type'          : basetypes.Field.uint8,
  }
  smart_notification_display_orientation = {
    'type'          : profile.display_orientation,
  }
  tap_interface = {
    'type'          : profile.switch,
  }
  tap_sensitivity = {
    'type'          : profile.tap_sensitivity,
    'offset'        : 1,
  }

class user_profile():
  message_index = {
    'type'          : profile.message_index,
  }
  friendly_name = {
    'type'          : basetypes.Field.string,
  }
  gender = {
    'type'          : profile.gender,
  }
  age = {
    'type'          : basetypes.Field.uint8,
    'units'         : "years",
  }
  height = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'units'         : "m",
  }
  weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "kg",
  }
  language = {
    'type'          : profile.language,
  }
  elev_setting = {
    'type'          : profile.display_measure,
  }
  weight_setting = {
    'type'          : profile.display_measure,
  }
  resting_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  default_max_running_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  default_max_biking_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  default_max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  hr_setting = {
    'type'          : profile.display_heart,
  }
  speed_setting = {
    'type'          : profile.display_measure,
  }
  dist_setting = {
    'type'          : profile.display_measure,
  }
  power_setting = {
    'type'          : profile.display_power,
  }
  activity_class = {
    'type'          : profile.activity_class,
  }
  position_setting = {
    'type'          : profile.display_position,
  }
  temperature_setting = {
    'type'          : profile.display_measure,
  }
  local_id = {
    'type'          : profile.user_local_id,
  }
  global_id = {
    'type'          : basetypes.Field.byte,
    'array'         : "[6]",
  }
  wake_time = {
    'type'          : profile.localtime_into_day,
  }
  sleep_time = {
    'type'          : profile.localtime_into_day,
  }
  height_setting = {
    'type'          : profile.display_measure,
  }
  user_running_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m",
  }
  user_walking_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m",
  }
  depth_setting = {
    'type'          : profile.display_measure,
  }
  dive_count = {
    'type'          : basetypes.Field.uint32,
  }

class hrm_profile():
  message_index = {
    'type'          : profile.message_index,
  }
  enabled = {
    'type'          : profile.bool,
  }
  hrm_ant_id = {
    'type'          : basetypes.Field.uint16z,
  }
  log_hrv = {
    'type'          : profile.bool,
  }
  hrm_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
  }

class sdm_profile():
  message_index = {
    'type'          : profile.message_index,
  }
  enabled = {
    'type'          : profile.bool,
  }
  sdm_ant_id = {
    'type'          : basetypes.Field.uint16z,
  }
  sdm_cal_factor = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "%",
  }
  odometer = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  speed_source = {
    'type'          : profile.bool,
  }
  sdm_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
  }
  odometer_rollover = {
    'type'          : basetypes.Field.uint8,
  }

class bike_profile():
  message_index = {
    'type'          : profile.message_index,
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  sport = {
    'type'          : profile.sport,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  odometer = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  bike_spd_ant_id = {
    'type'          : basetypes.Field.uint16z,
  }
  bike_cad_ant_id = {
    'type'          : basetypes.Field.uint16z,
  }
  bike_spdcad_ant_id = {
    'type'          : basetypes.Field.uint16z,
  }
  bike_power_ant_id = {
    'type'          : basetypes.Field.uint16z,
  }
  custom_wheelsize = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m",
  }
  auto_wheelsize = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m",
  }
  bike_weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "kg",
  }
  power_cal_factor = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "%",
  }
  auto_wheel_cal = {
    'type'          : profile.bool,
  }
  auto_power_zero = {
    'type'          : profile.bool,
  }
  id = {
    'type'          : basetypes.Field.uint8,
  }
  spd_enabled = {
    'type'          : profile.bool,
  }
  cad_enabled = {
    'type'          : profile.bool,
  }
  spdcad_enabled = {
    'type'          : profile.bool,
  }
  power_enabled = {
    'type'          : profile.bool,
  }
  crank_length = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : "-110",
    'units'         : "mm",
  }
  enabled = {
    'type'          : profile.bool,
  }
  bike_spd_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
  }
  bike_cad_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
  }
  bike_spdcad_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
  }
  bike_power_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
  }
  odometer_rollover = {
    'type'          : basetypes.Field.uint8,
  }
  front_gear_num = {
    'type'          : basetypes.Field.uint8z,
  }
  front_gear = {
    'type'          : basetypes.Field.uint8z,
    'array'         : "[N]",
  }
  rear_gear_num = {
    'type'          : basetypes.Field.uint8z,
  }
  rear_gear = {
    'type'          : basetypes.Field.uint8z,
    'array'         : "[N]",
  }
  shimano_di2_enabled = {
    'type'          : profile.bool,
  }

class connectivity():
  bluetooth_enabled = {
    'type'          : profile.bool,
  }
  bluetooth_le_enabled = {
    'type'          : profile.bool,
  }
  ant_enabled = {
    'type'          : profile.bool,
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  live_tracking_enabled = {
    'type'          : profile.bool,
  }
  weather_conditions_enabled = {
    'type'          : profile.bool,
  }
  weather_alerts_enabled = {
    'type'          : profile.bool,
  }
  auto_activity_upload_enabled = {
    'type'          : profile.bool,
  }
  course_download_enabled = {
    'type'          : profile.bool,
  }
  workout_download_enabled = {
    'type'          : profile.bool,
  }
  gps_ephemeris_download_enabled = {
    'type'          : profile.bool,
  }
  incident_detection_enabled = {
    'type'          : profile.bool,
  }
  grouptrack_enabled = {
    'type'          : profile.bool,
  }

class watchface_settings():
  message_index = {
    'type'          : profile.message_index,
  }
  mode = {
    'type'          : profile.watchface_mode,
  }
  layout = {
    'type'          : basetypes.Field.byte,
  }

class ohr_settings():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  enabled = {
    'type'          : profile.switch,
  }

class zones_target():
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
  }
  threshold_heart_rate = {
    'type'          : basetypes.Field.uint8,
  }
  functional_threshold_power = {
    'type'          : basetypes.Field.uint16,
  }
  hr_calc_type = {
    'type'          : profile.hr_zone_calc,
  }
  pwr_calc_type = {
    'type'          : profile.pwr_zone_calc,
  }

class sport():
  sport = {
    'type'          : profile.sport,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  name = {
    'type'          : basetypes.Field.string,
  }

class hr_zone():
  message_index = {
    'type'          : profile.message_index,
  }
  high_bpm = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  name = {
    'type'          : basetypes.Field.string,
  }

class speed_zone():
  message_index = {
    'type'          : profile.message_index,
  }
  high_value = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  name = {
    'type'          : basetypes.Field.string,
  }

class cadence_zone():
  message_index = {
    'type'          : profile.message_index,
  }
  high_value = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  name = {
    'type'          : basetypes.Field.string,
  }

class power_zone():
  message_index = {
    'type'          : profile.message_index,
  }
  high_value = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  name = {
    'type'          : basetypes.Field.string,
  }

class met_zone():
  message_index = {
    'type'          : profile.message_index,
  }
  high_bpm = {
    'type'          : basetypes.Field.uint8,
  }
  calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "kcal / min",
  }
  fat_calories = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
    'units'         : "kcal / min",
  }

class dive_settings():
  message_index = {
    'type'          : profile.message_index,
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  model = {
    'type'          : profile.tissue_model_type,
  }
  gf_low = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }
  gf_high = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }
  water_type = {
    'type'          : profile.water_type,
  }
  water_density = {
    'type'          : basetypes.Field.float32,
    'units'         : "kg/m^3",
  }
  po2_warn = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'units'         : "percent",
  }
  po2_critical = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'units'         : "percent",
  }
  po2_deco = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'units'         : "percent",
  }
  safety_stop_enabled = {
    'type'          : profile.bool,
  }
  bottom_depth = {
    'type'          : basetypes.Field.float32,
  }
  bottom_time = {
    'type'          : basetypes.Field.uint32,
  }
  apnea_countdown_enabled = {
    'type'          : profile.bool,
  }
  apnea_countdown_time = {
    'type'          : basetypes.Field.uint32,
  }
  backlight_mode = {
    'type'          : profile.dive_backlight_mode,
  }
  backlight_brightness = {
    'type'          : basetypes.Field.uint8,
  }
  backlight_timeout = {
    'type'          : profile.backlight_timeout,
  }
  repeat_dive_interval = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'units'         : "s",
  }
  safety_stop_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'units'         : "s",
  }
  heart_rate_source_type = {
    'type'          : profile.source_type,
  }
  heart_rate_source = {
    'type'          : basetypes.Field.uint8,
  }

class dive_alarm():
  message_index = {
    'type'          : profile.message_index,
  }
  depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  time = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'units'         : "s",
  }
  enabled = {
    'type'          : profile.bool,
  }
  alarm_type = {
    'type'          : profile.dive_alarm_type,
  }
  sound = {
    'type'          : profile.tone,
  }
  dive_types = {
    'type'          : profile.sub_sport,
    'array'         : "[N]",
  }

class dive_gas():
  message_index = {
    'type'          : profile.message_index,
  }
  helium_content = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }
  oxygen_content = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }
  status = {
    'type'          : profile.dive_gas_status,
  }

class goal():
  message_index = {
    'type'          : profile.message_index,
  }
  sport = {
    'type'          : profile.sport,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  start_date = {
    'type'          : profile.date_time,
  }
  end_date = {
    'type'          : profile.date_time,
  }
  type = {
    'type'          : profile.goal,
  }
  value = {
    'type'          : basetypes.Field.uint32,
  }
  repeat = {
    'type'          : profile.bool,
  }
  target_value = {
    'type'          : basetypes.Field.uint32,
  }
  recurrence = {
    'type'          : profile.goal_recurrence,
  }
  recurrence_value = {
    'type'          : basetypes.Field.uint16,
  }
  enabled = {
    'type'          : profile.bool,
  }
  source = {
    'type'          : profile.goal_source,
  }

class activity():
  timestamp = {
    'type'          : profile.date_time,
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  num_sessions = {
    'type'          : basetypes.Field.uint16,
  }
  type = {
    'type'          : profile.activity,
  }
  event = {
    'type'          : profile.event,
  }
  event_type = {
    'type'          : profile.event_type,
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
  }

class session():
  message_index = {
    'type'          : profile.message_index,
  }
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
  }
  event_type = {
    'type'          : profile.event_type,
  }
  start_time = {
    'type'          : profile.date_time,
  }
  start_position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  start_position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  sport = {
    'type'          : profile.sport,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'units'         : "cycles",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  total_fat_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_avg_speed",
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  max_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_max_speed",
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  avg_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  avg_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  max_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  avg_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  max_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  total_ascent = {
    'type'          : basetypes.Field.uint16,
    'units'         : "m",
  }
  total_descent = {
    'type'          : basetypes.Field.uint16,
    'units'         : "m",
  }
  total_training_effect = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
  }
  first_lap_index = {
    'type'          : basetypes.Field.uint16,
  }
  num_laps = {
    'type'          : basetypes.Field.uint16,
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
  }
  trigger = {
    'type'          : profile.session_trigger,
  }
  nec_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  nec_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  swc_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  swc_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  normalized_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  training_stress_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "tss",
  }
  intensity_factor = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "if",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance_100,
  }
  avg_stroke_count = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 10,
    'units'         : "strokes/lap",
  }
  avg_stroke_distance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m",
  }
  swim_stroke = {
    'type'          : profile.swim_stroke,
    'units'         : "swim_stroke",
  }
  pool_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m",
  }
  threshold_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  pool_length_unit = {
    'type'          : profile.display_measure,
  }
  num_active_lengths = {
    'type'          : basetypes.Field.uint16,
    'units'         : "lengths",
  }
  total_work = {
    'type'          : basetypes.Field.uint32,
    'units'         : "J",
  }
  avg_altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_avg_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  max_altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_max_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  gps_accuracy = {
    'type'          : basetypes.Field.uint8,
    'units'         : "m",
  }
  avg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  max_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  max_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  max_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  total_moving_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  avg_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  avg_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  min_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  time_in_hr_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_speed_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_cadence_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_power_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  avg_lap_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  best_lap_index = {
    'type'          : basetypes.Field.uint16,
  }
  min_altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_min_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  player_score = {
    'type'          : basetypes.Field.uint16,
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
  }
  opponent_name = {
    'type'          : basetypes.Field.string,
  }
  stroke_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  zone_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  max_ball_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m/s",
  }
  avg_ball_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m/s",
  }
  avg_vertical_oscillation = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "mm",
  }
  avg_stance_time_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  avg_stance_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "ms",
  }
  avg_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  max_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  total_fractional_cycles = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "cycles",
  }
  avg_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "g/dL",
  }
  min_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "g/dL",
  }
  max_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "g/dL",
  }
  avg_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'units'         : "%",
  }
  min_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'units'         : "%",
  }
  max_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'units'         : "%",
  }
  avg_left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  sport_index = {
    'type'          : basetypes.Field.uint8,
  }
  time_standing = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  stand_count = {
    'type'          : basetypes.Field.uint16,
  }
  avg_left_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  avg_right_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  avg_left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "watts",
  }
  max_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "watts",
  }
  avg_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "rpm",
  }
  max_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "rpm",
  }
  enhanced_avg_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  enhanced_max_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  enhanced_avg_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  enhanced_min_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  enhanced_max_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  avg_lev_motor_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  max_lev_motor_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  lev_battery_consumption = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_vertical_ratio = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  avg_stance_time_balance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  avg_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "mm",
  }
  total_anaerobic_training_effect = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
  }
  avg_vam = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  total_grit = {
    'type'          : basetypes.Field.float32,
    'units'         : "kGrit",
  }
  total_flow = {
    'type'          : basetypes.Field.float32,
    'units'         : "Flow",
  }
  jump_count = {
    'type'          : basetypes.Field.uint16,
  }
  avg_grit = {
    'type'          : basetypes.Field.float32,
    'units'         : "kGrit",
  }
  avg_flow = {
    'type'          : basetypes.Field.float32,
    'units'         : "Flow",
  }

class lap():
  message_index = {
    'type'          : profile.message_index,
  }
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
  }
  event_type = {
    'type'          : profile.event_type,
  }
  start_time = {
    'type'          : profile.date_time,
  }
  start_position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  start_position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  end_position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  end_position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'units'         : "cycles",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  total_fat_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_avg_speed",
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  max_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_max_speed",
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  avg_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  avg_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  max_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  avg_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  max_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  total_ascent = {
    'type'          : basetypes.Field.uint16,
    'units'         : "m",
  }
  total_descent = {
    'type'          : basetypes.Field.uint16,
    'units'         : "m",
  }
  intensity = {
    'type'          : profile.intensity,
  }
  lap_trigger = {
    'type'          : profile.lap_trigger,
  }
  sport = {
    'type'          : profile.sport,
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
  }
  num_lengths = {
    'type'          : basetypes.Field.uint16,
    'units'         : "lengths",
  }
  normalized_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance_100,
  }
  first_length_index = {
    'type'          : basetypes.Field.uint16,
  }
  avg_stroke_distance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m",
  }
  swim_stroke = {
    'type'          : profile.swim_stroke,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  num_active_lengths = {
    'type'          : basetypes.Field.uint16,
    'units'         : "lengths",
  }
  total_work = {
    'type'          : basetypes.Field.uint32,
    'units'         : "J",
  }
  avg_altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_avg_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  max_altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_max_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  gps_accuracy = {
    'type'          : basetypes.Field.uint8,
    'units'         : "m",
  }
  avg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  max_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  max_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  max_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  total_moving_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  avg_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  avg_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  time_in_hr_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_speed_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_cadence_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_power_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  repetition_num = {
    'type'          : basetypes.Field.uint16,
  }
  min_altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_min_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  min_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  wkt_step_index = {
    'type'          : profile.message_index,
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
  }
  stroke_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  zone_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  avg_vertical_oscillation = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "mm",
  }
  avg_stance_time_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  avg_stance_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "ms",
  }
  avg_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  max_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  total_fractional_cycles = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "cycles",
  }
  player_score = {
    'type'          : basetypes.Field.uint16,
  }
  avg_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "g/dL",
  }
  min_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "g/dL",
  }
  max_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "g/dL",
  }
  avg_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'units'         : "%",
  }
  min_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'units'         : "%",
  }
  max_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'units'         : "%",
  }
  avg_left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  time_standing = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  stand_count = {
    'type'          : basetypes.Field.uint16,
  }
  avg_left_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  avg_right_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  avg_left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "watts",
  }
  max_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "watts",
  }
  avg_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "rpm",
  }
  max_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "rpm",
  }
  enhanced_avg_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  enhanced_max_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  enhanced_avg_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  enhanced_min_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  enhanced_max_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  avg_lev_motor_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  max_lev_motor_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  lev_battery_consumption = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_vertical_ratio = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  avg_stance_time_balance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  avg_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "mm",
  }
  avg_vam = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  total_grit = {
    'type'          : basetypes.Field.float32,
    'units'         : "kGrit",
  }
  total_flow = {
    'type'          : basetypes.Field.float32,
    'units'         : "Flow",
  }
  jump_count = {
    'type'          : basetypes.Field.uint16,
  }
  avg_grit = {
    'type'          : basetypes.Field.float32,
    'units'         : "kGrit",
  }
  avg_flow = {
    'type'          : basetypes.Field.float32,
    'units'         : "Flow",
  }

class length():
  message_index = {
    'type'          : profile.message_index,
  }
  timestamp = {
    'type'          : profile.date_time,
  }
  event = {
    'type'          : profile.event,
  }
  event_type = {
    'type'          : profile.event_type,
  }
  start_time = {
    'type'          : profile.date_time,
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_strokes = {
    'type'          : basetypes.Field.uint16,
    'units'         : "strokes",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  swim_stroke = {
    'type'          : profile.swim_stroke,
    'units'         : "swim_stroke",
  }
  avg_swimming_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "strokes/min",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  length_type = {
    'type'          : profile.length_type,
  }
  player_score = {
    'type'          : basetypes.Field.uint16,
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
  }
  stroke_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  zone_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }

class record():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  altitude = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_altitude",
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
    'bits'          : "16",
  }
  heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_speed",
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  compressed_speed_distance = {
    'type'          : basetypes.Field.byte,
    'array'         : "[3]",
    'components'    : "speed, distance",
    'scale'         : "100, 16",
    'units'         : "m/s, m",
    'bits'          : "12, 12",
    'accumulate'    : "0, 1",
  }
  grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  resistance = {
    'type'          : basetypes.Field.uint8,
  }
  time_from_course = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  cycle_length = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'units'         : "m",
  }
  temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  speed_1s = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 16,
    'units'         : "m/s",
  }
  cycles = {
    'type'          : basetypes.Field.uint8,
    'components'    : "total_cycles",
    'units'         : "cycles",
    'bits'          : "8",
    'accumulate'    : "1",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'units'         : "cycles",
  }
  compressed_accumulated_power = {
    'type'          : basetypes.Field.uint16,
    'components'    : "accumulated_power",
    'units'         : "watts",
    'bits'          : "16",
    'accumulate'    : "1",
  }
  accumulated_power = {
    'type'          : basetypes.Field.uint32,
    'units'         : "watts",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance,
  }
  gps_accuracy = {
    'type'          : basetypes.Field.uint8,
    'units'         : "m",
  }
  vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  vertical_oscillation = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "mm",
  }
  stance_time_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  stance_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "ms",
  }
  activity_type = {
    'type'          : profile.activity_type,
  }
  left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  time128 = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "s",
  }
  stroke_type = {
    'type'          : profile.stroke_type,
  }
  zone = {
    'type'          : basetypes.Field.uint8,
  }
  ball_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m/s",
  }
  cadence256 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 256,
    'units'         : "rpm",
  }
  fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "g/dL",
  }
  total_hemoglobin_conc_min = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "g/dL",
  }
  total_hemoglobin_conc_max = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "g/dL",
  }
  saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "%",
  }
  saturated_hemoglobin_percent_min = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "%",
  }
  saturated_hemoglobin_percent_max = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "%",
  }
  device_index = {
    'type'          : profile.device_index,
  }
  left_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  right_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  enhanced_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  enhanced_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  battery_soc = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  motor_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  vertical_ratio = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  stance_time_balance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "percent",
  }
  step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'units'         : "mm",
  }
  absolute_pressure = {
    'type'          : basetypes.Field.uint32,
    'units'         : "Pa",
  }
  depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  next_stop_depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  next_stop_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'units'         : "s",
  }
  time_to_surface = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'units'         : "s",
  }
  ndl_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'units'         : "s",
  }
  cns_load = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }
  n2_load = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'units'         : "percent",
  }
  grit = {
    'type'          : basetypes.Field.float32,
  }
  flow = {
    'type'          : basetypes.Field.float32,
  }
  ebike_travel_range = {
    'type'          : basetypes.Field.uint16,
    'units'         : "km",
  }
  ebike_battery_level = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }
  ebike_assist_mode = {
    'type'          : basetypes.Field.uint8,
    'units'         : "depends on sensor",
  }
  ebike_assist_level_percent = {
    'type'          : basetypes.Field.uint8,
    'units'         : "percent",
  }

class event():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
  }
  event_type = {
    'type'          : profile.event_type,
  }
  data16 = {
    'type'          : basetypes.Field.uint16,
    'components'    : "data",
    'bits'          : "16",
  }
  data = {
    'type'          : basetypes.Field.uint32,
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
  }
  score = {
    'type'          : basetypes.Field.uint16,
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
  }
  front_gear_num = {
    'type'          : basetypes.Field.uint8z,
  }
  front_gear = {
    'type'          : basetypes.Field.uint8z,
  }
  rear_gear_num = {
    'type'          : basetypes.Field.uint8z,
  }
  rear_gear = {
    'type'          : basetypes.Field.uint8z,
  }
  device_index = {
    'type'          : profile.device_index,
  }
  radar_threat_level_max = {
    'type'          : profile.radar_threat_level_type,
  }
  radar_threat_count = {
    'type'          : basetypes.Field.uint8,
  }

class device_info():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  device_index = {
    'type'          : profile.device_index,
  }
  device_type = {
    'type'          : basetypes.Field.uint8,
  }
  manufacturer = {
    'type'          : profile.manufacturer,
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
  }
  product = {
    'type'          : basetypes.Field.uint16,
  }
  software_version = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
  }
  hardware_version = {
    'type'          : basetypes.Field.uint8,
  }
  cum_operating_time = {
    'type'          : basetypes.Field.uint32,
    'units'         : "s",
  }
  battery_voltage = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 256,
    'units'         : "V",
  }
  battery_status = {
    'type'          : profile.battery_status,
  }
  sensor_position = {
    'type'          : profile.body_location,
  }
  descriptor = {
    'type'          : basetypes.Field.string,
  }
  ant_transmission_type = {
    'type'          : basetypes.Field.uint8z,
  }
  ant_device_number = {
    'type'          : basetypes.Field.uint16z,
  }
  ant_network = {
    'type'          : profile.ant_network,
  }
  source_type = {
    'type'          : profile.source_type,
  }
  product_name = {
    'type'          : basetypes.Field.string,
  }

class training_file():
  timestamp = {
    'type'          : profile.date_time,
  }
  type = {
    'type'          : profile.file,
  }
  manufacturer = {
    'type'          : profile.manufacturer,
  }
  product = {
    'type'          : basetypes.Field.uint16,
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
  }
  time_created = {
    'type'          : profile.date_time,
  }

class hrv():
  time = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }

class weather_conditions():
  timestamp = {
    'type'          : profile.date_time,
  }
  weather_report = {
    'type'          : profile.weather_report,
  }
  temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  condition = {
    'type'          : profile.weather_status,
  }
  wind_direction = {
    'type'          : basetypes.Field.uint16,
    'units'         : "degrees",
  }
  wind_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  precipitation_probability = {
    'type'          : basetypes.Field.uint8,
  }
  temperature_feels_like = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  relative_humidity = {
    'type'          : basetypes.Field.uint8,
  }
  location = {
    'type'          : basetypes.Field.string,
  }
  observed_at_time = {
    'type'          : profile.date_time,
  }
  observed_location_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  observed_location_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  day_of_week = {
    'type'          : profile.day_of_week,
  }
  high_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  low_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }

class weather_alert():
  timestamp = {
    'type'          : profile.date_time,
  }
  report_id = {
    'type'          : basetypes.Field.string,
  }
  issue_time = {
    'type'          : profile.date_time,
  }
  expire_time = {
    'type'          : profile.date_time,
  }
  severity = {
    'type'          : profile.weather_severity,
  }
  type = {
    'type'          : profile.weather_severe_type,
  }

class gps_metadata():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  enhanced_altitude = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  enhanced_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  heading = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "degrees",
  }
  utc_timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  velocity = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[3]",
    'scale'         : 100,
    'units'         : "m/s",
  }

class camera_event():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  camera_event_type = {
    'type'          : profile.camera_event_type,
  }
  camera_file_uuid = {
    'type'          : basetypes.Field.string,
  }
  camera_orientation = {
    'type'          : profile.camera_orientation_type,
  }

class gyroscope_data():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "ms",
  }
  gyro_x = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  gyro_y = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  gyro_z = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  calibrated_gyro_x = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "deg/s",
  }
  calibrated_gyro_y = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "deg/s",
  }
  calibrated_gyro_z = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "deg/s",
  }

class accelerometer_data():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "ms",
  }
  accel_x = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  accel_y = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  accel_z = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  calibrated_accel_x = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "g",
  }
  calibrated_accel_y = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "g",
  }
  calibrated_accel_z = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "g",
  }
  compressed_calibrated_accel_x = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'units'         : "mG",
  }
  compressed_calibrated_accel_y = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'units'         : "mG",
  }
  compressed_calibrated_accel_z = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'units'         : "mG",
  }

class magnetometer_data():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "ms",
  }
  mag_x = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  mag_y = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  mag_z = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "counts",
  }
  calibrated_mag_x = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "G",
  }
  calibrated_mag_y = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "G",
  }
  calibrated_mag_z = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'units'         : "G",
  }

class barometer_data():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "ms",
  }
  baro_pres = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'units'         : "Pa",
  }

class three_d_sensor_calibration():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  sensor_type = {
    'type'          : profile.sensor_type,
  }
  calibration_factor = {
    'type'          : basetypes.Field.uint32,
  }
  calibration_divisor = {
    'type'          : basetypes.Field.uint32,
    'units'         : "counts",
  }
  level_shift = {
    'type'          : basetypes.Field.uint32,
  }
  offset_cal = {
    'type'          : basetypes.Field.sint32,
    'array'         : "[3]",
  }
  orientation_matrix = {
    'type'          : basetypes.Field.sint32,
    'array'         : "[9]",
    'scale'         : 65535,
  }

class one_d_sensor_calibration():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  sensor_type = {
    'type'          : profile.sensor_type,
  }
  calibration_factor = {
    'type'          : basetypes.Field.uint32,
  }
  calibration_divisor = {
    'type'          : basetypes.Field.uint32,
    'units'         : "counts",
  }
  level_shift = {
    'type'          : basetypes.Field.uint32,
  }
  offset_cal = {
    'type'          : basetypes.Field.sint32,
  }

class video_frame():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  frame_number = {
    'type'          : basetypes.Field.uint32,
  }

class obdii_data():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "ms",
  }
  pid = {
    'type'          : basetypes.Field.byte,
  }
  raw_data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
  }
  pid_data_size = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
  }
  system_time = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
  }
  start_timestamp = {
    'type'          : profile.date_time,
  }
  start_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }

class nmea_sentence():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  sentence = {
    'type'          : basetypes.Field.string,
  }

class aviation_attitude():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'units'         : "ms",
  }
  system_time = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'units'         : "ms",
  }
  pitch = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : "10430.38",
    'units'         : "radians",
  }
  roll = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : "10430.38",
    'units'         : "radians",
  }
  accel_lateral = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "m/s^2",
  }
  accel_normal = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 100,
    'units'         : "m/s^2",
  }
  turn_rate = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1024,
    'units'         : "radians/second",
  }
  stage = {
    'type'          : profile.attitude_stage,
    'array'         : "[N]",
  }
  attitude_stage_complete = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "%",
  }
  track = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : "10430.38",
    'units'         : "radians",
  }
  validity = {
    'type'          : profile.attitude_validity,
    'array'         : "[N]",
  }

class video():
  url = {
    'type'          : basetypes.Field.string,
  }
  hosting_provider = {
    'type'          : basetypes.Field.string,
  }
  duration = {
    'type'          : basetypes.Field.uint32,
    'units'         : "ms",
  }

class video_title():
  message_index = {
    'type'          : profile.message_index,
  }
  message_count = {
    'type'          : basetypes.Field.uint16,
  }
  text = {
    'type'          : basetypes.Field.string,
  }

class video_description():
  message_index = {
    'type'          : profile.message_index,
  }
  message_count = {
    'type'          : basetypes.Field.uint16,
  }
  text = {
    'type'          : basetypes.Field.string,
  }

class video_clip():
  clip_number = {
    'type'          : basetypes.Field.uint16,
  }
  start_timestamp = {
    'type'          : profile.date_time,
  }
  start_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
  }
  end_timestamp = {
    'type'          : profile.date_time,
  }
  end_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
  }
  clip_start = {
    'type'          : basetypes.Field.uint32,
    'units'         : "ms",
  }
  clip_end = {
    'type'          : basetypes.Field.uint32,
    'units'         : "ms",
  }

class set():
  timestamp = {
    'type'          : profile.date_time,
  }
  duration = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  repetitions = {
    'type'          : basetypes.Field.uint16,
  }
  weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 16,
    'units'         : "kg",
  }
  set_type = {
    'type'          : profile.set_type,
  }
  start_time = {
    'type'          : profile.date_time,
  }
  category = {
    'type'          : profile.exercise_category,
    'array'         : "[N]",
  }
  category_subtype = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
  }
  weight_display_unit = {
    'type'          : profile.fit_base_unit,
  }
  message_index = {
    'type'          : profile.message_index,
  }
  wkt_step_index = {
    'type'          : profile.message_index,
  }

class jump():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  distance = {
    'type'          : basetypes.Field.float32,
    'units'         : "m",
  }
  height = {
    'type'          : basetypes.Field.float32,
    'units'         : "m",
  }
  rotations = {
    'type'          : basetypes.Field.uint8,
  }
  hang_time = {
    'type'          : basetypes.Field.float32,
    'units'         : "s",
  }
  score = {
    'type'          : basetypes.Field.float32,
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_speed",
    'scale'         : 1000,
    'units'         : "m/s",
    'bits'          : "16",
  }
  enhanced_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m/s",
  }

class course():
  sport = {
    'type'          : profile.sport,
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  capabilities = {
    'type'          : profile.course_capabilities,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }

class course_point():
  message_index = {
    'type'          : profile.message_index,
  }
  timestamp = {
    'type'          : profile.date_time,
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  type = {
    'type'          : profile.course_point,
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  favorite = {
    'type'          : profile.bool,
  }

class segment_id():
  name = {
    'type'          : basetypes.Field.string,
  }
  uuid = {
    'type'          : basetypes.Field.string,
  }
  sport = {
    'type'          : profile.sport,
  }
  enabled = {
    'type'          : profile.bool,
  }
  user_profile_primary_key = {
    'type'          : basetypes.Field.uint32,
  }
  device_id = {
    'type'          : basetypes.Field.uint32,
  }
  default_race_leader = {
    'type'          : basetypes.Field.uint8,
  }
  delete_status = {
    'type'          : profile.segment_delete_status,
  }
  selection_type = {
    'type'          : profile.segment_selection_type,
  }

class segment_leaderboard_entry():
  message_index = {
    'type'          : profile.message_index,
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  type = {
    'type'          : profile.segment_leaderboard_type,
  }
  group_primary_key = {
    'type'          : basetypes.Field.uint32,
  }
  activity_id = {
    'type'          : basetypes.Field.uint32,
  }
  segment_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  activity_id_string = {
    'type'          : basetypes.Field.string,
  }

class segment_point():
  message_index = {
    'type'          : profile.message_index,
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  altitude = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  leader_time = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }

class segment_lap():
  message_index = {
    'type'          : profile.message_index,
  }
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
  }
  event_type = {
    'type'          : profile.event_type,
  }
  start_time = {
    'type'          : profile.date_time,
  }
  start_position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  start_position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  end_position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  end_position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  total_distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'units'         : "cycles",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  total_fat_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  avg_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  avg_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  max_cadence = {
    'type'          : basetypes.Field.uint8,
    'units'         : "rpm",
  }
  avg_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  max_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  total_ascent = {
    'type'          : basetypes.Field.uint16,
    'units'         : "m",
  }
  total_descent = {
    'type'          : basetypes.Field.uint16,
    'units'         : "m",
  }
  sport = {
    'type'          : profile.sport,
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
  }
  nec_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  nec_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  swc_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  swc_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  name = {
    'type'          : basetypes.Field.string,
  }
  normalized_power = {
    'type'          : basetypes.Field.uint16,
    'units'         : "watts",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance_100,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  total_work = {
    'type'          : basetypes.Field.uint32,
    'units'         : "J",
  }
  avg_altitude = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  max_altitude = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  gps_accuracy = {
    'type'          : basetypes.Field.uint8,
    'units'         : "m",
  }
  avg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  max_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  max_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "%",
  }
  avg_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  max_temperature = {
    'type'          : basetypes.Field.sint8,
    'units'         : "C",
  }
  total_moving_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  avg_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  avg_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  max_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'units'         : "m/s",
  }
  time_in_hr_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_speed_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_cadence_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  time_in_power_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'units'         : "s",
  }
  repetition_num = {
    'type'          : basetypes.Field.uint16,
  }
  min_altitude = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  min_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  active_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  wkt_step_index = {
    'type'          : profile.message_index,
  }
  sport_event = {
    'type'          : profile.sport_event,
  }
  avg_left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  avg_combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'units'         : "percent",
  }
  status = {
    'type'          : profile.segment_lap_status,
  }
  uuid = {
    'type'          : basetypes.Field.string,
  }
  avg_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  max_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "rpm",
  }
  total_fractional_cycles = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'units'         : "cycles",
  }
  front_gear_shift_count = {
    'type'          : basetypes.Field.uint16,
  }
  rear_gear_shift_count = {
    'type'          : basetypes.Field.uint16,
  }
  time_standing = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  stand_count = {
    'type'          : basetypes.Field.uint16,
  }
  avg_left_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  avg_right_pco = {
    'type'          : basetypes.Field.sint8,
    'units'         : "mm",
  }
  avg_left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : "0.7111111",
    'units'         : "degrees",
  }
  avg_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "watts",
  }
  max_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'units'         : "watts",
  }
  avg_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "rpm",
  }
  max_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "rpm",
  }
  manufacturer = {
    'type'          : profile.manufacturer,
  }
  total_grit = {
    'type'          : basetypes.Field.float32,
    'units'         : "kGrit",
  }
  total_flow = {
    'type'          : basetypes.Field.float32,
    'units'         : "Flow",
  }
  avg_grit = {
    'type'          : basetypes.Field.float32,
    'units'         : "kGrit",
  }
  avg_flow = {
    'type'          : basetypes.Field.float32,
    'units'         : "Flow",
  }

class segment_file():
  message_index = {
    'type'          : profile.message_index,
  }
  file_uuid = {
    'type'          : basetypes.Field.string,
  }
  enabled = {
    'type'          : profile.bool,
  }
  user_profile_primary_key = {
    'type'          : basetypes.Field.uint32,
  }
  leader_type = {
    'type'          : profile.segment_leaderboard_type,
    'array'         : "[N]",
  }
  leader_group_primary_key = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
  }
  leader_activity_id = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
  }
  leader_activity_id_string = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
  }
  default_race_leader = {
    'type'          : basetypes.Field.uint8,
  }

class workout():
  sport = {
    'type'          : profile.sport,
  }
  capabilities = {
    'type'          : profile.workout_capabilities,
  }
  num_valid_steps = {
    'type'          : basetypes.Field.uint16,
  }
  wkt_name = {
    'type'          : basetypes.Field.string,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  pool_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m",
  }
  pool_length_unit = {
    'type'          : profile.display_measure,
  }

class workout_session():
  message_index = {
    'type'          : profile.message_index,
  }
  sport = {
    'type'          : profile.sport,
  }
  sub_sport = {
    'type'          : profile.sub_sport,
  }
  num_valid_steps = {
    'type'          : basetypes.Field.uint16,
  }
  first_step_index = {
    'type'          : basetypes.Field.uint16,
  }
  pool_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "m",
  }
  pool_length_unit = {
    'type'          : profile.display_measure,
  }

class workout_step():
  message_index = {
    'type'          : profile.message_index,
  }
  wkt_step_name = {
    'type'          : basetypes.Field.string,
  }
  duration_type = {
    'type'          : profile.wkt_step_duration,
  }
  duration_value = {
    'type'          : basetypes.Field.uint32,
  }
  target_type = {
    'type'          : profile.wkt_step_target,
  }
  target_value = {
    'type'          : basetypes.Field.uint32,
  }
  custom_target_value_low = {
    'type'          : basetypes.Field.uint32,
  }
  custom_target_value_high = {
    'type'          : basetypes.Field.uint32,
  }
  intensity = {
    'type'          : profile.intensity,
  }
  notes = {
    'type'          : basetypes.Field.string,
  }
  equipment = {
    'type'          : profile.workout_equipment,
  }
  exercise_category = {
    'type'          : profile.exercise_category,
  }
  exercise_name = {
    'type'          : basetypes.Field.uint16,
  }
  exercise_weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "kg",
  }
  weight_display_unit = {
    'type'          : profile.fit_base_unit,
  }

class exercise_title():
  message_index = {
    'type'          : profile.message_index,
  }
  exercise_category = {
    'type'          : profile.exercise_category,
  }
  exercise_name = {
    'type'          : basetypes.Field.uint16,
  }
  wkt_step_name = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
  }

class schedule():
  manufacturer = {
    'type'          : profile.manufacturer,
  }
  product = {
    'type'          : basetypes.Field.uint16,
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
  }
  time_created = {
    'type'          : profile.date_time,
  }
  completed = {
    'type'          : profile.bool,
  }
  type = {
    'type'          : profile.schedule,
  }
  scheduled_time = {
    'type'          : profile.local_date_time,
  }

class totals():
  message_index = {
    'type'          : profile.message_index,
  }
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  timer_time = {
    'type'          : basetypes.Field.uint32,
    'units'         : "s",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'units'         : "m",
  }
  calories = {
    'type'          : basetypes.Field.uint32,
    'units'         : "kcal",
  }
  sport = {
    'type'          : profile.sport,
  }
  elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'units'         : "s",
  }
  sessions = {
    'type'          : basetypes.Field.uint16,
  }
  active_time = {
    'type'          : basetypes.Field.uint32,
    'units'         : "s",
  }
  sport_index = {
    'type'          : basetypes.Field.uint8,
  }

class weight_scale():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  weight = {
    'type'          : profile.weight,
    'scale'         : 100,
    'units'         : "kg",
  }
  percent_fat = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "%",
  }
  percent_hydration = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "%",
  }
  visceral_fat_mass = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "kg",
  }
  bone_mass = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "kg",
  }
  muscle_mass = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'units'         : "kg",
  }
  basal_met = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 4,
    'units'         : "kcal/day",
  }
  physique_rating = {
    'type'          : basetypes.Field.uint8,
  }
  active_met = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 4,
    'units'         : "kcal/day",
  }
  metabolic_age = {
    'type'          : basetypes.Field.uint8,
    'units'         : "years",
  }
  visceral_fat_rating = {
    'type'          : basetypes.Field.uint8,
  }
  user_profile_index = {
    'type'          : profile.message_index,
  }

class blood_pressure():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  systolic_pressure = {
    'type'          : basetypes.Field.uint16,
    'units'         : "mmHg",
  }
  diastolic_pressure = {
    'type'          : basetypes.Field.uint16,
    'units'         : "mmHg",
  }
  mean_arterial_pressure = {
    'type'          : basetypes.Field.uint16,
    'units'         : "mmHg",
  }
  map_3_sample_mean = {
    'type'          : basetypes.Field.uint16,
    'units'         : "mmHg",
  }
  map_morning_values = {
    'type'          : basetypes.Field.uint16,
    'units'         : "mmHg",
  }
  map_evening_values = {
    'type'          : basetypes.Field.uint16,
    'units'         : "mmHg",
  }
  heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  heart_rate_type = {
    'type'          : profile.hr_type,
  }
  status = {
    'type'          : profile.bp_status,
  }
  user_profile_index = {
    'type'          : profile.message_index,
  }

class monitoring_info():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
    'units'         : "s",
  }
  activity_type = {
    'type'          : profile.activity_type,
    'array'         : "[N]",
  }
  cycles_to_distance = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 5000,
    'units'         : "m/cycle",
  }
  cycles_to_calories = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 5000,
    'units'         : "kcal/cycle",
  }
  resting_metabolic_rate = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal / day",
  }

class monitoring():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  device_index = {
    'type'          : profile.device_index,
  }
  calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'units'         : "m",
  }
  cycles = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 2,
    'units'         : "cycles",
  }
  active_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }
  activity_type = {
    'type'          : profile.activity_type,
  }
  activity_subtype = {
    'type'          : profile.activity_subtype,
  }
  activity_level = {
    'type'          : profile.activity_level,
  }
  distance_16 = {
    'type'          : basetypes.Field.uint16,
    'units'         : "100 * m",
  }
  cycles_16 = {
    'type'          : basetypes.Field.uint16,
    'units'         : "2 * cycles (steps)",
  }
  active_time_16 = {
    'type'          : basetypes.Field.uint16,
    'units'         : "s",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
  }
  temperature = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "C",
  }
  temperature_min = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "C",
  }
  temperature_max = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'units'         : "C",
  }
  activity_time = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[8]",
    'units'         : "minutes",
  }
  active_calories = {
    'type'          : basetypes.Field.uint16,
    'units'         : "kcal",
  }
  current_activity_type_intensity = {
    'type'          : basetypes.Field.byte,
    'components'    : "activity_type,intensity",
    'bits'          : "5,3",
  }
  timestamp_min_8 = {
    'type'          : basetypes.Field.uint8,
    'units'         : "min",
  }
  timestamp_16 = {
    'type'          : basetypes.Field.uint16,
    'units'         : "s",
  }
  heart_rate = {
    'type'          : basetypes.Field.uint8,
    'units'         : "bpm",
  }
  intensity = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
  }
  duration_min = {
    'type'          : basetypes.Field.uint16,
    'units'         : "min",
  }
  duration = {
    'type'          : basetypes.Field.uint32,
    'units'         : "s",
  }
  ascent = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  descent = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  moderate_activity_minutes = {
    'type'          : basetypes.Field.uint16,
    'units'         : "minutes",
  }
  vigorous_activity_minutes = {
    'type'          : basetypes.Field.uint16,
    'units'         : "minutes",
  }

class hr():
  timestamp = {
    'type'          : profile.date_time,
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'units'         : "s",
  }
  time256 = {
    'type'          : basetypes.Field.uint8,
    'components'    : "fractional_timestamp",
    'scale'         : 256,
    'units'         : "s",
    'bits'          : "8",
  }
  filtered_bpm = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'units'         : "bpm",
  }
  event_timestamp = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1024,
    'units'         : "s",
  }
  event_timestamp_12 = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'components'    : "event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp ",
    'scale'         : "1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024",
    'units'         : "s",
    'bits'          : "12, 12, 12, 12, 12, 12, 12, 12, 12, 12",
    'accumulate'    : "1, 1, 1, 1, 1, 1, 1, 1, 1, 1",
  }

class stress_level():
  stress_level_value = {
    'type'          : basetypes.Field.sint16,
  }
  stress_level_time = {
    'type'          : profile.date_time,
    'units'         : "s",
  }

class memo_glob():
  part_index = {
    'type'          : basetypes.Field.uint32,
  }
  memo = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
  }
  message_number = {
    'type'          : basetypes.Field.uint16,
  }
  message_index = {
    'type'          : profile.message_index,
  }

class ant_channel_id():
  channel_number = {
    'type'          : basetypes.Field.uint8,
  }
  device_type = {
    'type'          : basetypes.Field.uint8z,
  }
  device_number = {
    'type'          : basetypes.Field.uint16z,
  }
  transmission_type = {
    'type'          : basetypes.Field.uint8z,
  }
  device_index = {
    'type'          : profile.device_index,
  }

class ant_rx():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'units'         : "s",
  }
  mesg_id = {
    'type'          : basetypes.Field.byte,
  }
  mesg_data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'components'    : "channel_number,data,data,data,data,data,data,data,data",
    'bits'          : "8,8,8,8,8,8,8,8,8",
  }
  channel_number = {
    'type'          : basetypes.Field.uint8,
  }
  data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
  }

class ant_tx():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'units'         : "s",
  }
  mesg_id = {
    'type'          : basetypes.Field.byte,
  }
  mesg_data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'components'    : "channel_number,data,data,data,data,data,data,data,data",
    'bits'          : "8,8,8,8,8,8,8,8,8",
  }
  channel_number = {
    'type'          : basetypes.Field.uint8,
  }
  data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
  }

class exd_screen_configuration():
  screen_index = {
    'type'          : basetypes.Field.uint8,
  }
  field_count = {
    'type'          : basetypes.Field.uint8,
  }
  layout = {
    'type'          : profile.exd_layout,
  }
  screen_enabled = {
    'type'          : profile.bool,
  }

class exd_data_field_configuration():
  screen_index = {
    'type'          : basetypes.Field.uint8,
  }
  concept_field = {
    'type'          : basetypes.Field.byte,
    'components'    : "field_id,concept_count",
    'bits'          : "4,4",
  }
  field_id = {
    'type'          : basetypes.Field.uint8,
  }
  concept_count = {
    'type'          : basetypes.Field.uint8,
  }
  display_type = {
    'type'          : profile.exd_display_type,
  }
  title = {
    'type'          : basetypes.Field.string,
    'array'         : "[32]",
  }

class exd_data_concept_configuration():
  screen_index = {
    'type'          : basetypes.Field.uint8,
  }
  concept_field = {
    'type'          : basetypes.Field.byte,
    'components'    : "field_id,concept_index",
    'bits'          : "4,4",
  }
  field_id = {
    'type'          : basetypes.Field.uint8,
  }
  concept_index = {
    'type'          : basetypes.Field.uint8,
  }
  data_page = {
    'type'          : basetypes.Field.uint8,
  }
  concept_key = {
    'type'          : basetypes.Field.uint8,
  }
  scaling = {
    'type'          : basetypes.Field.uint8,
  }
  data_units = {
    'type'          : profile.exd_data_units,
  }
  qualifier = {
    'type'          : profile.exd_qualifiers,
  }
  descriptor = {
    'type'          : profile.exd_descriptors,
  }
  is_signed = {
    'type'          : profile.bool,
  }

class field_description():
  developer_data_index = {
    'type'          : basetypes.Field.uint8,
  }
  field_definition_number = {
    'type'          : basetypes.Field.uint8,
  }
  fit_base_type_id = {
    'type'          : profile.fit_base_type,
  }
  field_name = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
  }
  array = {
    'type'          : basetypes.Field.uint8,
  }
  components = {
    'type'          : basetypes.Field.string,
  }
  scale = {
    'type'          : basetypes.Field.uint8,
  }
  offset = {
    'type'          : basetypes.Field.sint8,
  }
  units = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
  }
  bits = {
    'type'          : basetypes.Field.string,
  }
  accumulate = {
    'type'          : basetypes.Field.string,
  }
  fit_base_unit_id = {
    'type'          : profile.fit_base_unit,
  }
  native_mesg_num = {
    'type'          : profile.mesg_num,
  }
  native_field_num = {
    'type'          : basetypes.Field.uint8,
  }

class developer_data_id():
  developer_id = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
  }
  application_id = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
  }
  manufacturer_id = {
    'type'          : profile.manufacturer,
  }
  developer_data_index = {
    'type'          : basetypes.Field.uint8,
  }
  application_version = {
    'type'          : basetypes.Field.uint32,
  }

class dive_summary():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  reference_mesg = {
    'type'          : profile.mesg_num,
  }
  reference_index = {
    'type'          : profile.message_index,
  }
  avg_depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  max_depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "m",
  }
  surface_interval = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'units'         : "s",
  }
  start_cns = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'units'         : "percent",
  }
  end_cns = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'units'         : "percent",
  }
  start_n2 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'units'         : "percent",
  }
  end_n2 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'units'         : "percent",
  }
  o2_toxicity = {
    'type'          : basetypes.Field.uint16,
    'units'         : "OTUs",
  }
  dive_number = {
    'type'          : basetypes.Field.uint32,
  }
  bottom_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'units'         : "s",
  }

class climb_pro():
  timestamp = {
    'type'          : profile.date_time,
    'units'         : "s",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'units'         : "semicircles",
  }
  climb_pro_event = {
    'type'          : profile.climb_pro_event,
  }
  climb_number = {
    'type'          : basetypes.Field.uint16,
  }
  climb_category = {
    'type'          : basetypes.Field.uint8,
  }
  current_dist = {
    'type'          : basetypes.Field.float32,
    'units'         : "m",
  }
