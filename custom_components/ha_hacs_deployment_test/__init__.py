"""The ha_hacs_deployment_test integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

LOGGER = logging.getLogger(__name__)
DOMAIN = "ha_hacs_deployment_test"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up ha_hacs_deployment_test."""
    LOGGER.debug("Start async_setup - .")
    hass.data.setdefault(DOMAIN, {})

    await hass.config_entries.async_forward_entry_setups(entry, (Platform.SENSOR,))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(
        entry, (Platform.SENSOR,)
    ):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
