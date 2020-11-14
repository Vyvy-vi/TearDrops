import discord
from dicord.ext import commands


class ErrorCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # TODO- Error Handling
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command used...")
        else:
            await ctx.send(error)
def setup(client):
    client.add_cog(ErrorCog)
