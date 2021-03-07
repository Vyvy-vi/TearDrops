from typing import List

from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR
from .utils.embeds import info_embed

def format_help_text(txt: List) -> str:
    txt = f"{',** '.join(sorted(txt))}**".split(' ')
    txt = [txt[i: i+2] for i in range(0, len(txt), 2)]
    txt = [' '.join(i) for i in txt]
    txt = 'The following command categories exist for bot ;-;\n' + '\n'.join(txt)+ '\nFor more info, use\n`qq help <Category-name>`\nor `qq help <Command-name>`'
    return txt

class Help(commands.Cog):
    """Help cog for custom help embed"""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['botwhat'])
    async def botinfo(self, ctx: Context):
        '''Gives info about the bot'''
        embed = info_embed()
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx: Context, index: str = None):
        '''Displays the help command'''
        colo = COLOR.DEFAULT
        if index is None:
            title='**Help command**'
            text = [f'**{cog[0]}' for cog in self.client.cogs.items()]
            print(text)
            desc = format_help_text(text)
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
