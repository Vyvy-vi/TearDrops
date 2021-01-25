import random
import discord
from discord.ext import commands

from .utils import COLOR


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """The bot's ping command"""
        phrase = ['I am alive...',
                  'I was definitely not sleeping...',
                  'I was definitely not laughing...',
                  'I am still here',
                  'You are using a ping command? Why?',
                  'At your service.']
        ph = random.choice(phrase)
        lsm = round(self.client.latency * 1000)
        embed = discord.Embed(
            title='**pong...!**',
            description=f"_{ph}_ \n**~{lsm} ms taken**......",
            color=COLOR.SUCCESS)
        embed.set_footer(text='😭')
        await ctx.send(embed=embed)

    @commands.command()
    async def pong(self, ctx):
        """The bot's pong command"""
        phrase = ["I am aliven't...",
                  "I was sleeping...",
                  "I was laughing...",
                  "I am still not here",
                  "You are using a pong command? Why?",
                  "Not at your service."]
        ph = random.choice(phrase)
        lsm = round(self.client.latency * 1000)
        embed = discord.Embed(
            title='**PING...!**',
            description=f"_{ph}_ \n**~{lsm} ms taken**......",
            color=COLOR.ERROR)
        embed.set_footer(text='😭')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
