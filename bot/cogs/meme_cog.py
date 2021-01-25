import discord
from discord.ext import commands, tasks
import aiohttp

from .utils import COLOR

# Map of channel IDs to tasks.Loop automeme loops
automeme_loops = {}


async def automeme_routine(ctx):
    '''sends a meme every 10 mins'''
    async with aiohttp.ClientSession() as session:
        url = "https://meme-api.herokuapp.com/gimme"
        async with session.get(url) as response:
            response = await response.json()
        embed = discord.Embed(
            title=response['title'],
            url=response['postLink'],
            color=COLOR.JOY)
        embed.set_image(url=response['url'])
        embed.set_footer(
            text=f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes!")
        await ctx.send(embed=embed)


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['meme'])
    async def memes(self, ctx, param: str = None):
        sub = '/' if param is None else '/' + str(param)
        async with aiohttp.ClientSession() as session:
            url = "https://meme-api.herokuapp.com/gimme" + sub
            async with session.get(url) as response:
                response = await response.json()
            embed = discord.Embed(
                title=response['title'],
                url=response['postLink'],
                color=COLOR.JOY)
            embed.set_image(url=response['url'])
            txt = f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes"
            embed.set_footer(text=txt)
            await ctx.send(embed=embed)

    @commands.command()
    async def automeme(self, ctx):
        '''Triggers the automeme taskloop for the channel context'''
        channel_id = ctx.channel.id
        if channel_id in automeme_loops:
            await ctx.send('Automeme already running here')
        else:
            # using decorator instead of tasks.Loop directly to preserve
            # default arguments
            loop = tasks.loop(seconds=600)(automeme_routine)
            automeme_loops[channel_id] = loop
            loop.start(ctx)

    @commands.command()
    async def automeme_cancel(self, ctx):
        '''Cancel the Automeme task in the current channel'''
        channel_id = ctx.channel.id
        if channel_id not in automeme_loops:
            await ctx.send('Automeme not running here')
        else:
            automeme_loops[channel_id].cancel()
            del automeme_loops[channel_id]
            await ctx.send('Automeme canceled here')


def setup(client):
    client.add_cog(Meme(client))
