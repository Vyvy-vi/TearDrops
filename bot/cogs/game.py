import random

from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

import motor.motor_asyncio as motor

from .utils.colo import COLOR

buls = 1


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DB_CLIENT = motor.AsyncIOMotorClient(client.MONGO)

    @commands.command(aliases=['diceroll', 'roll'])
    async def dice(self, ctx: Context, num: int):
        '''Dice-guess game'''
        if num <= 6:
            user = ctx.message.author
            db = self.DB_CLIENT.users_db
            server = db[str(user.guild.id)]
            stats = await server.find_one({'id': user.id})
            numtemp = random.randint(1, 6)
            if num == numtemp:
                await server.update_one(stats, {"$inc": {'credits': 50}})
                embed = Embed(
                    title='Dice-roll...🎲',
                    description=f'The dice rolled a {numtemp}.\nYou have been awarded 50 tears for this...',
                    color=COLOR.JOY)
            else:
                embed = Embed(
                    title='Dice-roll...🎲',
                    description=f'The dice rolled a {numtemp}.\n\
Your prediction was wrong. 😖',
                    color=COLOR.DEFAULT)
        else:
            embed = Embed(
                title='Dice-roll...🎲',
                description='Please enter a valid number argument.\n\
Command Usage-> qq dice <num> (between 1 and 6)',
                color=COLOR.ERROR)

        await ctx.send(embed=embed)

    @commands.command(aliases=['russian-roulette', 'gunshot', 'rr'])
    async def russian_roulette(self, ctx: Context):
        '''Starts a fun russian roulette game'''
        global buls
        if buls >= 6:
            buls = 1
            embed = Embed(
                title='Russian Roulette.🔫',
                description='All you remember is the pain you felt when the bullet pierced your skull.',
                color=COLOR.ERROR())
        else:
            buls += 1
            embed = Embed(
                title='Russian Roulette.🔫',
                description='You live to fight another day',
                color=COLOR.DEFAULT())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Game(client))
