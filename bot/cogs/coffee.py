from random import choice

import motor.motor_asyncio as motor
from discord import Member, Embed
from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR


class Coffee(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.data = motor.AsyncIOMotorClient(client.MONGO).DATA.inputs
    @commands.command(aliases=['ask_out'])
    async def wannagrabacoffee(self, ctx: Context, *, member: Member):
        '''Wanna ask someone out on coffee'''
        res = await self.data.find_one({'type': 'coffee'})
        embed = Embed(
            title=f'{member}, Someone wants to grab a coffee with you...*wink *wink',
            color=COLOR.COFFEE)
        embed.add_field(name='This happened....', value=choice(res['events']))
        embed.set_footer(text='not actually :P')
        await ctx.send(embed=embed)

    @commands.command(aliases=['brew'])
    async def coffee(self, ctx: Context):
        '''A lovely coffee command (sip, sip)'''
        res = await self.data.find_one({'type': 'coffee'})
        embed = Embed(title='Coffee',
                      description=choice(res['text']),
                      color=COLOR.COFFEE)
        embed.set_footer(
            text=f"Caffeiene Level-{choice(res['strength'])}. {choice(res['msg'])}")
        embed.set_image(url=choice(res['img']))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Coffee(client))
