import discord
from discord.ext import commands
import ssl
import aiohttp


class MemeCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['meme'])
    async def memes(self, ctx):
        async with aiohttp.ClientSession() as session:
            url = "https://meme-api.herokuapp.com/gimme"
            async with session.get(url) as response:
                response = await response.json()
            embed = discord.Embed(title=response['title'],
                                  url=response['postLinki'],
                                  color=discord.Color.dark_orange())
            embed.set_image(url=response['url'])
            txt = f"r/{response['subreddit']} | Requested by {ctx.author.name} | Enjoy your dank memes"
            embed.set_footer(text=txt)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(MemeCog(client))
