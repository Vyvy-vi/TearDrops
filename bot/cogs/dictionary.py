from discord import app_commands, Interaction
from discord.ext import commands


class Dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="urban", description="Searche urban disctionary")
    async def urban(self, interaction: Interaction, args: str):
        """searches urban dictionary for words"""
        baseurl = "https://www.urbandictionary.com/define.php?term="
        output = args
        await interaction.response.send_message(baseurl + output)

    @app_commands.command(
        name="define", description="Search meaning of a word from merriam-webster"
    )
    async def define(self, interaction: Interaction, args: str):
        """searches merriam-webster for meanings of words"""
        baseurl = "https://www.merriam-webster.com/dictionary/"
        output = args
        await interaction.response.send_message(baseurl + output)


async def setup(client):
    await client.add_cog(Dictionary(client))
