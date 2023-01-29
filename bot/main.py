from itertools import cycle

import sys
import logging
import discord
from aiohttp import ClientSession
from loguru import logger
from discord.ext import commands, tasks

from utils import get_environment_variable

# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()


# remove default help command
# TODO - Use Sub-classsing from inbuilt command to re-build this.
# client.remove_command("help")

# _close = client.close


# async def close():
#     logger.info("Logging out...")
#     await _close()
#     if client.session:
#         logger.info("Closing aiohttp.ClientSession")
#         await client.session.close()


# client.close = close

d_logger = logging.getLogger("discord")
d_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
d_logger.addHandler(handler)

logger.add(
    "discord.log", format="{time} {level} {message}", level="DEBUG", rotation="5 MB"
)
logger.info("Logging Process Started...")

STATUS = cycle(
    [
        "qq help | :(",
        "with your heart",
        "in tears",
        "with tears",
        "with your soul",
        "I'm so sad",
        "with your tears...",
        "with your feelings",
        "with sparkles",
    ]
)

COGS = [
    "cogs.coffee",
    "cogs.comic",
    "cogs.error",
    "cogs.help",
    "cogs.game",
    "cogs.meme",
    "cogs.users",
    "cogs.utilities",
    "cogs.ping",
    "cogs.events",
    "cogs.economy",
    "cogs.fun",
    "cogs.name",
]


@tasks.loop(seconds=600)
async def change_status():
    """
    Change bot presence, based on the STATUS cycle
    """
    await bot.change_presence(activity=discord.Game(next(STATUS)))


CLIENT_ID = get_environment_variable("CLIENT_ID")


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="qq",
            case_insensitive=True,
            application_id=CLIENT_ID,
            intents=intents,
        )
        self.session = ClientSession()
        try:
            self.MONGO = get_environment_variable("MONGO_CONNECTION_STRING")
            self.TOKEN = get_environment_variable("DISCORD_BOT_TOKEN")
        except ValueError as err:
            logger.error(f"Environment Variables Not Found...\n{err}")
            sys.exit()

        super().remove_command("help")

    async def setup_hook(self):
        COGS.append("jishaku")
        logger.info("Loading Cogs...")
        for ext in COGS:
            await self.load_extension(ext)
            logger.info(f"Loaded cog : {ext}")
        await bot.tree.sync()

    async def on_ready(self):
        change_status.start()  # Triggers status change task
        logger.info("Bot has Successfully logged onto Discord...")
        logger.info(f"Successfully logged in as {bot.user}...")


bot = Bot()

if __name__ == "__main__":
    # Running the BOT:
    if bot.TOKEN != "foo" and (bot.TOKEN is not None):
        bot.run(str(bot.TOKEN))
    else:
        logger.warning("No token Loaded")
