import random
import discord
from discord.ext import commands
from .inputs import responses, fortunes, quo, nerd, tech, rost, bk, cmp, blurt, jk
from .utils import COLOR


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def magicball(self, ctx, *, question):
        embed = discord.Embed(title="8Ball :8ball:",
                              colour=COLOR.DEFAULT)
        embed.add_field(name=f"*Question: {question}*",
                        value=f"Conjecture: {random.choice(responses)}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["future"])
    async def fortune(self, ctx):
        embed = discord.Embed(title='Fortune', color=COLOR.DEFAULT)
        embed.add_field(name='Your Fortune', value=random.choice(fortunes))
        await ctx.send(embed=embed)

    @commands.command(aliases=['wisdom'])
    async def quote(self, ctx):
        randq = random.choice(list(quo.keys()))
        quote_text = f'`{randq}`\n_~{quo[randq]}_'
        embed = discord.Embed(
            title='Quote',
            description=quote_text,
            color=COLOR.RANDOM())
        await ctx.send(embed=embed)

    @commands.command(aliases=['joke', 'pun'])
    async def dadjoke(self, ctx):
        embed = discord.Embed(title='Dad joke huh 😏', color=COLOR.RANDOM())
        embed.add_field(name=random.choice(jk),
                        value='_looks at you, expecting you to laugh_')
        await ctx.send(embed=embed)

    @commands.command(aliases=['nerdystuff', 'smartystuff', 'bigbrains'])
    async def nerd(self, ctx):
        embed = discord.Embed(title='Nerdy Stuff', color=COLOR.JOY)
        embed.add_field(
            name='Take this you NERD',
            value=f'{random.choice(nerd)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['tehc', 'hackerman'])
    async def geek(self, ctx):
        embed = discord.Embed(title='Geek', color=COLOR.JOY)
        embed.add_field(name="Ahh I am a hackerman",
                        value=f'{random.choice(tech)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def roast(self, ctx, *, member: discord.Member = None):
        user = ctx.message.author if not member else member
        embed = discord.Embed(title='Roast', color=COLOR.SADNESS)
        embed.add_field(name='😈', value=f'{user}, {random.choice(rost)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['commend'])
    async def compliment(self, ctx, *, member: discord.Member = None):
        user = ctx.message.author if not member else member
        embed = discord.Embed(title='Compliment', color=COLOR.JOY)
        embed.add_field(name="Here's a compliment for you",
                        value=f'{user}, {random.choice(cmp)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def flirt(self, ctx, *, member: discord.Member = None):
        user = ctx.message.author if not member else member
        embed = discord.Embed(title='Flirt', color=COLOR.DEFAULT)
        embed.add_field(name='Flirt it away',
                        value=f'{user}, {random.choice(blurt)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['goodread'])
    async def book(self, ctx):
        embed = discord.Embed(title='Book', color=COLOR.JOY)
        embed.add_field(name="Here's a book recomendation: ",
                        value=f'{random.choice(bk)}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
