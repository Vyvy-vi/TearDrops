from random import randint
from typing import Optional

from discord import Embed, app_commands, Interaction
from discord.ext import commands
from .utils.colo import COLOR


class Comics(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="xkcd",
        description="Fetch comic strips from xkcd's blog",
    )
    async def xkcd(self, interaction: Interaction, arg: Optional[str] = None):
        """Comic strips from xkcd's blog"""
        base_url = "https://xkcd.com/"
        await interaction.response.defer()
        if not arg:
            async with self.client.session.get(base_url + "info.0.json") as json:
                json = await json.json()
                base_url += f'{randint(1, int(json["num"]))}/'
        elif arg != "latest":
            base_url += f"{arg}/"
        url = base_url + "info.0.json"
        async with self.client.session.get(url) as json:
            json = await json.json()
        embed = Embed(
            title=json["title"], url=base_url, description=json["alt"], color=COLOR.XKCD
        )
        embed.set_image(url=json["img"])
        txt = f"xkcd comic #{json['num']} | Requested by {interaction.user.name}"
        embed.set_footer(text=txt)
        await interaction.followup.send(embed=embed)


async def setup(client):
    await client.add_cog(Comics(client))
