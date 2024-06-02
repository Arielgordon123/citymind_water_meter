import logging

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.util import slugify

from ..common.consts import (
    API_DATA_SECTION_ME,
    ME_ACCOUNT_NUMBER,
    ME_FIRST_NAME,
    ME_LAST_NAME,
)
from ..common.enums import EntityType
from ..managers.config_manager import ConfigManager
from ..models.config_data import ConfigData

_LOGGER = logging.getLogger(__name__)


class BaseProcessor:
    _api_data: dict | None = None
    _account_number: int | None = None
    _first_name: str | None = None
    _last_name: str | None = None
    _today_iso: str | None = None
    _yesterday_iso: str | None = None
    _current_month_iso: str | None = None
    _config_manager: ConfigManager | None = None
    _config_data: ConfigData | None = None
    _unique_messages: list[str] | None = None
    processor_type: EntityType | None = None

    def __init__(self, config_manager: ConfigManager):
        self._config_manager = config_manager

        self._api_data = None
        self._account_number = None
        self._first_name = None
        self._last_name = None
        self.processor_type = None

        self._unique_messages = []

    def update(self, api_data: dict):
        self._api_data = api_data

        analytic_periods = self._config_manager.analytic_periods

        self._today_iso = analytic_periods.today_iso
        self._yesterday_iso = analytic_periods.yesterday_iso
        self._current_month_iso = analytic_periods.current_month_iso

        self._process_api_data()

    def _process_api_data(self):
        me_section = self._api_data.get(API_DATA_SECTION_ME)
        account_number_str = me_section.get(ME_ACCOUNT_NUMBER)
        first_name = me_section.get(ME_FIRST_NAME)
        last_name = me_section.get(ME_LAST_NAME)

        self._account_number = int(account_number_str)
        self._first_name = first_name
        self._last_name = last_name

    def _unique_log(self, log_level: int, message: str):
        if message not in self._unique_messages:
            self._unique_messages.append(message)

            _LOGGER.log(log_level, message)

    def _get_account_name(self):
        parts = [self._first_name, self._last_name, str(self._account_number)]

        relevant_parts = [part for part in parts if part is not None]

        name = " ".join(relevant_parts)

        return name

    def get_device_info(self, item_id: str | None = None) -> DeviceInfo:
        pass

    def _get_device_info_name(self, meter_id: str | None = None):
        parts = [self.processor_type, meter_id]

        relevant_parts = [part for part in parts if part is not None]

        name = " ".join(relevant_parts)

        return name

    def _get_device_info_unique_id(self, item_id: str | None = None):
        identifier = self._get_device_info_name(item_id)

        unique_id = slugify(identifier)

        return unique_id
