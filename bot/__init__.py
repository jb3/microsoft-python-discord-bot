"""Discord bot for the Microsoft Python Discord community."""

import logging
import os

from dotenv import load_dotenv

from bot import logs
from bot.bot import MicrosoftPythonBot
from bot.config import CONFIG

# Load the environment variables from a .env file (bot token)
load_dotenv()

logger = logging.getLogger(__name__)


def start():
    """Entrypoint for the bot, called by Poetry to start."""
    logs.setup_logging()

    logger.info("Starting Microsoft Python Discord bot")

    bot = MicrosoftPythonBot(command_prefix=CONFIG.bot.prefix)

    if token := os.getenv("TOKEN"):
        bot.run(token)
    else:
        logger.critical(
            "No token was passed, see the README and pass one through"
            " the TOKEN environment variable"
        )
