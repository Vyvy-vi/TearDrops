import random
from typing import Optional
import motor.motor_asyncio as motor

from discord import Embed, Member, app_commands, Interaction
from discord.ext import commands

from .utils.colo import COLOR


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.data = motor.AsyncIOMotorClient(client.MONGO).DATA.inputs

    @app_commands.command(name="8ball", description="Ask questions from an 8ball")
    async def _8ball(self, interaction: Interaction, question: str):
        """Use an 8ball"""
        res = await self.data.find_one({"type": "8ball"})
        embed = Embed(title="8Ball :8ball:", colour=COLOR.DEFAULT)
        embed.add_field(
            name=f"*Question: {question}*",
            value=f"Conjecture: {random.choice(res['text'])}",
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="fortune", description="Gives you your sad, terrible fortune"
    )
    async def fortune(self, interaction: Interaction):
        """Gives you your terrible fortune"""
        res = await self.data.find_one({"type": "fortunes"})
        embed = Embed(title="Fortune", color=COLOR.DEFAULT)
        embed.add_field(name="Your Fortune", value=random.choice(res["text"]))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="quote", description="get your dose of motivation from these quotes"
    )
    async def quote(self, interaction: Interaction):
        """Gives you a dose of motivational quotes"""
        res = await self.data.find_one({"type": "quotes"})
        randq = random.choice(list(res["text"].keys()))
        quote_text = f"`{randq.replace('|', '.')}`\n_~{res['text'][randq]}_"
        embed = Embed(title="Quote", description=quote_text, color=COLOR.RANDOM())
        await interaction.response.send_message(embed=embed)

    @commands.command(name="dadjoke", description="listen to my bad jokes child.")
    async def dadjoke(self, interaction: Interaction):
        """Gives you some dad puns"""
        res = await self.data.find_one({"type": "puns"})
        embed = Embed(title="Dad joke huh 😏", color=COLOR.RANDOM())
        embed.add_field(
            name=random.choice(res["text"]),
            value="_looks at you, expecting you to laugh_",
        )
        await interaction.response.send_message(embed=embed)

    @commands.command(name="nerd", description="here take some information, you NERD.")
    async def nerd(self, interaction: Interaction):
        """Returns some nerdy stuff"""
        res = await self.data.find_one({"type": "nerd"})
        embed = Embed(title="Nerdy Stuff", color=COLOR.JOY)
        embed.add_field(name="Take this you NERD", value=random.choice(res["text"]))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="hackerman",
        description="flex your hackerman persona with some geeky stuff",
    )
    async def hackerman(self, interaction: Interaction):
        """Returns some geeky gibberish"""
        res = await self.data.find_one({"type": "tech"})
        embed = Embed(title="Geek", color=COLOR.JOY)
        embed.add_field(name="Ahh I am a hackerman", value=random.choice(res["text"]))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="compliment",
        description="wanna complement someone? I can help. I promise.",
    )
    async def compliment(
        self, interaction: Interaction, member: Optional[Member] = None
    ):
        """Wanna shoot some compliments?"""
        user = interaction.user if not member else member
        res = await self.data.find_one({"type": "compliments"})
        embed = Embed(title="Compliment", color=COLOR.JOY)
        embed.add_field(
            name="Here's a compliment for you",
            value=f"{user}, {random.choice(res['text'])}",
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="flirt", description="I can help your helpless self flirt"
    )
    async def flirt(self, interaction: Interaction, member: Optional[Member] = None):
        """Flirting with bots is nice"""
        user = interaction.user if not member else member
        res = await self.data.find_one({"type": "flirts"})
        embed = Embed(title="Flirt", color=COLOR.DEFAULT)
        embed.add_field(
            name="Flirt it away", value=f"{user}, {random.choice(res['text'])}"
        )
        await interaction.response.send_message(embed=embed)

    @commands.command(
        name="book",
        description="take book recommendations from me. I am better than you.",
    )
    async def book(self, interaction: Interaction):
        """Returns you some epic book recomendation"""
        res = await self.data.find_one({"type": "books"})
        embed = Embed(title="Book", color=COLOR.JOY)
        embed.add_field(
            name="Here's a book recomendation: ", value=random.choice(res["text"])
        )
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Fun(client))
