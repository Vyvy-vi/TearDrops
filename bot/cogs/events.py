from discord import Embed
from discord.ext import commands

import motor.motor_asyncio as motor

from .utils.colo import COLOR
from .utils.embeds import info_embed

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DB_CLIENT = motor.AsyncIOMotorClient(client.MONGO)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        '''
        This sends a message in the main channel, when the bot joins a guild.
        Joining a guild is synonymous to joining a server.
        Basically, a hi message the bot sends on enterring the server.
        '''
        db = self.DB_CLIENT.users_db
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                if guild.id not in await db.list_collection_names():
                    col = db[str(guild.id)]
                    await col.insert_one({'server_name': guild.name,
                                          'server_id': guild.id})
                    print(f'Server added to db:  {guild.name} - {guild.id}')
                embed = info_embed()
                await channel.send(embed=embed)
            break
        print(f'Entered server:  {guild.name} - {guild.id}')
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
