# TODO - transfer, casino, etc commands
from itertools import cycle
from glob import glob

import discord
from discord.ext import commands, tasks

# Standard modules
# TOKEN, MONGO URI are env-vars
from utils import get_environment_variable
# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()

# NOTE- The initial version of the bot used TinyDB, but I've migrated to
# MongoDB (still considering sql tho)
# client pointer for API-reference
client = commands.Bot(command_prefix='qq ',
                      case_insensitive=True, intents=intents)
# Mongo connection string
client.MONGO = get_environment_variable("MONGO_CONNECTION_STRING")
client.TOKEN = get_environment_variable("DISCORD_BOT_TOKEN")

# discord.py has an inbuilt help command, which doesn't look good''
client.remove_command('help')
# status-change-cycle(The bot changes presence after a few mins.)
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
COGS = ['cogs.' + path.split("/")[-1][:-3] for path in glob("./bot/cogs/*.py")]


@client.event
async def on_ready():
    '''
    This prints a message when the on_ready event is detected.
    That is, when the bot logs onto discord when the script is ran.
    '''
    change_status.start()  # Triggers status change task
    print("Processing.....")
    print("|||||||||||||||")
    print("Bot has Successfully logged onto Discord...")
    print('Successfully logged in as {0.user}...'.format(client))
    # client.user gives the bots discord username tag


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
    for ext in COGS:
        client.load_extension(ext)
        print(f'Loaded cog : {ext}')

    # Running the BOT:
    if client.TOKEN != 'foo' and (client.TOKEN is not None):
        client.run(str(client.TOKEN))
    else:
        print('No token Loaded')
