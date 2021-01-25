import random
import discord
from pymongo import MongoClient
from discord.ext import commands
from utils import get_environment_variable
from .utils import COLOR
buls = 1


MONGO_CONNECTION_STRING = get_environment_variable("MONGO_CONNECTION_STRING")
DB_CLIENT = MongoClient(MONGO_CONNECTION_STRING)
db = DB_CLIENT.get_database('users_db')


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['diceroll', 'roll'])
    async def dice(self, ctx, amount: int):
        '''dice-guess game'''
        num = amount
        if num <= 6:
            user = ctx.message.author
            server = db[str(user.guild.id)]
            stats = list(server.find({'id': user.id}))
            cred = stats[-1]['credits']
            numtemp = random.randint(1, 6)
            if num == numtemp:
                cred += 50
                newstats = {"$set": {'credits': cred}}
                server.update_one(stats[-1], newstats)
                embed = discord.Embed(
                    title='Dice-roll...🎲',
                    description=f'The dice rolled a {numtemp}.\nYou have been awarded 50 tears for this...',
                    color=COLOR.JOY)
            else:
                embed = discord.Embed(
                    title='Dice-roll...🎲',
                    description=f'The dice rolled a {numtemp}.\n\
Your prediction was wrong. 😖',
                    color=COLOR.DEFAULT)
        else:
            embed = discord.Embed(
                title='Dice-roll...🎲',
                description='Please enter a valid number argument.\n\
Command Usage-> qq dice <num> (between 1 and 6)',
                color=COLOR.ERROR)

        await ctx.send(embed=embed)

    @commands.command(aliases=['russian-roulette', 'gunshot', 'rr'])
    async def russian_roulette(self, ctx):
        '''starts fun russian roulette game'''
        global buls
        if buls >= 6:
            buls = 1
            embed = discord.Embed(
                title='Russian Roulette.🔫',
                description='All you remember is the pain you felt when the bullet pierced your skull.',
                color=COLOR.ERROR())
        else:
            buls += 1
            embed = discord.Embed(
                title='Russian Roulette.🔫',
                description='You live to fight another day',
                color=COLOR.DEFAULT())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Game(client))
