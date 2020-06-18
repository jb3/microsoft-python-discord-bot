"""Loading of the configuration from the TOML file."""

import logging
from pathlib import Path

import toml
from attrdict import AttrDict

logger = logging.getLogger(__name__)


def get_config() -> AttrDict:
    """
    Load the confiuration from the TOML file and return an attribute dictionary.

    This also handles the swapping between config.toml and config-default.toml
    """
    config_toml = Path("./config.toml")
    config_default = Path("./config-default.toml")

    if config_toml.exists():
        with open(config_toml, "r") as config_file:
            return AttrDict(toml.load(config_file))

    if config_default.exists():
        with open(config_default, "r") as config_default:
            return AttrDict(toml.load(config_default))

    logger.critical("ABC")


# Create a config object for other modules to import
CONFIG = get_config()
