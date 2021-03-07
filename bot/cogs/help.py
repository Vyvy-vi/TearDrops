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
        colo = COLOR.DEFAULT
        if index is None:
            title='**Help command**'
            text = [f'**{cog[0]}' for cog in self.client.cogs.items()]
            text = f"{',** '.join(sorted(text))}**".split(' ')
            text = [text[i:i + 2] for i in range(0, len(text), 2)]
            text = [' '.join(i) for i in text]
            desc = 'The following command categories exist for bot ;-;\n' + '\n'.join(text) + '\nFor more info, use\n`qq help <Category-name>`\nor `qq help <Command-name>`'
        else:
            if index in self.client.cogs:
                cog_cmds = self.client.get_cog(index).get_commands()
                title = f'**Help category: `{index}`**'
                desc = '\n'.join([f'**{c.name}** : {c.short_doc}' for c in cog_cmds])
            else:
                cmd_match = list(filter(lambda cmd: cmd.name == index,
                                 self.client.commands))
                if len(cmd_match) > 0:
                    title=f'**Help command: `{cmd_match[0]}`**'
                    desc=f'Description : {cmd_match[0].short_doc} \n {cmd_match[0].brief}'
                else:
                    title = f'`{index}` was not found...'
                    desc = None
                    colo = COLOR.ERROR
        embed = Embed(title=title,
                      description=desc,
                      color=colo)
        embed.set_footer(text='Cry, cry, let the tears flow through you...')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
