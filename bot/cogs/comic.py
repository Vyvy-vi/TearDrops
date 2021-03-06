from random import randint
from typing import Optional

from discord import Embed
from discord.ext.commands import Context
from discord.ext import commands
from .utils.colo import COLOR


class Comics(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def xkcd(self, ctx: Context, arg: Optional[str] = 'random'):
        '''Provides a comic strip from xkcd blog'''
        base_url = 'https://xkcd.com/'
        if arg == 'random':
            base_url += f'{randint(1, 2390)}/'
        elif arg != 'latest':
            base_url += f'{arg}/'
        url = base_url + 'info.0.json'
        async with self.client.HTTP_SESSION.get(url) as json:
            json = await json.json()
        embed = Embed(title=json['title'],
                      url=base_url,
                      description=json['alt'],
                      color=COLOR.XKCD)
        embed.set_image(url=json['img'])
        txt = f"xkcd comic #{json['num']} | Requested by {ctx.author.name}"
        embed.set_footer(text=txt)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Comics(client))
