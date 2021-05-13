from discord import Embed

from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['meme'])
    async def memes(self, ctx: Context, param: str = None):
        """Meme command for the bot"""
        sub = '/' if param is None else '/' + str(param)
        url = "https://meme-api.herokuapp.com/gimme" + sub
        async with self.client.HTTP_SESSION.get(url) as response:
            response = await response.json()
        embed = Embed(
            title=response['title'],
            url=response['postLink'],
            color=COLOR.JOY)
        embed.set_image(url=response['url'])
        txt = f"r/{response['subreddit']} | Requested by {ctx.author.name}"
        embed.set_footer(text=txt)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))
