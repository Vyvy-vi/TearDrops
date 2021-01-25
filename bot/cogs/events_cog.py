import discord
from discord.ext import commands
from pymongo import MongoClient

from utils import get_environment_variable
from .utils import COLOR

MONGO_CONNECTION_STRING = get_environment_variable("MONGO_CONNECTION_STRING")
DB_CLIENT = MongoClient(MONGO_CONNECTION_STRING)
db = DB_CLIENT.get_database('users_db')


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
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
                    colour=COLOR.DEFAULT,
                    url='https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
                embed.set_footer(text='I Hope that you enjoyed the bot....😭')
                embed.set_image(url=icon_url)
                await channel.send(embed=embed)
            break
        print(f'Entered server {guild.name} : {guild.id}')
    """
    @commands.Cog.listener()
    async def on_member_remove(self, guild, user):
        '''
        Event triggered when a member leaves the server
        NOTE- This can also be displayed on the server
        '''
        print(f'{user} has left the server {guild}......')
    """
    """
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        '''Event Listener which is called when a user is banned from the guild
        For more info:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        '''
        print(f'{user} was banned from {guild.name}-{guild.id}')
    """


def setup(client):
    client.add_cog(Events(client))
