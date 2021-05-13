import random
from discord import Embed, Color

from discord.ext import commands
from discord.ext.commands import Context

from .utils.username import generate
from .utils.joeUsername import joe_generate


class Name(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['random-username', 'ru', 'random_username'])
    async def username(self, ctx: Context, lim: int = 30):
        """Generates a random username from DigitalOcean's name-set"""
        op = generate(lim)
        if lim == 30:
            op = generate(random.randint(20, 50))
        embed = Embed(
            title=op,
            description='That sounds cool :',
            color=Color.dark_magenta())
        await ctx.send(embed=embed)

    @commands.command(aliases=['joe-username', 'ju'])
    async def joe_username(self, ctx: Context, lim: int = 4):
        """Generates what Joe Nash would name you"""
        op = joe_generate(lim)
        if lim == 4:
            op = joe_generate(random.randint(3, 11))
        embed = Embed(
            title=op,
            description='That sounds cool, cool, cool.. Right.',
            color=Color.gold())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Name(client))
