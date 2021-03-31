import random
from discord import Embed

from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR


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
        """The bot's ping command"""
        phrase = ['I am alive...',
                  'I was definitely not sleeping...',
                  'I was definitely not laughing...',
                  'I am still here',
                  'You are using a ping command? Why?',
                  'At your service.']
        rand_ph = random.choice(phrase)
        bot_lsm = round(self.client.latency * 1000)
        embed = ping_embed(
            '**pong...!**',
            f"_{rand_ph}_ \n**~{bot_lsm} ms taken**......",
            COLOR.SUCCESS)
        await ctx.send(embed=embed)

    @commands.command()
    async def pong(self, ctx: Context):
        """The bot's pong command"""
        phrase = ["I am aliven't...",
                  "I was sleeping...",
                  "I was laughing...",
                  "I am still not here",
                  "You are using a pong command? Why?",
                  "Not at your service."]
        rand_ph = random.choice(phrase)
        bot_lsm = round(self.client.latency * 1000)
        embed = ping_embed(
            '**PING...!**',
            f"_{rand_ph}_ \n**~{bot_lsm} ms taken**......",
            COLOR.ERROR)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
