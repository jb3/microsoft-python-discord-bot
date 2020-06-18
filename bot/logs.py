"""Logging configuration for the bot."""

import coloredlogs


def setup_logging() -> None:
    """Install the colored log handler on the root logger."""
    coloredlogs.install(level="INFO")
