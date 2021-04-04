# TODO - transfer, casino, etc commands
from itertools import cycle

import sys
import logging
import discord

from loguru import logger

from discord.ext import commands, tasks

# Standard modules
# TOKEN, MONGO URI are env-vars
from utils import get_environment_variable
from aiohttp import ClientSession
# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()

# NOTE- The initial version of the bot used TinyDB, but I've migrated to
# MongoDB (still considering sql tho)
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
client.remove_command('help')
# status-change-cycle(The bot changes presence after a few mins.)

_close = client.close
async def close():
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
    This prints a message when the on_ready event is detected.
    That is, when the bot logs onto discord when the script is ran.
    '''
    change_status.start()  # Triggers status change task
    logger.info("Bot has Successfully logged onto Discord...")
    logger.info('Successfully logged in as {0.user}...'.format(client))
    logger.info('Starting aiohttp.ClientSession')
    client.HTTP_SESSION = ClientSession()
    # client.user gives the bots discord username tag

# discord.py has an inbuilt help command, which doesn't look good''
@tasks.loop(seconds=600)
async def change_status():
    '''
    loops through the cycle of the STATUS list and sets that as bot presence
    '''
    await client.change_presence(activity=discord.Game(next(STATUS)))
    # NOTE- There are other methods, that can be utilised instead of just
    # 'playing'

# cog-loader
if __name__ == "__main__":
    COGS.append('jishaku')
    logger.info('Loading Cogs...')
    for ext in COGS:
        client.load_extension(ext)
        logger.info(f'Loaded cog : {ext}')
    # Running the BOT:
    if client.TOKEN != 'foo' and (client.TOKEN is not None):
        client.run(str(client.TOKEN))
    else:
        logger.warning('No token Loaded')
