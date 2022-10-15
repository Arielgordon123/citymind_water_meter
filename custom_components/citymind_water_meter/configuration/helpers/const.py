"""
Following constants are mandatory for CORE:
    DEFAULT_NAME - Full name for the title of the integration
    DOMAIN - name of component, will be used as component's domain
    SUPPORTED_PLATFORMS - list of supported HA components to initialize
"""

from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, STATE_OFF, STATE_ON

DOMAIN = "citymind_water_meter"
DEFAULT_NAME = "CityMind"

CONFIGURATION_MANAGER = f"cm_{DOMAIN}"

DATA_KEYS = [
    CONF_EMAIL,
    CONF_PASSWORD
]
