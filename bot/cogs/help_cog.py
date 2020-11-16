import discord
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['botwhat'])
    async def botinfo(self, ctx):
        '''Gives info about the bot'''
        embed = discord.Embed(title='**Tear Drops:tm:**', description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license, I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes', colour=discord.Color.purple(), url='https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
        embed.set_footer(text='I Hope that you enjoyed the bot....😭')
        embed.set_image(url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx, command_name=None, *args):
        '''Displays the help command'''
        if command_name is None:
            embed = discord.Embed(title='**Help command**',description='All commands of bot ;-; with description',color=discord.Color.dark_orange())
            for command in self.client.commands:
                embed.add_field(
    name=f'{command}',
    value=f'\u200b',
     inline=True)
            await ctx.send(embed=embed)
        else:
            for command in self.client.commands:
                if command_name == command.name:
                    embed = discord.Embed(
    title=f'**Help command: {command}**',
    description=f'Description : {command.short_doc} \n {command.brief}',
     color=discord.Color.dark_orange())
                    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HelpCog(client))
