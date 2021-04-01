from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands import Context

class Dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def urban(self, ctx: Context, *args):
        '''searches urban dictionary for words'''
        baseurl = "https://www.urbandictionary.com/define.php?term="
        output = ''.join(args)
        await ctx.send(baseurl + output)

    @commands.command(pass_context=True)
    async def define(self, ctx: Context, *args):
        '''searches merriam-webster for meanings of words'''
        baseurl = "https://www.merriam-webster.com/dictionary/"
        output = '%20'.join(args)
        await ctx.send(baseurl + output)

def setup(client):
    client.add_cog(Dictionary(client))
