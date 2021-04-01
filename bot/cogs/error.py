from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

from loguru import logger
from .utils.colo import COLOR


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error):
        if isinstance(error, commands.CommandNotFound):
            embed = Embed(title='Invalid command used...',
                          colour=COLOR.ERROR)
            await ctx.send(embed=embed)
            logger.warning(f'Invalid command used:\n {ctx.message.content}\n')
        else:  # TODO - Error Handling
            await ctx.send(error)
            logger.error(error)


def setup(client):
    client.add_cog(Errors(client))
