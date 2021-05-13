from itertools import cycle

import sys
import logging
import discord

from loguru import logger

from discord.ext import commands, tasks

from utils import get_environment_variable
from aiohttp import ClientSession

# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()

# client pointer for API-reference
client = commands.Bot(command_prefix='qq ',
                      case_insensitive=True, intents=intents)

# Mongo connection string
try:
    client.MONGO = get_environment_variable("MONGO_CONNECTION_STRING")
    client.TOKEN = get_environment_variable("DISCORD_BOT_TOKEN")
except ValueError as err:
    logger.error(f'Environment Variables Not Found...\n{err}')
    sys.exit()

# remove default help command
# TODO - Use Sub-classsing from inbuilt command to re-build this.
client.remove_command('help')

_close = client.close


async def close():
    logger.info('Logging out...')
    await _close()
    if client.HTTP_SESSION:
        logger.info('Closing aiohttp.ClientSession')
        await client.HTTP_SESSION.close()
client.close = close

d_logger = logging.getLogger('discord')
d_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log',
    encoding='utf-8',
    mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
d_logger.addHandler(handler)

logger.add(
    'discord.log',
    format="{time} {level} {message}",
    level='DEBUG',
    rotation="5 MB")
logger.info('Logging Process Started...')

STATUS = cycle([
    "qq help | :(",
    "with your heart",
    "in tears",
    "with tears",
    "with your soul",
    "I'm so sad",
    "with your tears...",
    "with your feelings",
    "with sparkles"])

COGS = ['cogs.coffee',
        'cogs.comic',
        'cogs.error',
        'cogs.help',
        'cogs.game',
        'cogs.meme',
        'cogs.users',
        'cogs.utilities',
        'cogs.ping',
        'cogs.events',
        'cogs.economy',
        'cogs.fun',
        'cogs.name']


@client.event
async def on_ready():
    '''
    Prints out bot status on start
    '''
    change_status.start()  # Triggers status change task
    logger.info("Bot has Successfully logged onto Discord...")
    logger.info('Successfully logged in as {0.user}...'.format(client))
    logger.info('Starting aiohttp.ClientSession')
    client.HTTP_SESSION = ClientSession()


@tasks.loop(seconds=600)
async def change_status():
    '''
    Change bot presence, based on the STATUS cycle
    '''
    await client.change_presence(activity=discord.Game(next(STATUS)))


if __name__ == "__main__":
    COGS.append('jishaku')
    logger.info('Loading Cogs...')
    # Load Cogs
    for ext in COGS:
        client.load_extension(ext)
        logger.info(f'Loaded cog : {ext}')
    # Running the BOT:
    if client.TOKEN != 'foo' and (client.TOKEN is not None):
        client.run(str(client.TOKEN))
    else:
        logger.warning('No token Loaded')
