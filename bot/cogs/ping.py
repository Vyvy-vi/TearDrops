from discord import Embed, Interaction, app_commands
from discord.ext import commands

from .utils.colo import COLOR
from .utils.phrases import TEXT


def ping_embed(title, desc, colo):
    embed = Embed(title=title, description=desc, color=colo)
    embed.set_footer(text="😭")
    return embed


class Ping(commands.Cog):
    """This is the Ping Cog, mainly for testing the bot-status"""

    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ping", description="Ping the bot")
    async def ping(self, interaction: Interaction):
        """Ping command (for testing)"""
        bot_lsm = round(self.client.latency * 1000)
        embed = ping_embed(
            "**pong...!**",
            f"_{TEXT.ping}_ \n**~{bot_lsm} ms taken**......",
            COLOR.SUCCESS,
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="pong", description="Pong the bot??")
    async def pong(self, interaction: Interaction):
        """Pong command (also for testing)"""
        bot_lsm = round(self.client.latency * 1000)
        embed = ping_embed(
            "**PING...!**",
            f"_{TEXT.pong}_ \n**~{bot_lsm} ms taken**......",
            COLOR.ERROR,
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="echo", description="echo your words into the abyss...")
    async def echo(self, interaction: Interaction, args: str):
        """echos the words into the abyss"""
        output = ""
        for word in args.split(" "):
            output += word
            output += " "
        await interaction.response.send_message(output)

    @app_commands.command(
        name="say", description="get the bot to make a fancy message for your text"
    )
    async def say(self, interaction: Interaction, args: str):
        """Gives the user's statement a nice richtext quote format"""
        output = ""
        for word in args.split(" "):
            output += word
            output += " "
        user = interaction.user
        embed = Embed(title=f"{output}", description=f"~{user}", colour=COLOR.RANDOM())
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Ping(client))
