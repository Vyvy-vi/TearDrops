from typing import Optional

from discord import Member, Embed, Interaction, app_commands
from discord.ext import commands


class Users(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(
        name="user", description="Get information about a server member"
    )
    async def user(self, interaction: Interaction, user: Optional[Member] = None):
        """Gives info about a Server member"""
        if not user:
            user = interaction.user
            # async with ctx.channel.typing():
        embed = Embed(
            title=f"{user.name}'s info",
            description="Here's what I could find.",
            color=user.color,
        )
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Highest role", value=user.top_role, inline=True)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name="Account Created on", value=user.created_at)
        embed.set_thumbnail(url=user.avatar_url)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="")
    async def avatar(self, interaction: Interaction, *, user: Member = None):
        """Fetches a user's avatar"""
        if not user:
            user = interaction.user
        # async with ctx.channel.typing():
        embed = Embed(color=user.color)
        embed.set_footer(text=f"Displaying avatar of {user.display_name}")
        embed.set_image(url=user.avatar_url)
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Users(client))
