from random import choice

import motor.motor_asyncio as motor
from discord import Member, Embed, app_commands, Interaction
from discord.ext import commands

from .utils.colo import COLOR


class Coffee(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.data = motor.AsyncIOMotorClient(client.MONGO).DATA.inputs

    @app_commands.command(
        name="wannagrabacoffee", description="Ask someone out for coffee"
    )
    async def wannagrabacoffee(self, interaction: Interaction, member: Member):
        """Wanna ask someone out on coffee"""
        res = await self.data.find_one({"type": "coffee"})
        embed = Embed(
            title=f"{member}, Someone wants to grab a coffee with you...*wink *wink",
            color=COLOR.COFFEE,
        )
        embed.add_field(name="This happened....", value=choice(res["events"]))
        embed.set_footer(text="not actually :P")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="coffee", description="Brew yourself a nice cup of coffee"
    )
    async def coffee(self, interaction: Interaction):
        """A lovely coffee command (sip, sip)"""
        res = await self.data.find_one({"type": "coffee"})
        embed = Embed(
            title="Coffee", description=choice(res["text"]), color=COLOR.COFFEE
        )
        embed.set_footer(
            text=f"Caffeiene Level-{choice(res['strength'])}. {choice(res['msg'])}"
        )
        embed.set_image(url=choice(res["img"]))
        await interaction.response.send_message(embed=embed)


async def setup(client) -> None:
    await client.add_cog(Coffee(client))
