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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  manufacturer = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_created = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  number = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product_name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class file_creator():
  software_version = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  hardware_version = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class timestamp_correlation():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'offset'        : 0,
    'units'         : "s",
  }
  system_timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  fractional_system_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'offset'        : 0,
    'units'         : "s",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  system_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }

class software():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  version = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "",
  }
  part_number = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class slave_device():
  manufacturer = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class capabilities():
  languages = {
    'type'          : basetypes.Field.uint8z,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sports = {
    'type'          : profile.sport_bits_0,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  workouts_supported = {
    'type'          : profile.workout_capabilities,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  connectivity_supported = {
    'type'          : profile.connectivity_capabilities,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class file_capabilities():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.file,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  flags = {
    'type'          : profile.file_flags,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  directory = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  max_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  max_size = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bytes",
  }

class mesg_capabilities():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  file = {
    'type'          : profile.file,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  mesg_num = {
    'type'          : profile.mesg_num,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  count_type = {
    'type'          : profile.mesg_count,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class field_capabilities():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  file = {
    'type'          : profile.file,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  mesg_num = {
    'type'          : profile.mesg_num,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  field_num = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class device_settings():
  active_time_zone = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  utc_offset = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_offset = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  time_mode = {
    'type'          : profile.time_mode,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_zone_offset = {
    'type'          : basetypes.Field.sint8,
    'array'         : "[N]",
    'scale'         : 4,
    'offset'        : 0,
    'units'         : "hr",
  }
  backlight_mode = {
    'type'          : profile.backlight_mode,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  activity_tracker_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  clock_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  pages_enabled = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  move_alert_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  date_mode = {
    'type'          : profile.date_mode,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  display_orientation = {
    'type'          : profile.display_orientation,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  mounting_side = {
    'type'          : profile.side,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  default_page = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  autosync_min_steps = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "steps",
  }
  autosync_min_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "minutes",
  }
  lactate_threshold_autodetect_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ble_auto_upload_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  auto_sync_frequency = {
    'type'          : profile.auto_sync_frequency,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  auto_activity_detect = {
    'type'          : profile.auto_activity_detect,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  number_of_screens = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  smart_notification_display_orientation = {
    'type'          : profile.display_orientation,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  tap_interface = {
    'type'          : profile.switch,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  tap_sensitivity = {
    'type'          : profile.tap_sensitivity,
    'scale'         : 1,
    'offset'        : 1,
    'units'         : "",
  }

class user_profile():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  friendly_name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  gender = {
    'type'          : profile.gender,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  age = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "years",
  }
  height = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "kg",
  }
  language = {
    'type'          : profile.language,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  elev_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  weight_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  resting_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  default_max_running_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  default_max_biking_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  default_max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  hr_setting = {
    'type'          : profile.display_heart,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  speed_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  dist_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  power_setting = {
    'type'          : profile.display_power,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  activity_class = {
    'type'          : profile.activity_class,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  position_setting = {
    'type'          : profile.display_position,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  temperature_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  local_id = {
    'type'          : profile.user_local_id,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  global_id = {
    'type'          : basetypes.Field.byte,
    'array'         : "[6]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  wake_time = {
    'type'          : profile.localtime_into_day,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sleep_time = {
    'type'          : profile.localtime_into_day,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  height_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  user_running_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  user_walking_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  depth_setting = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  dive_count = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class hrm_profile():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  hrm_ant_id = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  log_hrv = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  hrm_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class sdm_profile():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sdm_ant_id = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sdm_cal_factor = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  odometer = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  speed_source = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sdm_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  odometer_rollover = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class bike_profile():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  odometer = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  bike_spd_ant_id = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_cad_ant_id = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_spdcad_ant_id = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_power_ant_id = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  custom_wheelsize = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  auto_wheelsize = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  bike_weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "kg",
  }
  power_cal_factor = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  auto_wheel_cal = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  auto_power_zero = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  id = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  spd_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  cad_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  spdcad_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  power_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  crank_length = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "mm",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_spd_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_cad_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_spdcad_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bike_power_ant_id_trans_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  odometer_rollover = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  front_gear_num = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  front_gear = {
    'type'          : basetypes.Field.uint8z,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  rear_gear_num = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  rear_gear = {
    'type'          : basetypes.Field.uint8z,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  shimano_di2_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class connectivity():
  bluetooth_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bluetooth_le_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ant_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  live_tracking_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  weather_conditions_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  weather_alerts_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  auto_activity_upload_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  course_download_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  workout_download_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  gps_ephemeris_download_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  incident_detection_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  grouptrack_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class watchface_settings():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  mode = {
    'type'          : profile.watchface_mode,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  layout = {
    'type'          : basetypes.Field.byte,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class ohr_settings():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  enabled = {
    'type'          : profile.switch,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class zones_target():
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  threshold_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  functional_threshold_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  hr_calc_type = {
    'type'          : profile.hr_zone_calc,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  pwr_calc_type = {
    'type'          : profile.pwr_zone_calc,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class sport():
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class hr_zone():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  high_bpm = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class speed_zone():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  high_value = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class cadence_zone():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  high_value = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class power_zone():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  high_value = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class met_zone():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  high_bpm = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "kcal / min",
  }
  fat_calories = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "kcal / min",
  }

class dive_settings():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  model = {
    'type'          : profile.tissue_model_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  gf_low = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  gf_high = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  water_type = {
    'type'          : profile.water_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  water_density = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kg/m^3",
  }
  po2_warn = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  po2_critical = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  po2_deco = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  safety_stop_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bottom_depth = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bottom_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  apnea_countdown_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  apnea_countdown_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  backlight_mode = {
    'type'          : profile.dive_backlight_mode,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  backlight_brightness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  backlight_timeout = {
    'type'          : profile.backlight_timeout,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  repeat_dive_interval = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  safety_stop_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  heart_rate_source_type = {
    'type'          : profile.source_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  heart_rate_source = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class dive_alarm():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  time = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  alarm_type = {
    'type'          : profile.dive_alarm_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sound = {
    'type'          : profile.tone,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  dive_types = {
    'type'          : profile.sub_sport,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class dive_gas():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  helium_content = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  oxygen_content = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  status = {
    'type'          : profile.dive_gas_status,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class goal():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_date = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  end_date = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.goal,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  value = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  repeat = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  target_value = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  recurrence = {
    'type'          : profile.goal_recurrence,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  recurrence_value = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  source = {
    'type'          : profile.goal_source,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class activity():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  num_sessions = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.activity,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event = {
    'type'          : profile.event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_type = {
    'type'          : profile.event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class session():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_type = {
    'type'          : profile.event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  start_position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "cycles",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  total_fat_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_avg_speed",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  max_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_max_speed",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  avg_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  avg_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  avg_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  total_ascent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  total_descent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  total_training_effect = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "",
  }
  first_lap_index = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  num_laps = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  trigger = {
    'type'          : profile.session_trigger,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  nec_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  nec_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  swc_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  swc_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  normalized_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  training_stress_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "tss",
  }
  intensity_factor = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "if",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance_100,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_stroke_count = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "strokes/lap",
  }
  avg_stroke_distance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  swim_stroke = {
    'type'          : profile.swim_stroke,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "swim_stroke",
  }
  pool_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  threshold_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  pool_length_unit = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  num_active_lengths = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "lengths",
  }
  total_work = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  avg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  max_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  max_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  max_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  total_moving_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  avg_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  avg_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  min_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  time_in_hr_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_speed_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_cadence_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_power_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  avg_lap_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  best_lap_index = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  opponent_name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  stroke_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  zone_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  max_ball_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m/s",
  }
  avg_ball_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m/s",
  }
  avg_vertical_oscillation = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_stance_time_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_stance_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "ms",
  }
  avg_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  total_fractional_cycles = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "cycles",
  }
  avg_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  min_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  max_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  avg_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  min_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  max_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  sport_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_standing = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  stand_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_left_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_right_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  avg_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  enhanced_avg_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  enhanced_max_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_lev_motor_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  lev_battery_consumption = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_vertical_ratio = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_stance_time_balance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "mm",
  }
  total_anaerobic_training_effect = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "",
  }
  avg_vam = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  total_grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kGrit",
  }
  total_flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Flow",
  }
  jump_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kGrit",
  }
  avg_flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Flow",
  }

class lap():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_type = {
    'type'          : profile.event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  start_position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  end_position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  end_position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "cycles",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  total_fat_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_avg_speed",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  max_speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_max_speed",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  avg_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  avg_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  avg_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  total_ascent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  total_descent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  intensity = {
    'type'          : profile.intensity,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  lap_trigger = {
    'type'          : profile.lap_trigger,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  num_lengths = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "lengths",
  }
  normalized_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance_100,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  first_length_index = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_stroke_distance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  swim_stroke = {
    'type'          : profile.swim_stroke,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  num_active_lengths = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "lengths",
  }
  total_work = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  avg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  max_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  max_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  max_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  total_moving_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  avg_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  avg_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  time_in_hr_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_speed_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_cadence_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_power_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  repetition_num = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  wkt_step_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  stroke_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  zone_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  avg_vertical_oscillation = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_stance_time_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_stance_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "ms",
  }
  avg_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  total_fractional_cycles = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "cycles",
  }
  player_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  min_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  max_total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  avg_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  min_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  max_saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  time_standing = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  stand_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_left_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_right_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  avg_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  enhanced_avg_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  enhanced_max_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_lev_motor_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  lev_battery_consumption = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_vertical_ratio = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_stance_time_balance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_vam = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  total_grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kGrit",
  }
  total_flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Flow",
  }
  jump_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kGrit",
  }
  avg_flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Flow",
  }

class length():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event = {
    'type'          : profile.event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_type = {
    'type'          : profile.event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_strokes = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "strokes",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  swim_stroke = {
    'type'          : profile.swim_stroke,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "swim_stroke",
  }
  avg_swimming_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "strokes/min",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  length_type = {
    'type'          : profile.length_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  player_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  stroke_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  zone_count = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }

class record():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_speed",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  compressed_speed_distance = {
    'type'          : basetypes.Field.byte,
    'array'         : "[3]",
    'components'    : "speed, distance",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m/s, m",
    'bits'          : "12, 12",
    'accumulate'    : "0, 1",
  }
  grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  resistance = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_from_course = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  cycle_length = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  speed_1s = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 16,
    'offset'        : 0,
    'units'         : "m/s",
  }
  cycles = {
    'type'          : basetypes.Field.uint8,
    'components'    : "total_cycles",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "cycles",
    'bits'          : "8",
    'accumulate'    : "1",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "cycles",
  }
  compressed_accumulated_power = {
    'type'          : basetypes.Field.uint16,
    'components'    : "accumulated_power",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
    'bits'          : "16",
    'accumulate'    : "1",
  }
  accumulated_power = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  gps_accuracy = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  vertical_oscillation = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "mm",
  }
  stance_time_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  stance_time = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "ms",
  }
  activity_type = {
    'type'          : profile.activity_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  time128 = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "s",
  }
  stroke_type = {
    'type'          : profile.stroke_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  zone = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ball_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m/s",
  }
  cadence256 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 256,
    'offset'        : 0,
    'units'         : "rpm",
  }
  fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  total_hemoglobin_conc = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  total_hemoglobin_conc_min = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  total_hemoglobin_conc_max = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "g/dL",
  }
  saturated_hemoglobin_percent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  saturated_hemoglobin_percent_min = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  saturated_hemoglobin_percent_max = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "%",
  }
  device_index = {
    'type'          : profile.device_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  left_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  right_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  enhanced_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
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
    'offset'        : 0,
    'units'         : "percent",
  }
  motor_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  vertical_ratio = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  stance_time_balance = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "percent",
  }
  step_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "mm",
  }
  absolute_pressure = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Pa",
  }
  depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  next_stop_depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  next_stop_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  time_to_surface = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  ndl_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  cns_load = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  n2_load = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ebike_travel_range = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "km",
  }
  ebike_battery_level = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  ebike_assist_mode = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "depends on sensor",
  }
  ebike_assist_level_percent = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }

class event():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_type = {
    'type'          : profile.event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  data16 = {
    'type'          : basetypes.Field.uint16,
    'components'    : "data",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
    'bits'          : "16",
  }
  data = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  opponent_score = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  front_gear_num = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  front_gear = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  rear_gear_num = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  rear_gear = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  device_index = {
    'type'          : profile.device_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  radar_threat_level_max = {
    'type'          : profile.radar_threat_level_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  radar_threat_count = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class device_info():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  device_index = {
    'type'          : profile.device_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  device_type = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  manufacturer = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  software_version = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "",
  }
  hardware_version = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  cum_operating_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  battery_voltage = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 256,
    'offset'        : 0,
    'units'         : "V",
  }
  battery_status = {
    'type'          : profile.battery_status,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sensor_position = {
    'type'          : profile.body_location,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  descriptor = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ant_transmission_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ant_device_number = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  ant_network = {
    'type'          : profile.ant_network,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  source_type = {
    'type'          : profile.source_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product_name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class training_file():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.file,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  manufacturer = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_created = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class hrv():
  time = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }

class weather_conditions():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  weather_report = {
    'type'          : profile.weather_report,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  condition = {
    'type'          : profile.weather_status,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  wind_direction = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  wind_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  precipitation_probability = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  temperature_feels_like = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  relative_humidity = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  location = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  observed_at_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  observed_location_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  observed_location_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  day_of_week = {
    'type'          : profile.day_of_week,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  high_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  low_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }

class weather_alert():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  report_id = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  issue_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  expire_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  severity = {
    'type'          : profile.weather_severity,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.weather_severe_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class gps_metadata():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
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
    'offset'        : 0,
    'units'         : "m/s",
  }
  heading = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "degrees",
  }
  utc_timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  velocity = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[3]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m/s",
  }

class camera_event():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  camera_event_type = {
    'type'          : profile.camera_event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  camera_file_uuid = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  camera_orientation = {
    'type'          : profile.camera_orientation_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class gyroscope_data():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  gyro_x = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  gyro_y = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  gyro_z = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  calibrated_gyro_x = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "deg/s",
  }
  calibrated_gyro_y = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "deg/s",
  }
  calibrated_gyro_z = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "deg/s",
  }

class accelerometer_data():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  accel_x = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  accel_y = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  accel_z = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  calibrated_accel_x = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "g",
  }
  calibrated_accel_y = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "g",
  }
  calibrated_accel_z = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "g",
  }
  compressed_calibrated_accel_x = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mG",
  }
  compressed_calibrated_accel_y = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mG",
  }
  compressed_calibrated_accel_z = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mG",
  }

class magnetometer_data():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  mag_x = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  mag_y = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  mag_z = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  calibrated_mag_x = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "G",
  }
  calibrated_mag_y = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "G",
  }
  calibrated_mag_z = {
    'type'          : basetypes.Field.float32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "G",
  }

class barometer_data():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  sample_time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  baro_pres = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Pa",
  }

class three_d_sensor_calibration():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  sensor_type = {
    'type'          : profile.sensor_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  calibration_factor = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  calibration_divisor = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  level_shift = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  offset_cal = {
    'type'          : basetypes.Field.sint32,
    'array'         : "[3]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  orientation_matrix = {
    'type'          : basetypes.Field.sint32,
    'array'         : "[9]",
    'scale'         : 65535,
    'offset'        : 0,
    'units'         : "",
  }

class one_d_sensor_calibration():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  sensor_type = {
    'type'          : profile.sensor_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  calibration_factor = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  calibration_divisor = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "counts",
  }
  level_shift = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  offset_cal = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class video_frame():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  frame_number = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class obdii_data():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  time_offset = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  pid = {
    'type'          : basetypes.Field.byte,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  raw_data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  pid_data_size = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  system_time = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }

class nmea_sentence():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  sentence = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class aviation_attitude():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  system_time = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  pitch = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "radians",
  }
  roll = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "radians",
  }
  accel_lateral = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m/s^2",
  }
  accel_normal = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m/s^2",
  }
  turn_rate = {
    'type'          : basetypes.Field.sint16,
    'array'         : "[N]",
    'scale'         : 1024,
    'offset'        : 0,
    'units'         : "radians/second",
  }
  stage = {
    'type'          : profile.attitude_stage,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  attitude_stage_complete = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "%",
  }
  track = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "radians",
  }
  validity = {
    'type'          : profile.attitude_validity,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class video():
  url = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  hosting_provider = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  duration = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }

class video_title():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  message_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  text = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class video_description():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  message_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  text = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class video_clip():
  clip_number = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  end_timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  end_timestamp_ms = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  clip_start = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }
  clip_end = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "ms",
  }

class set():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  duration = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  repetitions = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 16,
    'offset'        : 0,
    'units'         : "kg",
  }
  set_type = {
    'type'          : profile.set_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  category = {
    'type'          : profile.exercise_category,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  category_subtype = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  weight_display_unit = {
    'type'          : profile.fit_base_unit,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  wkt_step_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class jump():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  distance = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  height = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  rotations = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  hang_time = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  score = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  speed = {
    'type'          : basetypes.Field.uint16,
    'components'    : "enhanced_speed",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
    'bits'          : "16",
  }
  enhanced_speed = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }

class course():
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  capabilities = {
    'type'          : profile.course_capabilities,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class course_point():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  type = {
    'type'          : profile.course_point,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  favorite = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class segment_id():
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  uuid = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  user_profile_primary_key = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  device_id = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  default_race_leader = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  delete_status = {
    'type'          : profile.segment_delete_status,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  selection_type = {
    'type'          : profile.segment_selection_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class segment_leaderboard_entry():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.segment_leaderboard_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  group_primary_key = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  activity_id = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  segment_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  activity_id_string = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class segment_point():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
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
    'offset'        : 0,
    'units'         : "s",
  }

class segment_lap():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  event = {
    'type'          : profile.event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_type = {
    'type'          : profile.event_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  start_position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  start_position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  end_position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  end_position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  total_elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  total_distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  total_cycles = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "cycles",
  }
  total_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  total_fat_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  avg_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_speed = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  avg_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  max_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  avg_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  avg_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  total_ascent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  total_descent = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  event_group = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  nec_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  nec_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  swc_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  swc_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  normalized_power = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  left_right_balance = {
    'type'          : profile.left_right_balance_100,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  total_work = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
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
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  avg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  max_pos_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  max_neg_grade = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  avg_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  max_temperature = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "C",
  }
  total_moving_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  avg_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  avg_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_pos_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  max_neg_vertical_speed = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m/s",
  }
  time_in_hr_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_speed_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_cadence_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  time_in_power_zone = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  repetition_num = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  min_altitude = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 5,
    'offset'        : 500,
    'units'         : "m",
  }
  min_heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  active_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  wkt_step_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sport_event = {
    'type'          : profile.sport_event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_left_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_right_torque_effectiveness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_left_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_right_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  avg_combined_pedal_smoothness = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "percent",
  }
  status = {
    'type'          : profile.segment_lap_status,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  uuid = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_fractional_cadence = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "rpm",
  }
  total_fractional_cycles = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 128,
    'offset'        : 0,
    'units'         : "cycles",
  }
  front_gear_shift_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  rear_gear_shift_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_standing = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  stand_count = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_left_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_right_pco = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mm",
  }
  avg_left_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_left_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_right_power_phase = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_right_power_phase_peak = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "degrees",
  }
  avg_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  max_power_position = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "watts",
  }
  avg_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  max_cadence_position = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "rpm",
  }
  manufacturer = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  total_grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kGrit",
  }
  total_flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Flow",
  }
  avg_grit = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kGrit",
  }
  avg_flow = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "Flow",
  }

class segment_file():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  file_uuid = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  user_profile_primary_key = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  leader_type = {
    'type'          : profile.segment_leaderboard_type,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  leader_group_primary_key = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  leader_activity_id = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  leader_activity_id_string = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  default_race_leader = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class workout():
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  capabilities = {
    'type'          : profile.workout_capabilities,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  num_valid_steps = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  wkt_name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  pool_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  pool_length_unit = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class workout_session():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  sub_sport = {
    'type'          : profile.sub_sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  num_valid_steps = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  first_step_index = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  pool_length = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  pool_length_unit = {
    'type'          : profile.display_measure,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class workout_step():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  wkt_step_name = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  duration_type = {
    'type'          : profile.wkt_step_duration,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  duration_value = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  target_type = {
    'type'          : profile.wkt_step_target,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  target_value = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  custom_target_value_low = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  custom_target_value_high = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  intensity = {
    'type'          : profile.intensity,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  notes = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  equipment = {
    'type'          : profile.workout_equipment,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  exercise_category = {
    'type'          : profile.exercise_category,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  exercise_name = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  exercise_weight = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "kg",
  }
  weight_display_unit = {
    'type'          : profile.fit_base_unit,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class exercise_title():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  exercise_category = {
    'type'          : profile.exercise_category,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  exercise_name = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  wkt_step_name = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class schedule():
  manufacturer = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  product = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  serial_number = {
    'type'          : basetypes.Field.uint32z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  time_created = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  completed = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  type = {
    'type'          : profile.schedule,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  scheduled_time = {
    'type'          : profile.local_date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class totals():
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  timer_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
  calories = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  sport = {
    'type'          : profile.sport,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  elapsed_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  sessions = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  active_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  sport_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class weight_scale():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  weight = {
    'type'          : profile.weight,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "kg",
  }
  percent_fat = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  percent_hydration = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "%",
  }
  visceral_fat_mass = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "kg",
  }
  bone_mass = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "kg",
  }
  muscle_mass = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "kg",
  }
  basal_met = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 4,
    'offset'        : 0,
    'units'         : "kcal/day",
  }
  physique_rating = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  active_met = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 4,
    'offset'        : 0,
    'units'         : "kcal/day",
  }
  metabolic_age = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "years",
  }
  visceral_fat_rating = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  user_profile_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class blood_pressure():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  systolic_pressure = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mmHg",
  }
  diastolic_pressure = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mmHg",
  }
  mean_arterial_pressure = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mmHg",
  }
  map_3_sample_mean = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mmHg",
  }
  map_morning_values = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mmHg",
  }
  map_evening_values = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "mmHg",
  }
  heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  heart_rate_type = {
    'type'          : profile.hr_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  status = {
    'type'          : profile.bp_status,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  user_profile_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class monitoring_info():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  activity_type = {
    'type'          : profile.activity_type,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  cycles_to_distance = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 5000,
    'offset'        : 0,
    'units'         : "m/cycle",
  }
  cycles_to_calories = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[N]",
    'scale'         : 5000,
    'offset'        : 0,
    'units'         : "kcal/cycle",
  }
  resting_metabolic_rate = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal / day",
  }

class monitoring():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  device_index = {
    'type'          : profile.device_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  distance = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "m",
  }
  cycles = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 2,
    'offset'        : 0,
    'units'         : "cycles",
  }
  active_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }
  activity_type = {
    'type'          : profile.activity_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  activity_subtype = {
    'type'          : profile.activity_subtype,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  activity_level = {
    'type'          : profile.activity_level,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  distance_16 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "100 * m",
  }
  cycles_16 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "2 * cycles (steps)",
  }
  active_time_16 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  local_timestamp = {
    'type'          : profile.local_date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  temperature = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "C",
  }
  temperature_min = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "C",
  }
  temperature_max = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 100,
    'offset'        : 0,
    'units'         : "C",
  }
  activity_time = {
    'type'          : basetypes.Field.uint16,
    'array'         : "[8]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "minutes",
  }
  active_calories = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "kcal",
  }
  current_activity_type_intensity = {
    'type'          : basetypes.Field.byte,
    'components'    : "activity_type,intensity",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
    'bits'          : "5,3",
  }
  timestamp_min_8 = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "min",
  }
  timestamp_16 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  heart_rate = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  intensity = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 10,
    'offset'        : 0,
    'units'         : "",
  }
  duration_min = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "min",
  }
  duration = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  ascent = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  descent = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  moderate_activity_minutes = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "minutes",
  }
  vigorous_activity_minutes = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "minutes",
  }

class hr():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'offset'        : 0,
    'units'         : "s",
  }
  time256 = {
    'type'          : basetypes.Field.uint8,
    'components'    : "fractional_timestamp",
    'scale'         : 256,
    'offset'        : 0,
    'units'         : "s",
    'bits'          : "8",
  }
  filtered_bpm = {
    'type'          : basetypes.Field.uint8,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "bpm",
  }
  event_timestamp = {
    'type'          : basetypes.Field.uint32,
    'array'         : "[N]",
    'scale'         : 1024,
    'offset'        : 0,
    'units'         : "s",
  }
  event_timestamp_12 = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'components'    : "event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp, event_timestamp ",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
    'bits'          : "12, 12, 12, 12, 12, 12, 12, 12, 12, 12",
    'accumulate'    : "1, 1, 1, 1, 1, 1, 1, 1, 1, 1",
  }

class stress_level():
  stress_level_value = {
    'type'          : basetypes.Field.sint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  stress_level_time = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }

class memo_glob():
  part_index = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  memo = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  message_number = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  message_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class ant_channel_id():
  channel_number = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  device_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  device_number = {
    'type'          : basetypes.Field.uint16z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  transmission_type = {
    'type'          : basetypes.Field.uint8z,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  device_index = {
    'type'          : profile.device_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class ant_rx():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'offset'        : 0,
    'units'         : "s",
  }
  mesg_id = {
    'type'          : basetypes.Field.byte,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  mesg_data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'components'    : "channel_number,data,data,data,data,data,data,data,data",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
    'bits'          : "8,8,8,8,8,8,8,8,8",
  }
  channel_number = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class ant_tx():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  fractional_timestamp = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 32768,
    'offset'        : 0,
    'units'         : "s",
  }
  mesg_id = {
    'type'          : basetypes.Field.byte,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  mesg_data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'components'    : "channel_number,data,data,data,data,data,data,data,data",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
    'bits'          : "8,8,8,8,8,8,8,8,8",
  }
  channel_number = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  data = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class exd_screen_configuration():
  screen_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  field_count = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  layout = {
    'type'          : profile.exd_layout,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  screen_enabled = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class exd_data_field_configuration():
  screen_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  concept_field = {
    'type'          : basetypes.Field.byte,
    'components'    : "field_id,concept_count",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
    'bits'          : "4,4",
  }
  field_id = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  concept_count = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  display_type = {
    'type'          : profile.exd_display_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  title = {
    'type'          : basetypes.Field.string,
    'array'         : "[32]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class exd_data_concept_configuration():
  screen_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  concept_field = {
    'type'          : basetypes.Field.byte,
    'components'    : "field_id,concept_index",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
    'bits'          : "4,4",
  }
  field_id = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  concept_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  data_page = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  concept_key = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  scaling = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  data_units = {
    'type'          : profile.exd_data_units,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  qualifier = {
    'type'          : profile.exd_qualifiers,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  descriptor = {
    'type'          : profile.exd_descriptors,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  is_signed = {
    'type'          : profile.bool,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class field_description():
  developer_data_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  field_definition_number = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  fit_base_type_id = {
    'type'          : profile.fit_base_type,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  field_name = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  array = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  components = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  scale = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  offset = {
    'type'          : basetypes.Field.sint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  units = {
    'type'          : basetypes.Field.string,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bits = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  accumulate = {
    'type'          : basetypes.Field.string,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  fit_base_unit_id = {
    'type'          : profile.fit_base_unit,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  native_mesg_num = {
    'type'          : profile.mesg_num,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  native_field_num = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class developer_data_id():
  developer_id = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  application_id = {
    'type'          : basetypes.Field.byte,
    'array'         : "[N]",
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  manufacturer_id = {
    'type'          : profile.manufacturer,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  developer_data_index = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  application_version = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }

class dive_summary():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  reference_mesg = {
    'type'          : profile.mesg_num,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  reference_index = {
    'type'          : profile.message_index,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  avg_depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  max_depth = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "m",
  }
  surface_interval = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  start_cns = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  end_cns = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  start_n2 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  end_n2 = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "percent",
  }
  o2_toxicity = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "OTUs",
  }
  dive_number = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  bottom_time = {
    'type'          : basetypes.Field.uint32,
    'scale'         : 1000,
    'offset'        : 0,
    'units'         : "s",
  }

class climb_pro():
  timestamp = {
    'type'          : profile.date_time,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "s",
  }
  position_lat = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  position_long = {
    'type'          : basetypes.Field.sint32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "semicircles",
  }
  climb_pro_event = {
    'type'          : profile.climb_pro_event,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  climb_number = {
    'type'          : basetypes.Field.uint16,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  climb_category = {
    'type'          : basetypes.Field.uint8,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "",
  }
  current_dist = {
    'type'          : basetypes.Field.float32,
    'scale'         : 1,
    'offset'        : 0,
    'units'         : "m",
  }
