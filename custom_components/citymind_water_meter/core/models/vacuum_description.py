from dataclasses import dataclass

from homeassistant.components.vacuum import StateVacuumEntityDescription


@dataclass(kw_only=True, frozen=True)
class VacuumDescription(StateVacuumEntityDescription):
    """A class that describes vacuum entities."""

    features: int = 0
    fan_speed_list: list[str] = ()
