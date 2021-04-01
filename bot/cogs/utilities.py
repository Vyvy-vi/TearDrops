import wikipedia
import aiohttp

from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands import Context
from loguru import logger

from .utils.colo import COLOR


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def wiki(self, ctx: Context, *, args):
        '''Displays wikipedia info about given arguments'''
        searchResults = wikipedia.search(args)
        if not searchResults:
            embed = Embed(
                title=f'**{args}**',
                description='It appears that there is no instance of this in Wikipedia index...',
                colour=COLOR.ERROR)
            embed.set_footer(text='Powered by Wikipedia...')
        else:
            try:
                page = wikipedia.page(searchResults[0], auto_suggest=False)
                pg = 0
            except wikipedia.DisambiguationError as err:
                page = wikipedia.page(err.options[0], auto_suggest=False)
                pg = err.options
            wikiTitle = str(page.title.encode('utf-8'))
            wikiSummary = page.summary
            embed = Embed(title=f'**{wikiTitle[1:]}**', description=str(
                wikiSummary[0:900]) + '...', color=COLOR.WIKI, url=page.url)
            embed.set_footer(text='Powered by Wikipedia...')
            if pg != 0:
                s = pg[1:10] + ['...']
                s = ','.join(s)
                embed.add_field(name='Did you mean?:', value=s)
            embed.set_image(url=page.images[0])

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def weather(self, ctx: Context, *, loc):
        '''displays weather data'''
        p = {"http": "http://111.233.225.166:1234"}
        key = "353ddfe27aa4b3537c47c975c70b58d9"  # dummy key(for now)
        async with aiohttp.ClientSession() as session:
            url = f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={loc}, verify= False"
            async with session.get(url) as res:
                q = await res.json()

        if q["cod"] not in [404, 401]:
            weather_data = {}
            temp = q['main']['temp']

            weather_data['Temperature'] = f'{str(round(temp-273.16, 2))} °C'
            weather_data['Pressure'] = f"{q['main']['pressure']} hpa"
            weather_data['Humidity'] = f"{q['main']['humidity']} %"
            weather_data['Wind Speed'] = q['wind']['speed']

            w_obj = q['weather'][0]
            weather_data['\nDescription'] = w_obj['description']
            w_id = str(w_obj['id'])
            col = {'8': 0xbababa,
                   '7': 0xc2eaea,
                   '6': 0xdde5f4,
                   '5': 0x68707c,
                   '3': 0xb1c4d8,
                   '2': 0x4d5665}
            col = 0xd8d1b4 if w_id == '800' else col.get(w_id[0], 0x000000)
            weather_data = [
                f'**{field}**: {weather_data[field]}' for field in weather_data]
            embed = Embed(
                title='Weather',
                description=f'displaying weather of {loc}...',
                color=col)
            embed.add_field(name='\u200b', value='\n'.join(weather_data))
            embed.set_footer(text=f'Requested by {ctx.message.author.name}')
        else:
            embed = Embed(title='Weather',
                          description='API Connection Refused',
                          color=Color.red())
            embed.set_footer(text=f'Requested by {ctx.message.author.name}')
            logger.error('Error with weather command')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utils(client))
