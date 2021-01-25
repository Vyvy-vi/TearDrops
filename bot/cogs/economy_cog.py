import time
import random
import discord
from discord.ext import commands
from pymongo import MongoClient


from utils import get_environment_variable
from .utils import COLOR

MONGO_CONNECTION_STRING = get_environment_variable("MONGO_CONNECTION_STRING")
DB_CLIENT = MongoClient(MONGO_CONNECTION_STRING)
db = DB_CLIENT.get_database('users_db')

timelast = 0


async def update_data(user):
    '''
    This Updates the user data in the db to add entry for new members
    '''
    if str(user.guild.id) not in db.list_collection_names():
        server = db[str(user.guild.id)]
        server.insert_one({'server_name': user.guild.name,
                           'server_id': user.guild.id})
        server.insert_one({'id': user.id, 'experience': 0,
                           'level': 1, 'credits': 0, 'crytime': 0})
        print(f'{user.guild.name} : {user.guild.id} added to database')
        print(f'{user.id} added to database...')
    else:
        server = db[str(user.guild.id)]
        # print(list(server.find({'id':user.id}))[-1].values())
        try:
            if len(list(server.find({'id': user.id}))) == 0:
                server.insert_one(
                    {'id': user.id, 'experience': 0, 'level': 1, 'credits': 0, 'crytime': 0})
                print(f'{user.id} added to database')
            elif user.id not in list(server.find({'id': user.id}))[-1].values():
                server.insert_one(
                    {'id': user.id, 'experience': 0, 'level': 1, 'credits': 0, 'crytime': 0})
                print(f'{user.id} added to database')
        except BaseException:
            print('Some error occured')


async def add_experience(message, user, exp):
    """Adds xp to the user in the database, and calls the level up function"""
    server = db[str(user.guild.id)]
    stats = list(server.find({'id': user.id}))
    exp = stats[-1]['experience'] + exp
    new_stats = {"$set": {'experience': exp}}
    server.update_one(stats[-1], new_stats)
    await level_up(message.author, message.channel)


async def level_up(user, channel):
    """Takes care of checking the level-up parameters to boot ppl to next level when sufficient xp obtained"""
    server = db[str(user.guild.id)]
    stats = list(server.find({'id': user.id}))
    lvl_start = stats[-1]['level']
    experience = stats[-1]['experience']
    x = 35
    cnt = 1
    while x < experience:
        x = 2 * x + 10
        cnt += 1

    lvl_end = cnt - 1 if experience >= x else lvl_start
    if lvl_start < lvl_end:
        new_stats = {"$set": {'level': lvl_end}}
        server.update_one(stats[-1], new_stats)
        ls = lvl_end * 150
        server = db[str(user.guild.id)]
        stats = list(server.find({'id': user.id}))
        cred = stats[-1]['credits'] + ls
        new_stats = {"$set": {'credits': cred}}
        server.update_one(stats[-1], new_stats)
        embed = discord.Embed(
            title=f'{user} has leveled up to {lvl_end}.',
            description=f'You have been given {ls} tears for your active-ness.\n\
Saving {ls} tears in your vault of tears.',
            color=COLOR.LEVELLING)
        embed.set_footer(text='😭')
        await channel.send(embed=embed)


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        '''
        Event triggered when a new member enters server
        This prints the message out on Terminal.
        Also, this awaits the update_data() function, to add member to the database.
        '''
        print(f'{member} has joined the server.....')
        await update_data(member)

    @commands.Cog.listener()
    async def on_message(self, message):
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
            await update_data(message.author)
            timlst = timelast
            if time.time() - timlst > 25:
                await add_experience(message, message.author, 10)
                timelast = time.time()
            # message if-else response examples(you can add more)
            if 'tears' in message.content:
                await message.author.send('😭')  # dms

        # prevents commands from not being processed

    @commands.command(aliases=['daily'])
    async def cry(self, ctx):
        '''credit gain command for crying'''
        user = ctx.message.author
        server = db[str(user.guild.id)]
        stats = list(server.find({'id': user.id}))
        tim = stats[-1]['crytime']
        if time.time() - tim > 10800:
            trs = [
                0,
                100,
                150,
                150,
                200,
                100,
                50,
                250,
                500,
                200,
                1,
                200,
                150,
                100]
            tr = random.choice(trs)
            if tr > 1:
                embed = discord.Embed(
                    title='**Tear Dispenser**',
                    description=f'You cried {tr} tears.\n\
Storing them in the vaults of tears.Spend them wisely...💦\nSpend them wisely...',
                    color=COLOR.DEFAULT)
                embed.set_footer(text='😭')
            elif tr == 1:
                embed = discord.Embed(
                    title='**Tear Dispenser**',
                    description='You really tried but only 1 tear came out...\n\
Storing it in the vaults of tears.Spend them wisely...💧\nSpend it wisely...',
                    color=COLOR.DEFAULT)
                embed.set_footer(text='😭')
            else:
                tr2 = [
                    'You were not sad',
                    'You were surprisingly too happy to cry',
                    'You cried so much already that the tears are not coming out',
                    'You really tried but you could not cry',
                    'The tears are not coming out...']
                message = random.choice(tr2)
                embed = discord.Embed(
                    title='**Tear Dispenser**',
                    description=f"You can't cry rn.{message}",
                    color=COLOR.ERROR)
                embed.set_footer(text='😭')
                embed.add_field(
                    name='Try again after like 3 hours.',
                    value='oof',
                    inline=False)
            await ctx.send(embed=embed)
            cred = tr + stats[-1]['credits']
            new_stats = {"$set": {'credits': cred, 'crytime': time.time()}}
            server.update_one(stats[-1], new_stats)
        else:
            embed = discord.Embed(
                title='**Tear Dispenser**',
                description=f"You can't cry rn. Let your eyes hydrate.\n\
Wait for like {round((10800 - time.time()+tim)//3600)} hours or something.",
                color=COLOR.ECONOMY)
            embed.set_footer(text='😭')
            await ctx.send(embed=embed)

    @commands.command(aliases=['vaultoftears', 'tearvault'])
    async def vault(self, ctx, member: discord.Member = None):
        '''Gives the users economy balance'''
        user = ctx.message.author if not member else member
        server = db[str(user.guild.id)]
        stats = server.find({'id': user.id})
        trp = list(stats)[-1]['credits']
        embed = discord.Embed(
            title='**Vault of Tears**',
            description=f"Opening {user}'s vault-of-tears....",
            colour=COLOR.ECONOMY)
        embed.set_footer(
            text='Cry, cry, let the emotions flow through you...😭')
        embed.add_field(name='Tears', value=trp)
        await ctx.send(embed=embed)

    @commands.command(aliases=['lvl', 'dep_level'])
    async def level(self, ctx, member: discord.Member = None):
        '''Gives the users level'''
        user = ctx.message.author if not member else member
        server = db[str(user.guild.id)]
        stats = server.find({'id': user.id})
        lvl = list(stats)[-1]['level']
        embed = discord.Embed(
            title=f'**Depression-Level of {user}**',
            description="._.",
            colour=COLOR.LEVELLING)
        embed.set_footer(
            text='Cry, cry, let the emotions flow through you...😭')
        embed.add_field(name='Level', value=lvl)
        await ctx.send(embed=embed)

    @commands.command(aliases=['share', 'send', 'cryon'])
    async def transfer(self, ctx, amount: int, member: discord.Member):
        '''transfer command'''
        user1 = ctx.message.author
        user2 = member
        server = db[str(user1.guild.id)]
        stat1 = list(server.find({'id': user1.id}))
        bal1 = stat1[-1]['credits'] - amount
        if bal1 >= 0:
            new_stat1 = {"$set": {'credits': bal1}}
            server.update_one(stat1[-1], new_stat1)

            stat2 = list(server.find({'id': user2.id}))
            bal2 = stat2[-1]['credits'] + amount
            new_stat2 = {"$set": {'credits': bal2}}
            server.update_one(stat2[-1], new_stat2)
            embed = discord.Embed(
                title='**Heart_to_heart**',
                description=f"You tried to cry tears for {member}",
                colour=COLOR.ECONOMY)
            embed.set_footer(
                text='Cry, cry, let the emotions flow through you...😭')
            embed.add_field(
                name=f"You handed out a vial of {amount} tears to {member}",
                value="._.")

        else:
            embed = discord.Embed(
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
async def shop(self, ctx):
    '''market command'''
    items= []
    embed=discord.Embed(title='**TearShops**',description = f'items',colour=discord.Color.red())"""


def setup(client):
    client.add_cog(Economy(client))
