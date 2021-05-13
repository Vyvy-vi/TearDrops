# from discord import Embed
from discord.ext import commands

import motor.motor_asyncio as motor
from loguru import logger

# from .utils.colo import COLOR
from .utils.embeds import info_embed


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DB_CLIENT = motor.AsyncIOMotorClient(client.MONGO)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        '''
        This sends a message in the main channel, when the bot joins a guild.
        '''
        db = self.DB_CLIENT.users_db
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                if guild.id not in await db.list_collection_names():
                    col = db[str(guild.id)]
                    await col.insert_one({'server_name': guild.name,
                                          'server_id': guild.id})
                    logger.info(
                        f'Server added to db:  {guild.name} - {guild.id}')
                embed = info_embed()
                await channel.send(embed=embed)
            break
        logger.info(f'Entered server:  {guild.name} - {guild.id}')


def setup(client):
    client.add_cog(Events(client))
