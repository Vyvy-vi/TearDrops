from discord import Embed

from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR
from .utils.phrases import TEXT


def ping_embed(title, desc, colo):
    embed = Embed(title=title,
                  description=desc,
                  color=colo)
    embed.set_footer(text='😭')
    return embed


class Ping(commands.Cog):
    """This is the Ping Cog, mainly for testing the bot-status"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx: Context):
        """Ping command (for testing)"""
        bot_lsm = round(self.client.latency * 1000)
        embed = ping_embed(
            '**pong...!**',
            f"_{TEXT.ping}_ \n**~{bot_lsm} ms taken**......",
            COLOR.SUCCESS)
        await ctx.send(embed=embed)

    @commands.command()
    async def pong(self, ctx: Context):
        """Pong command (also for testing)"""
        bot_lsm = round(self.client.latency * 1000)
        embed = ping_embed(
            '**PING...!**',
            f"_{TEXT.pong}_ \n**~{bot_lsm} ms taken**......",
            COLOR.ERROR)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def echo(self, ctx: Context, *args):
        '''echos the words into the abyss'''
        output = ''
        for word in args:
            output += word
            output += ' '
        await ctx.send(output)

    @commands.command(pass_context=True)
    async def say(self, ctx: Context, *args):
        """Gives the user's statement a nice richtext quote format"""
        output = ''
        for word in args:
            output += word
            output += ' '
        user = ctx.message.author
        embed = Embed(
            title=f'{output}',
            description=f'~{user}',
            colour=COLOR.RANDOM())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
