"""RSS feed parsing feeds from Python related outlets."""

from datetime import datetime
from time import mktime

import feedparser
from babel.dates import format_timedelta
from discord import Embed
from discord.ext.commands import Bot, Cog, Context, command

from bot.config import CONFIG

FEEDS = {
    "python": "https://devblogs.microsoft.com/python/feed/",
    "devblogs": "https://devblogs.microsoft.com/feed/landingpage/",
    "azure devops": "https://devblogs.microsoft.com/devops/feed/",
    "devops": "https://devblogs.microsoft.com/devops/feed/",
    "vscode": "https://code.visualstudio.com/feed.xml",
    "vs code": "https://code.visualstudio.com/feed.xml",
    "cosmos db": "https://devblogs.microsoft.com/cosmosdb/feed/",
    "cosmos": "https://devblogs.microsoft.com/cosmosdb/feed/",
    "iot": "https://devblogs.microsoft.com/iotdev/feed/",
    "internet of things": "https://devblogs.microsoft.com/iotdev/feed/",
}


class RSS(Cog):
    """A cog for working with RSS feeds from various sites."""

    def __init__(self, bot: Bot) -> None:
        """Assign the bot to a class attribute for later usage."""
        self.bot = bot

    @command(aliases=["available", "feeds"])
    async def available_feeds(self, ctx: Context) -> None:
        """Post the available feeds."""
        found = set()
        available = []

        for feed, url in FEEDS.items():
            # Ignore aliases
            if url in found:
                continue

            found.add(url)

            available.append(f"• {feed}")

        embed = Embed(title="Available feeds", description="\n".join(available))

        await ctx.send(embed=embed)

    @command()
    async def feed(self, ctx: Context, *, feed: str = "devblogs") -> None:
        """Fetch 5 most recent posts from a feed."""
        if feed_url := FEEDS.get(feed.lower()):
            feed = feedparser.parse(feed_url)

            feed["entries"] = feed["entries"][:5]

            description = ""

            embed = Embed(
                title=feed["feed"]["title"],
                color=41709,
                description=feed["feed"].get("description"),
            )

            for post in feed["entries"]:
                if published := post.get("published_parsed"):
                    dt = datetime.fromtimestamp(mktime(published))
                    delta = datetime.now() - dt
                    delta_human = format_timedelta(delta, locale="en_US")
                    published_str = f" - {delta_human} ago"
                else:
                    published_str = ""

                description += (
                    f"[{post['title']} - {post['author']}]({post['id']})"
                    f"{published_str}\n\n"
                )

                embed.add_field(
                    name=f"{post['title']} - {post['author']}",
                    value=f"[View post]({post['id']}){published_str}",
                    inline=False,
                )

            embed.set_thumbnail(
                url=feed["feed"].get("image", {}).get("href", "https://example.com/")
            )

            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f":warning: Feed not found! Run `{CONFIG.bot.prefix}available` to see"
                " all available feeds."
            )


def setup(bot: Bot) -> None:
    """Add the RSS cog to the bot."""
    bot.add_cog(RSS(bot))
