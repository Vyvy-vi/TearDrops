import random
from typing import Optional
from discord import Embed, Color, Interaction, app_commands

from discord.ext import commands

from .utils.username import generate
from .utils.joeUsername import joe_generate


class Name(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="do-username",
        description="Generate a random Digital-Ocean themed username",
    )
    async def username(self, interaction: Interaction, lim: Optional[int] = 30):
        """Generates a random username from DigitalOcean's name-set"""
        op = generate(lim)
        if lim == 30:
            op = generate(random.randint(20, 50))
        embed = Embed(
            title=op, description="That sounds cool :", color=Color.dark_magenta()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="joe-username", description="generate what joe-nash would name you"
    )
    async def joe_username(self, interaction: Interaction, lim: Optional[int] = 4):
        """Generates what Joe Nash would name you"""
        op = joe_generate(lim)
        if lim == 4:
            op = joe_generate(random.randint(3, 11))
        embed = Embed(
            title=op,
            description="That sounds cool, cool, cool.. Right.",
            color=Color.gold(),
        )
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Name(client))
