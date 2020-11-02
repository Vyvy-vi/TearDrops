# TODO - transfer, casino, etc commands


import aiohttp
import time
import random
import wikipedia
from inputs import responses, fortunes, quo, nerd, tech, rost, bk, cmp, blurt, cf, jk, cfe, chill, cl, ur
import os
import ssl
import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()

# temp->

# modules for wiki and wolfram queries
# import wolframalpha
# import requests

# Standard modules

# TOKEN, MONGO URI are env-vars


DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
MONGO_TEARS = os.getenv("MONGO_TEARS")
MONGO_TEARS_PASS = os.getenv("MONGO_TEARS_PASS")
print('fetched Tokens from env-vars')

# mongoDB Client
link = f'mongodb+srv://{MONGO_TEARS}:{MONGO_TEARS_PASS}@cluster0.ls3h6.mongodb.net/users_db?retryWrites=true&w=majority'

DB_CLIENT = MongoClient(link)
db = DB_CLIENT.get_database('users_db')

print(db.list_collection_names())
timelast = 0
timecheck = 0
buls = 0
ssl._create_default_https_context = ssl._create_unverified_context

# intents (new discord feature to limit bots to certain bucket events)
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# NOTE- The initial version of the bot used TinyDB, but I've migrated to MongoDB (still considering sql tho)

# client pointer for API-reference
client = commands.Bot(command_prefix='qq ',
                      case_insensitive=True, intents=intents)

# discord.py has an inbuilt help command, which doesn't look good''
client.remove_command('help')


# status-change-cycle(The bot changes presence after a few mins.)
STATUS = cycle([
    "qq help | :(",
    "with your heart"
    "in tears",
    "with tears",
    "with ",
    "I'm so sad",
    "with your tears...",
    "with your feelings",
    "with sparkles"])


@client.event
async def on_ready():
    '''
    This prints a message when the on_ready event is detected.
    That is, when the bot logs onto discord when the script is ran.
    '''

    change_status.start()  # Triggers status change task

    print("Processing.....")
    print("|||||||||||||||")
    print("Bot has Successfully logged onto Discord...")
    print('Successfully logged in as {0.user}...'.format(client))
    # client.user gives the bots discord username tag
    print([guild.id for guild in client.guilds])


@client.event
async def on_guild_join(guild):
    '''
    This sends a message in the main channel, when the bot joins a guild.
    Joining a guild is synonymous to joining a server.
    Basically, a hi message the bot sends on enterring the server.
    '''

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            if guild.id not in db.list_collection_names():
                col = db[str(guild.id)]
                col.insert_one(
                    {'server_name': guild.name, 'server_id': guild.id})
            icon_url = 'https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png'
            embed = discord.Embed(title='**Tear Drops:tm:**', description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license, I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes', colour=discord.Color.purple(), url='https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
            embed.set_footer(text='I Hope that you enjoyed the bot....😭')
            embed.set_image(url=icon_url)
            await channel.send(embed=embed)
        break
    print(f'Entered server {guild.name} : {guild.id}')


@tasks.loop(seconds=600)
async def change_status():
    '''
    loops through the cycle of the STATUS list and sets that as bot presence
    '''
    await client.change_presence(activity=discord.Game(next(STATUS)))
    # NOTE- There are other methods, that can be utilised instead of just 'playing'


@client.event
async def on_member_join(member):
    '''
    Event triggered when a new member enters server
    This prints the message out on Terminal.
    Also, this awaits the update_data() function, to add member to the database.
    '''
    print(f'{member} has joined the server.....')
    await update_data(member)


@client.event
async def on_member_remove(member):
    '''
    Event triggered when a member leaves the server
    NOTE- This can also be displayed on the server
    '''
    print(f'{member} has left the server......')


@client.event
async def on_message(message):
    '''
    Event triggered when a message is sent on the server
    This is associated with a few if-else responses(you can add more by looking at the examples)
    And finally, this triggers client.process_commands() which registers bot commands.
    '''
    if message.author == client.user:
        # self-ignore, to prevent responses to self
        return
    elif(message.author.bot):
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
        if message.content.startswith('owo'):
            await message.channel.send('uwu')
        elif message.content.startswith('hi' or 'hey'):
            await message.channel.send('Hi there!👋')
        elif 'bitch' in message.content:
            await message.author.send('**BIRCH**')  # dms
        elif 'tears' in message.content:
            await message.channel.send('😭')

    # prevents commands from not being processed
    await client.process_commands(message)


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
        except Exception as e:
            print(e)


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
    while (x < experience):
        x = 2 * x + 10
        cnt += 1

    if experience >= x:
        lvl_end = cnt - 1
    else:
        lvl_end = lvl_start

    if lvl_start < lvl_end:
        new_stats = {"$set": {'level': lvl_end}}
        server.update_one(stats[-1], new_stats)
        ls = lvl_end * 150
        server = db[str(user.guild.id)]
        stats = list(server.find({'id': user.id}))
        cred = stats[-1]['credits'] + ls
        new_stats = {"$set": {'credits': cred}}
        server.update_one(stats[-1], new_stats)
        embed = discord.Embed(title=f'{user} has leveled up to {lvl_end}.', description=f'You have been given {ls} tears for your active-ness.\n\
Saving {ls} tears in your vault of tears.', color=discord.Color.teal())
        embed.set_footer(text='😭')
        await channel.send(embed=embed)


@client.command()
async def ping(ctx):
    """The bot's ping command"""
    phrase = ['I am alive...',
              'I was definitely not sleeping...',
              'I was definitely not laughing...',
              'I am still here',
              'You are using a ping command? Why?',
              'At your service.']
    ph = random.choice(phrase)
    lsm = round((client.latency) * 100)
    embed = discord.Embed(
        title='**pong...!**', description=f"_{ph}_ \n**~{lsm} ms taken**......", color=discord.Color.gold())
    embed.set_footer(text='😭')
    await ctx.send(embed=embed)


@client.command()
async def pong(ctx):
    """The bot's pong command"""
    phrase = ["I am aliven't...",
              "I was sleeping...",
              "I was laughing...",
              "I am still not here",
              "You are using a pong command? Why?",
              "Not at your service."]
    ph = random.choice(phrase)
    lsm = round((client.latency) * 100)
    embed = discord.Embed(
        title='**PING...!**', description=f"_{ph}_ \n**~{lsm} ms taken**......", color=discord.Color.red())
    embed.set_footer(text='😭')
    await ctx.send(embed=embed)


@client.command()
async def help(ctx, command_name=None, *args):
    '''This command Ofc'''
    if command_name is None:
        embed = discord.Embed(
            title='**Help command**', description='All commands of bot ;-; with description', color=discord.Color.dark_orange())
        for command in client.commands:
            embed.add_field(
                name=f'{command}', value=f'`{command.short_doc}.`', inline=False)
        await ctx.send(embed=embed)
    else:
        for command in client.commands:
            if command_name == command.name:
                embed = discord.Embed(
                    title=f'**Help command: {command}**', description=f'Description : {command.short_doc} \n {command.brief}', color=discord.Color.dark_orange())
                await ctx.send(embed=embed)


@client.command(aliases=['daily'])
async def cry(ctx):
    '''credit gain command for crying'''
    user = ctx.message.author
    server = db[str(user.guild.id)]
    stats = list(server.find({'id': user.id}))
    trs = [0, 100, 150, 150, 200, 100, 50, 250, 500, 200, 1, 200, 150, 100]
    tim = stats[-1]['crytime']
    if time.time() - tim > 10800:
        tr = random.choice(trs)
        if tr > 1:
            embed = discord.Embed(title='**Tear Dispenser**', description=f'You cried {tr} tears.\n\
Storing them in the vaults of tears.Spend them wisely...💦\nSpend them wisely...', color=discord.Color.blue())
            embed.set_footer(text='😭')
            await ctx.send(embed=embed)
        elif tr == 1:
            embed = discord.Embed(title='**Tear Dispenser**', description='You really tried but only 1 tear came out...\n\
Storing it in the vaults of tears.Spend them wisely...💧\nSpend it wisely...', color=discord.Color.blue())
            embed.set_footer(text='😭')
            await ctx.send(embed=embed)
        else:
            tr2 = [
                'You were not sad',
                'You were surprisingly too happy to cry',
                'You cried so much already that the tears are not coming out',
                'You really tried but you could not cry',
                'The tears are not coming out...']
            message = random.choice(tr2)
            embed = discord.Embed(
                title='**Tear Dispenser**', description=f"You can't cry rn.{message}", color=discord.Color.blue())
            embed.set_footer(text='😭')
            embed.add_field(name='Try again after like 3 hours.',
                            value='oof', inline=False)
            await ctx.send(embed=embed)
        cred = tr + stats[-1]['credits']
        new_stats = {"$set": {'credits': cred, 'crytime': time.time()}}
        server.update_one(stats[-1], new_stats)
    else:
        embed = discord.Embed(title='**Tear Dispenser**', description=f"You can't cry rn. Let your eyes hydrate.\n\
Wait for like {round((10800 - time.time()+tim)//3600)} hours or something.", color=discord.Color.blue())
        embed.set_footer(text='😭')
        await ctx.send(embed=embed)


@client.command(aliases=['vaultoftears', 'tearvault'])
async def vault(ctx, member: discord.Member = None):
    '''Gives the users economy balance'''
    if not member:
        user = ctx.message.author
    else:
        user = member
    server = db[str(user.guild.id)]
    stats = server.find({'id': user.id})
    trp = list(stats)[-1]['credits']
    embed = discord.Embed(title='**Vault of Tears**',
                          description=f"Opening {user}'s vault-of-tears....", colour=discord.Color.blurple())
    embed.set_footer(text='Cry, cry, let the emotions flow through you...😭')
    embed.add_field(name='Tears', value=trp)
    await ctx.send(embed=embed)


@client.command(aliases=['lvl', 'dep_level'])
async def level(ctx):
    '''Gives the users level'''
    user = ctx.message.author
    server = db[str(user.guild.id)]
    stats = server.find({'id': user.id})
    lvl = list(stats)[-1]['level']
    embed = discord.Embed(title='**Depression-Level**',
                          description="._.", colour=discord.Color.blurple())
    embed.set_footer(text='Cry, cry, let the emotions flow through you...😭')
    embed.add_field(name='Level', value=lvl)
    await ctx.send(embed=embed)


@client.command(aliases=['share', 'send', 'cryon'])
async def transfer(ctx, amount: int, member: discord.Member):
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
        embed = discord.Embed(title='**Heart_to_heart**',
                              description=f"You tried to cry tears for {member}",
                              colour=discord.Color.green())
        embed.set_footer(
            text='Cry, cry, let the emotions flow through you...😭')
        embed.add_field(
            name=f"You handed out a vial of {amount} tears to {member}", value="._.")

    else:
        embed = discord.Embed(title='**Heart_to_heart**',
                              description=f"You tried to cry tears for {member}",
                              colour=discord.Color.green())
        embed.set_footer(
            text='Cry, cry, let the emotions flow through you...😭')
        embed.add_field(
            name=f"Failed to share {amount} tears.\nYou have insufficient tears in TearVault", value="._.")
    await ctx.send(embed=embed)


"""
@client.command(aliases=['market'])
async def shop(ctx):
    '''market command'''
    items= []
    embed=discord.Embed(title='**TearShops**',description = '',colour=discord.Color.red())
"""


@client.command(aliases=['botwhat'])
async def botinfo(ctx):
    '''Gives info about the bot'''
    embed = discord.Embed(title='**Tear Drops:tm:**', description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license, I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes', colour=discord.Color.purple(), url='https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
    embed.set_footer(text='I Hope that you enjoyed the bot....😭')
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def echo(ctx, *args):
    '''echos the words'''
    output = ''
    for word in args:
        output += word
        output += ' '
    print(ctx.message.author.id)
    if ctx.message.author.id == 558192816308617227:
        for i in range(3):
            await ctx.send(output)
    else:
        await ctx.send(output)


@client.command(pass_context=True)
async def say(ctx, *args):
    """Gives the user's statement a nice richtext quote format"""
    output = ''
    for word in args:
        output += word
        output += ' '
    user = ctx.message.author
    embed = discord.Embed(
        title=f'{output}', description=f'~{user}', colour=discord.Color.greyple())
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def urban(ctx, *args):
    '''searches urban dictionary for words'''
    baseurl = "https://www.urbandictionary.com/define.php?term="
    output = ''
    for word in args:
        output += word
    await ctx.send(baseurl + output)


@client.command(pass_context=True)
async def define(ctx, *args):
    '''searches merriam-webster for meanings of words'''
    baseurl = "https://www.merriam-webster.com/dictionary/"
    output = ''
    for word in args:
        output += word
        output += '%20'
    await ctx.send(baseurl + output)


@client.command(aliases=['diceroll', 'roll'])
async def dice(ctx, amount: int):
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
                title='Dice-roll...🎲', description=f'The dice rolled a {numtemp}.\nYou have been awarded 50 tears for this...', color=discord.Color.dark_red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Dice-roll...🎲', description=f'The dice rolled a {numtemp}.\n\
Your prediction was wrong. 😖', color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title='Dice-roll...🎲', description='Please enter a valid number argument.\n\
Command Usage-> qq dice <num> (between 1 and 6)', color=discord.Color.dark_red())
        await ctx.send(embed=embed)


@client.command(pass_context=True)
async def user(ctx, user: discord.Member):
    '''gives user info'''
    embed = discord.Embed(title="{}'s info".format(
        user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name='Account Created on', value=user.created_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)


@client.command(aliases=['russian-roulette', 'gunshot', 'rr'])
async def russian_roulette(ctx):
    '''starts fun russian roulette game'''
    global buls
    if buls >= 6:
        buls = 0
        embed = discord.Embed(title='Russian Roulette.🔫',
                              description='All you remember is the pain you felt when the bullet pierced your skull.', color=discord.Color.light_gray())
    else:
        buls += 1
        embed = discord.Embed(title='Russian Roulette.🔫',
                              description='You live to fight another day', color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def wiki(ctx, *args):
    '''Displays wikipedia info about given arguments'''
    qu = ' '.join(list(args))
    searchResults = wikipedia.search(qu)
    if not searchResults:
        embed = discord.Embed(
            title=f'**{qu}**', description='It appears that there is no instance of this in Wikipedia index...', colour=discord.Color.dark_red())
        embed.set_footer(text='Powered by Wikipedia...')
        await ctx.send(embed=embed)
    else:
        try:
            page = wikipedia.page(searchResults[0])
            pg = 0
        except wikipedia.DisambiguationError as err:
            page = wikipedia.page(err.options[0])
            pg = err.options
        wikiTitle = str(page.title.encode('utf-8'))
        wikiSummary = page.summary
        embed = discord.Embed(title=f'**{wikiTitle[1:]}**', description=str(
            wikiSummary[1:900]) + '...', color=discord.Color.dark_orange(), url=page.url)
        embed.set_footer(text='Powered by Wikipedia...')
        if pg != 0:
            s = pg[1:10] + ['...']
            s = ','.join(s)
            embed.add_field(name='Did you mean?:', value=s)
        embed.set_image(url=page.images[0])
        await ctx.send(embed=embed)


@client.command(aliases=['meme'])
async def memes(ctx):
    """Get the dankest memes Reddit has to offer."""
    async with aiohttp.ClientSession() as session:
        url = "https://meme-api.herokuapp.com/gimme"
        async with session.get(url) as response:
            response = await response.json()
        embed = discord.Embed(
            title=response['title'], url=response['postLink'], color=discord.Color.dark_orange())
        embed.set_image(url=response['url'])
        embed.set_footer(
            text=f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes!")
        await ctx.send(embed=embed)


# ---> NEEDS FIXING <---
@client.command()
async def automeme(ctx):
    '''Triggers the automeme taskloop for the channel context'''
    automeme_routine.start(ctx)


@tasks.loop(seconds=600)
async def automeme_routine(ctx):
    '''
    sends a meme every 10 mins
    '''
    async with aiohttp.ClientSession() as session:
        url = "https://meme-api.herokuapp.com/gimme"
        async with session.get(url) as response:
            response = await response.json()
        embed = discord.Embed(
            title=response['title'], url=response['postLink'], color=discord.Color.dark_orange())
        embed.set_image(url=response['url'])
        embed.set_footer(
            text=f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes!")
        await ctx.send(embed=embed)
    # NOTE- There are other methods, that can be utilised instead of just 'playing'


@client.command(aliases=["8ball", "seer"])
async def magicball(ctx, *, question):
    embed = discord.Embed(title="8Ball :8ball:", color=discord.Color.magenta())
    embed.add_field(name=f"*Question: {question}*",
                    value=f'Conjecture: {random.choice(responses)}')
    await ctx.send(embed=embed)


@client.command(aliases=['future'])
async def fortune(ctx):
    embed = discord.Embed(title='Fortune', color=0x09b58d)
    embed.add_field(name='Your Fortune', value=random.choice(fortunes))
    await ctx.send(embed=embed)


@client.command(aliases=['phrase', 'wisdom'])
async def quote(ctx):
    embed = discord.Embed(title='Quote', color=0x0973b5)
    embed.add_field(name='Quote for you', value=f'`{random.choice(quo)}`')
    await ctx.send(embed=embed)


@client.command(aliases=['joke', 'pun', 'badjoke'])
async def dadjoke(ctx):
    embed = discord.Embed(title='Dad Jokes huh 😏', color=0x5511c2)
    embed.add_field(name='Your Fortune', value=random.choice(jk))
    await ctx.send(embed=embed)


@client.command(aliases=['smartstuff'])
async def nerdystuff(ctx):
    embed = discord.Embed(title='Nerdy Stuff', color=0x22bfb0)
    embed.add_field(name='Take this you NERD', value=f'{random.choice(nerd)}')
    await ctx.send(embed=embed)


@client.command(aliases=['techie', 'hackerman', 'pimp'])
async def geek(ctx):
    embed = discord.Embed(title='Geek', color=0xc21155)
    embed.add_field(name='Ahh I love geeky stuff too',
                    value=f'{random.choice(tech)}')
    await ctx.send(embed=embed)


@client.command(aliases=['shame', 'destroy'])
async def roast(ctx, *, link):
    embed = discord.Embed(title='Roast', color=0x11ad4b)
    embed.add_field(name='😈', value=f'{link} , {random.choice(rost)}')
    await ctx.send(embed=embed)


@client.command(aliases=['appreciate', 'commend'])
async def compliment(ctx, *, link):
    embed = discord.Embed(title='Compliment', color=0xa9e010)
    embed.add_field(name="Here's a compliment for you",
                    value=f'{link} , {random.choice(cmp)}')
    await ctx.send(embed=embed)


@client.command()
async def flirt(ctx, *, link):
    embed = discord.Embed(title='Flirt', color=0xcf8c11)
    embed.add_field(name='Flirt it away',
                    value=f'{link} , {random.choice(blurt)}')
    await ctx.send(embed=embed)


@client.command(aliases=['goodread', 'read'])
async def book(ctx):
    embed = discord.Embed(title='Books', color=0xbf2b11)
    embed.add_field(name='Some books for you', value=f'{random.choice(bk)}')
    await ctx.send(embed=embed)


@client.command(aliases=['ask_out'])
async def wannagrabacoffee(ctx, *, link):
    embed = discord.Embed(
        title=f'{link}, Someone wants to grab a coffee with you...*wink *wink', color=0x11bf51)
    embed.add_field(name='This happened....', value=f'{random.choice(cf)}')
    embed.add_field(name='not actually')
    await ctx.send(embed=embed)


@client.command(aliases=['brew'])
async def coffee(ctx):
    op = f'{random.choice(cfe)}'
    embed = discord.Embed(title='Coffee',
                          description=op,
                          color=discord.Color.red())
    embed.set_footer(text=f'Caffeiene Level-{random.choice(cl)}.{random.choice(chill)}')
    embed.set_image(url=random.choice(ur))
    await ctx.send(embed=embed)


# error_handling
@client.event
async def on_command_error(ctx, error):
    # TODO- Error Handling
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used..... ")
    else:
        await ctx.send(error)

# Running the BOT:
client.run(str(DISCORD_BOT_TOKEN))
