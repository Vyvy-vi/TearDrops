# TODO - transfer, casino, etc commands


import aiohttp
import time
import random

import os
import ssl
import discord
from discord.ext import commands, tasks
from itertools import cycle

from pymongo import MongoClient


# temp->

# modules for wiki and wolfram queries
# import wolframalpha
# import requests

# Standard modules

# TOKEN, MONGO URI are env-vars
from utils import get_environment_variable


DISCORD_BOT_TOKEN = get_environment_variable("DISCORD_BOT_TOKEN")
MONGO_CONNECTION_STRING = get_environment_variable("MONGO_CONNECTION_STRING")


DB_CLIENT = MongoClient(MONGO_CONNECTION_STRING)
db = DB_CLIENT.get_database('users_db')

ssl._create_default_https_context = ssl._create_unverified_context


# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# NOTE- The initial version of the bot used TinyDB, but I've migrated to
# MongoDB (still considering sql tho)

# client pointer for API-reference
client = commands.Bot(command_prefix='qq ',
                      case_insensitive=True, intents=intents)

# discord.py has an inbuilt help command, which doesn't look good''
client.remove_command('help')


# status-change-cycle(The bot changes presence after a few mins.)
STATUS = cycle([
    "qq help | :(",
    "with your heart"
    "in tears",
    "with tears",
    "with ",
    "I'm so sad",
    "with your tears...",
    "with your feelings",
    "with sparkles"])


ls_cog = ['cogs.fun_cog',
          'cogs.ping_cog',
          'cogs.help_cog',
          'cogs.coffee_cog',
          'cogs.meme_cog',
          'cogs.utils_cog',
          'cogs.name_cog',
          'cogs.game_cog',
          'cogs.economy_cog']


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


@client.event
async def on_guild_join(guild):
    '''
    This sends a message in the main channel, when the bot joins a guild.
    Joining a guild is synonymous to joining a server.
    Basically, a hi message the bot sends on enterring the server.
    '''

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            if guild.id not in db.list_collection_names():
                col = db[str(guild.id)]
                col.insert_one(
                    {'server_name': guild.name, 'server_id': guild.id})
            icon_url = 'https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png'
            embed = discord.Embed(
                title='**Tear Drops:tm:**',
                description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license, I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes',
                colour=discord.Color.purple(),
                url='https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
            embed.set_footer(text='I Hope that you enjoyed the bot....😭')
            embed.set_image(url=icon_url)
            await channel.send(embed=embed)
        break
    print(f'Entered server {guild.name} : {guild.id}')


@tasks.loop(seconds=600)
async def change_status():
    '''
    loops through the cycle of the STATUS list and sets that as bot presence
    '''
    await client.change_presence(activity=discord.Game(next(STATUS)))
    # NOTE- There are other methods, that can be utilised instead of just
    # 'playing'


@client.event
async def on_member_remove(member):
    '''
    Event triggered when a member leaves the server
    NOTE- This can also be displayed on the server
    '''
    print(f'{member} has left the server......')


# error_handling
@client.event
async def on_command_error(ctx, error):
    # TODO- Error Handling
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used..... ")
    else:
        await ctx.send(error)


# cog-loader
if __name__ == "__main__":
    for extension in ls_cog:
        client.load_extension(extension)

# Running the BOT:
client.run(str(DISCORD_BOT_TOKEN))
