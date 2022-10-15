"""
constants.
"""
from datetime import timedelta

from ...core.helpers.const import *

VERSION = "1.0.0"

ATTR_FRIENDLY_NAME = "friendly_name"

WEEKDAY_UPDATE_DATA_INTERVAL = timedelta(minutes=10)
WEEKEND_UPDATE_DATA_INTERVAL = timedelta(hours=3)
UPDATE_ENTITIES_INTERVAL = timedelta(minutes=1)

UPDATE_DATA_INTERVALS = {
    True: WEEKEND_UPDATE_DATA_INTERVAL,
    False: WEEKDAY_UPDATE_DATA_INTERVAL
}

API_URL_OLD = "https://api.city-mind.com"
API_URL_NEW = "https://api-ctm.city-mind.com"

CITY_MIND_WEBSITE = "https://rym-pro.com"

ENDPOINT_CONSUMER_OLD = f"{API_URL_OLD}/consumer"
ENDPOINT_CONSUMER_NEW = f"{API_URL_NEW}/consumer"

ENDPOINT_CONSUMPTION_NEW = f"{API_URL_NEW}/consumption"

ENDPOINT_MUNICIPALS_OLD = f"{API_URL_OLD}/municipals"
ENDPOINT_MUNICIPALS_NEW = f"{API_URL_NEW}/municipality"

ENDPOINT_LOGIN = f"{ENDPOINT_CONSUMER_OLD}/login"

ENDPOINT_ME = f"{ENDPOINT_CONSUMER_OLD}/me"
ENDPOINT_METERS = f"{ENDPOINT_CONSUMER_NEW}/meters"
ENDPOINT_UNITS = f"{ENDPOINT_MUNICIPALS_OLD}/h1/measurmentunits"
ENDPOINT_CUSTOMER_SERVICE = f"{ENDPOINT_MUNICIPALS_OLD}/municipalCustomerService"
ENDPOINT_ALERTS_FOR_SETTINGS = f"{ENDPOINT_CONSUMER_NEW}/alertsForSettings"

ENDPOINT_LAST_READ = f"{ENDPOINT_CONSUMPTION_NEW}/last-read"
ENDPOINT_CONSUMPTION_DAILY = f"{ENDPOINT_CONSUMPTION_NEW}/daily/lastbillingCycle/[PH_YESTERDAY]/[PH_TODAY]?meterCount=[PH_METER_ID]"
ENDPOINT_CONSUMPTION_MONTHLY = f"{ENDPOINT_CONSUMPTION_NEW}/monthly/[PH_CURRENT_MONTH]/[PH_LAST_DAY_MONTH]?meterCount=[PH_METER_ID]"
ENDPOINT_VACATIONS = f"{ENDPOINT_CONSUMER_OLD}/vacations"
ENDPOINT_MY_ALERTS = f"{ENDPOINT_CONSUMER_NEW}/myalerts"
ENDPOINT_MY_ALERTS_SETTINGS = f"{ENDPOINT_CONSUMER_OLD}/myalerts/settings"
ENDPOINT_MY_MESSAGES = f"{ENDPOINT_MUNICIPALS_NEW}/[PH_MUNICIPALITY]/messages"
ENDPOINT_MY_MESSAGE_SUBJECTS = f"{ENDPOINT_MY_MESSAGES}/message-subjects"
ENDPOINT_CONSUMPTION_LOW_RATE_LIMIT = f"{ENDPOINT_CONSUMPTION_NEW}/Low-Rate-Limit"
ENDPOINT_CONSUMPTION_FORCAST = f"{ENDPOINT_CONSUMPTION_NEW}/forecast/[PH_METER_ID]"
ENDPOINT_MY_ALERTS_SETTINGS_UPDATE = f"{ENDPOINT_MY_ALERTS}/settings"

API_DATA_SECTION_ME = "me"
API_DATA_SECTION_METERS = "meters"
# API_DATA_SECTION_UNITS = "units"
API_DATA_SECTION_CUSTOMER_SERVICE = "customer-service"
# API_DATA_SECTION_MY_MESSAGE_SUBJECTS = "my-message-subjects"
# API_DATA_SECTION_ALERTS_FOR_SETTINGS = "alerts-for-settings"
API_DATA_SECTION_LAST_READ = "last-read"
# API_DATA_SECTION_CONSUMPTION_LOW_RATE_LIMIT = "consumption-low-rate-limit"
API_DATA_SECTION_VACATIONS = "vacations"
API_DATA_SECTION_MY_ALERTS = "my-alerts"
API_DATA_SECTION_MY_MESSAGES = "my-messages"
API_DATA_SECTION_CONSUMPTION_DAILY = "consumption-daily"
API_DATA_SECTION_CONSUMPTION_MONTHLY = "consumption-monthly"
API_DATA_SECTION_CONSUMPTION_FORCAST = "consumption-forcast"
API_DATA_SECTION_SETTINGS = "settings"

CUSTOMER_SERVICE_PHONE_NUMBER = "phoneNumber"
CUSTOMER_SERVICE_DESCRIPTION = "description"
CUSTOMER_SERVICE_PHONE_MUNICIPAL_ID = "municipalID"
CUSTOMER_SERVICE_EMAIL = "Email"

METER_COUNT = "meterCount"
METER_SERIAL_NUMBER = "meterSn"
METER_FULL_ADDRESS = "fullAddress"

LAST_READ_METER_COUNT = METER_COUNT
LAST_READ_METER_ID = "meterId"
LAST_READ_VALUE = "read"

ME_FIRST_NAME = "firstName"
ME_LAST_NAME = "lastName"
ME_ACCOUNT_NUMBER = "accountNumber"
ME_PHONE_NUMBER_SECTION = "phoneNumber"
ME_COUNTRY_CODE = "countryCode"
ME_PHONE_NUMBER = "phoneNumber"
ME_ADDITIONAL_PHONE_NUMBER = "AdditionalPhoneNumber"
ME_MUNICIPAL_ID = "municipalId"

CONSUMPTION_METER_COUNT = METER_COUNT
CONSUMPTION_VALUE = "cons"
CONSUMPTION_DATE = "consDate"
CONSUMPTION_ESTIMATION_TYPE = "estimationType"
CONSUMPTION_METER_STATUS_DESC = "meterStatusDesc"

CONSUMPTION_FORCAST_ESTIMATED_CONSUMPTION = "estimatedConsumption"

SETTINGS_ALERT_TYPE_ID = "alertTypeId"
SETTINGS_MEDIA_TYPE_ID = "mediaTypeId"

ENDPOINT_DATA_INITIALIZE = {
    API_DATA_SECTION_ME: ENDPOINT_ME,
    API_DATA_SECTION_METERS: ENDPOINT_METERS,
    # API_DATA_SECTION_UNITS: ENDPOINT_UNITS,
    API_DATA_SECTION_CUSTOMER_SERVICE: ENDPOINT_CUSTOMER_SERVICE,
    # API_DATA_SECTION_MY_MESSAGE_SUBJECTS: ENDPOINT_MY_MESSAGE_SUBJECTS,
    # API_DATA_SECTION_ALERTS_FOR_SETTINGS: ENDPOINT_ALERTS_FOR_SETTINGS
}

ENDPOINT_DATA_UPDATE = {
    API_DATA_SECTION_LAST_READ: ENDPOINT_LAST_READ,
    # API_DATA_SECTION_CONSUMPTION_LOW_RATE_LIMIT: ENDPOINT_CONSUMPTION_LOW_RATE_LIMIT,
    API_DATA_SECTION_VACATIONS: ENDPOINT_VACATIONS,
    API_DATA_SECTION_MY_ALERTS: ENDPOINT_MY_ALERTS,
    API_DATA_SECTION_MY_MESSAGES: ENDPOINT_MY_MESSAGES,
    API_DATA_SECTION_SETTINGS: ENDPOINT_MY_ALERTS_SETTINGS
}

ENDPOINT_DATA_UPDATE_PER_METER = {
    API_DATA_SECTION_CONSUMPTION_DAILY: ENDPOINT_CONSUMPTION_DAILY,
    API_DATA_SECTION_CONSUMPTION_MONTHLY: ENDPOINT_CONSUMPTION_MONTHLY,
    API_DATA_SECTION_CONSUMPTION_FORCAST: ENDPOINT_CONSUMPTION_FORCAST
}

ENDPOINT_DATA_RELOAD = {
    API_DATA_SECTION_SETTINGS: ENDPOINT_MY_ALERTS_SETTINGS
}

PH_TODAY = "[PH_TODAY]"
PH_YESTERDAY = "[PH_YESTERDAY]"
PH_CURRENT_MONTH = "[PH_CURRENT_MONTH]"
PH_LAST_DAY_MONTH = "[PH_LAST_DAY_MONTH]"
PH_METER = "[PH_METER_ID]"
PH_MUNICIPALITY = "[PH_MUNICIPALITY]"

LOGIN_EMAIL = "email"
LOGIN_PASSWORD = "pw"
LOGIN_DEVICE_ID = "deviceId"

DEVICE_ID = "home-assistant"

API_DATA_TOKEN = "token"
API_DATA_LAST_UPDATE = "last-update"

API_HEADER_TOKEN = "x-access-token"

ICON_ALERT_MODES = {
}

STORAGE_DATA_STORE_DEBUG_DATA = "store-debug-data"

STORAGE_DATA_FILE_CONFIG = "config"
STORAGE_DATA_FILE_API_DEBUG = "debug.api"

STORAGE_DATA_FILES = [
    STORAGE_DATA_FILE_CONFIG,
    STORAGE_DATA_FILE_API_DEBUG,
]

FORMAT_DATE_ISO = "%Y-%m-%d"
FORMAT_DATE_YEAR_MONTH = "%Y-%m"

WEEKEND_DAYS = [
    "Friday",
    "Saturday"
]

ALERT_TYPE_DAILY_EXCEPTION = 12
ALERT_TYPE_LEAK = 23
ALERT_TYPE_CONSUMPTION_WHILE_AWAY = 1001

MEDIA_TYPE_NONE = "0"
MEDIA_TYPE_EMAIL = "3"
MEDIA_TYPE_SMS = "1"
MEDIA_TYPE_ALL = "4"

ALERT_TYPES = {
    ALERT_TYPE_DAILY_EXCEPTION: "Exceeded threshold",
    ALERT_TYPE_LEAK: "Leak",
    ALERT_TYPE_CONSUMPTION_WHILE_AWAY: "Leak While Away",
}

ATTR_MEDIA_TYPES = "media_type"
ATTR_ALERT_TYPES = "alert_type"

MEDIA_TYPES = {
    MEDIA_TYPE_NONE: "None",
    MEDIA_TYPE_EMAIL: "Email",
    MEDIA_TYPE_SMS: "SMS",
    MEDIA_TYPE_ALL: "All",
}

MEDIA_TYPE_ICONS = {
    MEDIA_TYPE_NONE: "mdi:close-box-multiple",
    MEDIA_TYPE_EMAIL: "mdi:email",
    MEDIA_TYPE_SMS: "mdi:android-messages",
    MEDIA_TYPE_ALL: "mdi:email-open-multiple",
}
