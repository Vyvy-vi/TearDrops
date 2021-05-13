import random

import motor.motor_asyncio as motor

from discord import Embed, Member
from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.data = motor.AsyncIOMotorClient(client.MONGO).DATA.inputs

    @commands.command(aliases=["8ball"])
    async def magicball(self, ctx: Context, *, question: str):
        """Use an 8ball"""
        res = await self.data.find_one({'type': '8ball'})
        embed = Embed(title="8Ball :8ball:",
                      colour=COLOR.DEFAULT)
        embed.add_field(name=f"*Question: {question}*",
                        value=f"Conjecture: {random.choice(res['text'])}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["future"])
    async def fortune(self, ctx: Context):
        """Gives you your terrible fortune"""
        res = await self.data.find_one({'type': 'fortunes'})
        embed = Embed(title='Fortune', color=COLOR.DEFAULT)
        embed.add_field(name='Your Fortune', value=random.choice(res['text']))
        await ctx.send(embed=embed)

    @commands.command(aliases=['wisdom'])
    async def quote(self, ctx: Context):
        """Gives you a dose of motivational quotes"""
        res = await self.data.find_one({'type': 'quotes'})
        randq = random.choice(list(res['text'].keys()))
        quote_text = f"`{randq.replace('|', '.')}`\n_~{res['text'][randq]}_"
        embed = Embed(
            title='Quote',
            description=quote_text,
            color=COLOR.RANDOM())
        await ctx.send(embed=embed)

    @commands.command(aliases=['joke', 'pun'])
    async def dadjoke(self, ctx: Context):
        """Gives you some dad puns"""
        res = await self.data.find_one({'type': 'puns'})
        embed = Embed(title='Dad joke huh 😏', color=COLOR.RANDOM())
        embed.add_field(name=random.choice(res['text']),
                        value='_looks at you, expecting you to laugh_')
        await ctx.send(embed=embed)

    @commands.command(aliases=['nerdystuff', 'smartystuff', 'bigbrains'])
    async def nerd(self, ctx: Context):
        """Returns some nerdy stuff"""
        res = await self.data.find_one({'type': 'nerd'})
        embed = Embed(title='Nerdy Stuff', color=COLOR.JOY)
        embed.add_field(
            name='Take this you NERD',
            value=random.choice(res['text']))
        await ctx.send(embed=embed)

    @commands.command(aliases=['tehc', 'hackerman'])
    async def geek(self, ctx: Context):
        """Returns some geeky gibberish"""
        res = await self.data.find_one({'type': 'tech'})
        embed = Embed(title='Geek', color=COLOR.JOY)
        embed.add_field(name="Ahh I am a hackerman",
                        value=random.choice(res['text']))
        await ctx.send(embed=embed)

    @commands.command(aliases=['commend'])
    async def compliment(self, ctx: Context, *, member: Member = None):
        """Wanna shoot some compliments?"""
        user = ctx.message.author if not member else member
        res = await self.data.find_one({'type': 'compliments'})
        embed = Embed(title='Compliment', color=COLOR.JOY)
        embed.add_field(name="Here's a compliment for you",
                        value=f"{user}, {random.choice(res['text'])}")
        await ctx.send(embed=embed)

    @commands.command()
    async def flirt(self, ctx: Context, *, member: Member = None):
        """Flirting with bots is nice"""
        user = ctx.message.author if not member else member
        res = await self.data.find_one({'type': 'flirts'})
        embed = Embed(title='Flirt', color=COLOR.DEFAULT)
        embed.add_field(name='Flirt it away',
                        value=f"{user}, {random.choice(res['text'])}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['goodread'])
    async def book(self, ctx: Context):
        """Returns you some epic book recomendation"""
        res = await self.data.find_one({'type': 'books'})
        embed = Embed(title='Book', color=COLOR.JOY)
        embed.add_field(name="Here's a book recomendation: ",
                        value=random.choice(res['text']))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
