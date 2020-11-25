import discord
from discord import commands

class Users(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def user(self, ctx, user: discord.Member):
        '''gives user info'''
        embed = discord.Embed(
            title="{}'s info".format(
                user.name),
            description="Here's what I could find.",
            color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name='Account Created on', value=user.created_at)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @command.command(pass_context=True)
    async def avatar(self, ctx, user:discor.Member)

def setup(client):
    client.add_cog(Utils(client))
