import random

from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

from pymongo import MongoClient
import motor.motor_asyncio as motor

from utils import get_environment_variable
from .utils import COLOR

buls = 1


MONGO_CONNECTION_STRING = get_environment_variable("MONGO_CONNECTION_STRING")
DB_CLIENT = motor.AsyncIOMotorClient(MONGO_CONNECTION_STRING)


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['diceroll', 'roll'])
    async def dice(self, ctx: Context, amount: int):
        '''dice-guess game'''
        num = amount
        if num <= 6:
            user = ctx.message.author
            db = DB_CLIENT.users_db
            server = db[str(user.guild.id)]
            stats = list(await server.find_one({'id': user.id}))
            cred = stats[-1]['credits']
            numtemp = random.randint(1, 6)
            if num == numtemp:
                await server.update_one(stats[-1], {"$inc": {'credits': 50}})
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
        '''starts fun russian roulette game'''
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
