import discord
from discord.ext import commands

class Users(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def user(self, ctx, *, user: discord.Member = None):
        '''gives user info'''
        if user is None:
            user = ctx.message.author
        embed = discord.Embed(
            title="{}'s info".format(
                user.name),
            description="Here's what I could find.",
            color=user.color)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Highest role", value=user.top_role, inline=True)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name='Account Created on', value=user.created_at)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        async with ctx.channel.typing():
            embed = discord.Embed(color=user.color)
            embed.set_footer(text=f"Displaying avatar of {user.display_name}")
            embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Users(client))
