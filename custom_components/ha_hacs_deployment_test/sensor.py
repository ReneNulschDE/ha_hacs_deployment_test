"""Sensor platform for ha_hacs_deployment_test integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Initialize ha_hacs_deployment_test config entry."""

    name = "ha_hacs_deployment_test"
    unique_id = "ha_hacs_deployment_test"

    async_add_entities([DeploymentTestSensorEntity(unique_id, name)])


class DeploymentTestSensorEntity(SensorEntity):
    """ha_hacs_deployment_test Sensor."""

    def __init__(self, unique_id: str, name: str) -> None:
        """Initialize NEW_DOMAIN Sensor."""
        super().__init__()
        self._attr_state = "1"
        self._attr_name = name
        self._attr_unique_id = unique_id
