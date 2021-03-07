import time
import random

from typing import Union

import motor.motor_asyncio as motor

from discord import User, Member, Message, TextChannel, Embed
from discord.ext import commands
from discord.ext.commands import Context

from .utils import COLOR

timelast = 0


def decide_score() -> int:
    trs = tuple(range(0, 501, 50))
    weights = (5, 15, 20, 30, 45, 50, 45, 30, 20, 15, 5)
    return random.choices(trs, weights)[0]

def rand_message() -> str:
    txt = (
            'You were not sad',
            'You were surprisingly too happy to cry',
            'You cried so much already that the tears are not coming out',
            'You really tried but you could not cry',
            'The tears are not coming out...')
    return random.choice(txt)



async def update_data(db, user: Union[User, Member]):
    '''
    This Updates the user data in the db to add entry for new members
    '''
    server = db[str(user.guild.id)]
    matching_entry = await server.find_one({'id': user.id})
    if matching_entry is None:
        await server.insert_one({'id': user.id,
                                 'experience': 0,
                                 'level': 1,
                                 'credits': 0,
                                 'crytime': 0})
        print(f'{user.id} added to database...')


async def add_experience(db, message: Message, user: Union[User, Member], exp: int):
    """Adds xp to the user in the database, and calls the level up function"""
    server = db[str(user.guild.id)]
    stats = await server.find_one({'id': user.id})
    await server.update_one(stats, {"$inc": {'experience': exp}})
    await level_up(db, message.author, message.channel)


async def level_up(db, user: Union[User, Member], channel: TextChannel):
    """Takes care of checking the level-up parameters to boot ppl to next level when sufficient xp obtained"""
    server = db[str(user.guild.id)]
    stats = await server.find_one({'id': user.id})
    lvl_start = stats['level']
    exp = stats['experience']
    x = 35
    cnt = 1
    while x < exp:
        x = 2 * x + 10
        cnt += 1
    lvl_end = cnt - 1 if exp >= x else lvl_start
    earned = lvl_end * 150
    if lvl_start < lvl_end:
        new_stats = {"$set": {'level': lvl_end,
                              'credits': stats['credits'] + earned}}
        await server.update_one(stats, new_stats)
        embed = Embed(
            title=f'{user} has leveled up to {lvl_end}.',
            description=f'You have been given {earned} tears for your active-ness.\n\
Saving {earned} tears in your vault of tears.',
            color=COLOR.LEVELLING)
        embed.set_footer(text='😭')
        await channel.send(embed=embed)


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DB_CLIENT = motor.AsyncIOMotorClient(client.MONGO)

    @commands.Cog.listener()
    async def on_member_join(self, member: Union[User, Member]):
        '''
        Event triggered when a new member enters server
        This prints the message out on Terminal.
        Also, this awaits the update_data() function, to add member to the database.
        '''
        print(f'{member} has joined the server.....')
        await update_data(self.DB_CLIENT.users_db, member)

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        '''
        Event triggered when a message is sent on the server
        This is associated with a few if-else responses(you can add more by looking at the examples)
        And finally, this triggers client.process_commands() which registers bot commands.
        '''
        if message.author == self.client.user:
            # self-ignore, to prevent responses to self
            return
        elif message.author.bot:
            # To ignore the messages of other bots
            return
        else:
            # message_xp updation block
            global timelast
            await update_data(self.DB_CLIENT.users_db, message.author)
            timlst = timelast
            if time.time() - timlst > 25:
                await add_experience(self.DB_CLIENT.users_db, message, message.author, 10)
                timelast = time.time()
            # message if-else response examples(you can add more)
            if 'tears' in message.content:
                await message.author.send('😭')  # dms

        # prevents commands from not being processed

    @commands.command(aliases=['daily'])
    async def cry(self, ctx: Context):
        '''credit gain command for crying'''
        user = ctx.message.author
        server = self.DB_CLIENT.users_db[str(user.guild.id)]
        stats = await server.find_one({'id': user.id})
        colo = COLOR.DEFAULT
        if time.time() - stats['crytime'] > 10800:
            tr = decide_score()
            if tr > 1:
                desc = f'You cried {tr} tears.\n\
Storing them in the vaults of tears.Spend them wisely...💦\nSpend them wisely...'
            elif tr == 1:
                desc = 'You really tried but only 1 tear came out...\n\
Storing it in the vaults of tears.Spend them wisely...💧\nSpend it wisely...'
            else:
                desc = "You can't cry rn. {rand_message()}\n\
Try again in like 3 hours.",
                colo = COLOR.ERROR
            new_stats = {"$set": {'credits': tr + stats['credits'],
                                  'crytime': time.time()}}
            await server.update_one(stats, new_stats)
        else:
            desc = f"You can't cry rn. Let your eyes hydrate.\n\
Wait for like {round((10800 - time.time()+stats['crytime'])//3600)} hours or something."
            colo = COLOR.ERROR
        embed = Embed(title="**Tear Dispenser**",
                      description=desc,
                      color=colo)
        embed.set_footer(text='😭')
        await ctx.send(embed=embed)

    @commands.command(aliases=['vaultoftears', 'tearvault'])
    async def vault(self, ctx: Context, member: Member = None):
        '''Gives the users economy balance'''
        user = ctx.message.author if not member else member
        server = self.DB_CLIENT.users_db[str(user.guild.id)]
        stats = await server.find_one({'id': user.id})
        trp = stats['credits']
        embed = Embed(
            title='**Vault of Tears**',
            description=f"Opening {user}'s vault-of-tears....",
            colour=COLOR.ECONOMY)
        embed.set_footer(
            text='Cry, cry, let the emotions flow through you...😭')
        embed.add_field(name='Tears', value=trp)
        await ctx.send(embed=embed)

    @commands.command(aliases=['lvl', 'dep_level'])
    async def level(self, ctx: Context, member: Member = None):
        '''Gives the users level'''
        user = ctx.message.author if not member else member
        server = self.DB_CLIENT.users_db[str(user.guild.id)]
        stats = await server.find_one({'id': user.id})
        lvl = stats['level']
        embed = Embed(
            title=f'**Depression-Level of {user}**',
            description="._.",
            colour=COLOR.LEVELLING)
        embed.set_footer(
            text='Cry, cry, let the emotions flow through you...😭')
        embed.add_field(name='Level', value=lvl)
        await ctx.send(embed=embed)

    @commands.command(aliases=['absorb', 'cryon'])
    async def transfer(self, ctx: Context, amount: int, member: Member):
        '''transfer command'''
        user1 = ctx.message.author
        user2 = member
        server = self.DB_CLIENT.users_db[str(user1.guild.id)]
        stat1 = await server.find_one({'id': user1.id})
        await update_data(user2)
        stat2 = await server.find_one({'id': user2.id})
        bal1 = stat1['credits'] - amount
        if bal1 >= 0:
            await server.update_one(stat1, {"$set": {'credits': bal1}})
            await server.update_one(stat2, {"$inc": {'credits': amount}})
            embed = Embed(
                title='**Heart_to_heart**',
                description=f"You tried to cry tears for {member}",
                colour=COLOR.ECONOMY)
            embed.set_footer(
                text='Cry, cry, let the emotions flow through you...😭')
            embed.add_field(
                name=f"You handed out a vial of {amount} tears to {member}",
                value="._.")
        else:
            embed = Embed(
                title='**Heart_to_heart**',
                description=f"You tried to cry tears for {member}",
                colour=COLOR.ERROR)
            embed.set_footer(
                text='Cry, cry, let the emotions flow through you...😭')
            embed.add_field(
                name=f"Failed to share {amount} tears.\nYou have insufficient tears in TearVault",
                value="._.")
        await ctx.send(embed=embed)


""" The marketplace ---> TODO
@commands.command(aliases=['market'])
async def shop(self, ctx: Context):
    '''market command'''
    items= []
    embed=discord.Embed(title='**TearShops**',description = f'items',colour=discord.Color.red())"""


def setup(client):
    client.add_cog(Economy(client))
