import discord
from discord.ext import commands

from .utils import COLOR


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='Invalid command used...',
                                  colour=COLOR.ERROR)
            await ctx.send(embed=embed)
        else:  # TODO - Error Handling
            await ctx.send(error)


def setup(client):
    client.add_cog(Errors(client))
