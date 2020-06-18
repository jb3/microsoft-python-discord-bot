"""Main bot class for the Discord bot."""

import logging
from pathlib import Path

from discord.ext.commands import Bot

logger = logging.getLogger(__name__)


class MicrosoftPythonBot(Bot):
    async def on_ready(self) -> None:
        """Handle the on_ready event from Discord, called when the bot comes online."""
        logger.info(f"Logged in as {self.user} connected to {len(self.guilds)} servers")

        cog_directory = Path(".") / "bot" / "cogs"

        for cog in cog_directory.rglob("*.py"):
            logger.info(f"Loading {cog.stem} cog")

            import_name = f"bot.cogs.{cog.stem}"
            self.load_extension(import_name)
