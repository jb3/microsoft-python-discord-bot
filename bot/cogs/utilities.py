"""Utility cog for the bot."""

from discord.ext.commands import Bot, Cog, Context, command


class Utilities(Cog):
    """Utility commands."""

    def __init__(self, bot: Bot) -> None:
        """Assign the bot to a class attribute for later usage."""
        self.bot = bot

    @command()
    async def ping(self, ctx: Context) -> None:
        """Ping pong command, ensure the bot is online!"""
        await ctx.send(f"{ctx.author.mention}, pong!")


def setup(bot: Bot) -> None:
    """Setup the Utility cog on the bot."""
    bot.add_cog(Utilities(bot))
