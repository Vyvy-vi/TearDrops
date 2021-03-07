from discord.ext import commands
from discord import Embed

from discord.ext.commands import Context

from .utils.colo import COLOR


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['botwhat'])
    async def botinfo(self, ctx: Context):
        '''Gives info about the bot'''
        embed = Embed(
            title='**Tear Drops:tm:**',
            description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under MIT license, I request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under MIT License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes',
            colour=COLOR.DEFAULT,
            url='https://github.com/Py-Contributors/awesomeScripts/Tear-Drops_DiscordBot/')
        embed.set_footer(text='I Hope that you enjoyed the bot....😭')
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx: Context, index: str = None):
        '''Displays the help command'''
        text = []
        if index is None:
            embed = Embed(
                title='**Help command**',
                description='The following command categories exist for bot ;-;',
                color=COLOR.DEFAULT)
            for cog in self.client.cogs.items():
                text.append(f'**{cog[0]}')
            text = f"{',** '.join(sorted(text))}**".split(' ')
            text = [text[i:i + 2] for i in range(0, len(text), 2)]
            text = [' '.join(i) for i in text]
            embed.add_field(
                name='\u200b',
                value='\n'.join(text) +
                '\nFor more info, use `qq help <Category-name>` or `qq help <Command-name>`')
            embed.set_footer(
                text='Cry, cry, let the tears flow through you...')
        else:
            if index in self.client.cogs:
                cog = self.client.get_cog(index)
                text = [f'**{c.name}** : {c.short_doc}' for c in cog.get_commands()]
                embed = Embed(
                            title=f'**Help category: {index}**',
                            description='\n'.join(text),
                            color=COLOR.DEFAULT)
            else:
                is_command = lambda cmd: cmd.name == index
                cmd_match = list(filter(lambda cmd: cmd.name == index,
                                 self.client.commands))
                if cmd_match:
                    embed = Embed(
                        title=f'**Help command: {cmd_match[0]}**',
                        description=f'Description : {cmd_match[0].short_doc} \n {cmd_match[0].brief}',
                        color=COLOR.DEFAULT)
                else:
                    embed = Embed(
                            title=f'{index} was not found...',
                            color=COLOR.ERROR)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
