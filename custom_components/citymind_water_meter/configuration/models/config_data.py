from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry

from ...configuration.helpers.const import *


class ConfigData:
    email: str | None
    password: str | None
    entry: ConfigEntry | None

    def __init__(self):
        self.email = None
        self.password = None
        self.entry = None

    @staticmethod
    def from_dict(data: dict[str, Any] = None) -> ConfigData:
        result = ConfigData()

        if data is not None:
            result.email = data.get(CONF_EMAIL)
            result.password = data.get(CONF_PASSWORD)

        return result

    def to_dict(self):
        obj = {
            CONF_EMAIL: self.email,
            CONF_PASSWORD: self.password
        }

        return obj

    def __repr__(self):
        to_string = f"{self.to_dict()}"

        return to_string
