import discord
from discord.ext import commands
from .username import generate
from .joeUsername import joe_generate


class NameCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['random-username', 'ru', 'random_username'])
    async def username(self, ctx, lim: int = 30):
        op = generate(lim)
        if lim == 30:
            op = generate(random.randint(20, 50))
        embed = discord.Embed(
            title=op,
            description='That sounds cool :',
            color=discord.Color.dark_magenta())
        await ctx.send(embed=embed)

    @commands.command(aliases=['joe-username', 'ju'])
    async def joe_username(self, ctx, lim: int = 4):
        op = joe_generate(lim)
        if lim == 4:
            op = joe_generate(random.randint(3, 11))
        embed = discord.Embed(
            title=op,
            description='That sounds cool, cool, cool.. Right.',
            color=discord.Color.gold())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(NameCog(client))
