"""
Support for Blue Iris.
For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/switch.blueiris/
"""
from datetime import timedelta

VERSION = '1.0.7'

DOMAIN = 'blueiris'
DATA_BLUEIRIS = f'data_{DOMAIN}'
DEFAULT_NAME = "Blue Iris"
SIGNAL_UPDATE_BLUEIRIS = f'updates_{DOMAIN}'

ATTR_ADMIN_PROFILE = 'Profile'
ATTR_SYSTEM_CAMERA_ALL_NAME = 'All'
ATTR_SYSTEM_CAMERA_ALL_ID = 'Index'
ATTR_SYSTEM_CAMERA_CYCLE_NAME = 'Cycle'
ATTR_SYSTEM_CAMERA_CYCLE_ID = '@Index'

BLUEIRIS_AUTH_ERROR = "Authorization required"

SYSTEM_CAMERA_CONFIG = {
    ATTR_SYSTEM_CAMERA_ALL_NAME: ATTR_SYSTEM_CAMERA_ALL_ID,
    ATTR_SYSTEM_CAMERA_CYCLE_NAME: ATTR_SYSTEM_CAMERA_CYCLE_ID
}

CONF_CAMERAS = 'camera'

CONF_PROFILE = 'profile'
CONF_PROFILE_ARMED = 'armed'
CONF_PROFILE_UNARMED = 'unarmed'

NOTIFICATION_ID = f'{DOMAIN}_notification'
NOTIFICATION_TITLE = f'{DEFAULT_NAME} Setup'

ATTR_SUPPORTED_FEATURES = 'supported_features'

DEFAULT_ICON = 'mdi:alarm-light'

CAMERA_ID_PLACEHOLDER = '[camera_id]'

SCAN_INTERVAL = timedelta(seconds=60)

IMAGE_TIMEOUT = timedelta(seconds=5)

PROTOCOLS = {
    True: 'https',
    False: 'http'
}

DEFAULT_PAYLOAD_OFF = 'OFF'
DEFAULT_PAYLOAD_ON = 'ON'
DEFAULT_FORCE_UPDATE = False

DEVICE_CLASS_CONNECTIVITY = 'connectivity'
DEVICE_CLASS_MOTION = 'motion'
