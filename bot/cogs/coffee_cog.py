import random

from discord import Member, Embed
from discord.ext import commands
from discord.ext.commands import Context
from .inputs import cl, cf, chill, cfe, ur
from .utils import COLOR


class Coffee(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ask_out'])
    async def wannagrabacoffee(self, ctx: Context, *, member: Member):
        '''Wanna ask someone out on coffee'''
        embed = Embed(
            title=f'{member}, Someone wants to grab a coffee with you...*wink *wink',
            color=COLOR.DEFAULT)
        embed.add_field(name='This happened....', value=f'{random.choice(cf)}')
        embed.set_footer(text='not actually')
        await ctx.send(embed=embed)

    @commands.command(aliases=['brew'])
    async def coffee(self, ctx: Context):
        '''A lovely coffee command (sip, sip)'''
        op = f'{random.choice(cfe)}'
        embed = Embed(title='Coffee',
                              description=op,
                              color=COLOR.DEFAULT)
        embed.set_footer(
            text=f'Caffeiene Level-{random.choice(cl)}.{random.choice(chill)}')
        embed.set_image(url=random.choice(ur))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Coffee(client))
