from discord import Embed, Interaction
from discord.ext import commands

from .utils.colo import COLOR


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["meme"])
    async def memes(self, interaction: Interaction, param: str = None):
        """Meme command for the bot"""
        sub = "/" if param is None else "/" + str(param)
        url = "https://meme-api.herokuapp.com/gimme" + sub
        async with self.client.session.get(url) as response:
            response = await response.json()
        embed = Embed(
            title=response["title"], url=response["postLink"], color=COLOR.JOY
        )
        embed.set_image(url=response["url"])
        txt = f"r/{response['subreddit']} | Requested by {interaction.user}"
        embed.set_footer(text=txt)
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Meme(client))
