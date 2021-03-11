import wikipedia
import requests

from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands import Context

from .utils.colo import COLOR


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def echo(self, ctx: Context, *args):
        '''echos the words'''
        output = ''
        for word in args:
            output += word
            output += ' '
        await ctx.send(output)

    @commands.command(pass_context=True)
    async def say(self, ctx: Context, *args):
        """Gives the user's statement a nice richtext quote format"""
        output = ''
        for word in args:
            output += word
            output += ' '
        user = ctx.message.author
        embed = Embed(
            title=f'{output}',
            description=f'~{user}',
            colour=Color.greyple())
        await ctx.send(embed=embed)

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
        api_r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={loc}, verify= False, proxies=p")
        q = api_r.json()
        if q["cod"] != 404:
            weather_data = {}
            temp = q['main']['temp']
            weather_data['Temperature'] = f'{str(round(temp-273.16, 2))} °C'

            p = q['main']['pressure']
            weather_data['Pressure'] = f'{p} hpa'

            hum = q['main']['humidity']
            weather_data['Humidity'] = f'{hum} %'

            wind = q['wind']['speed']
            weather_data['Wind Speed'] = wind

            w_obj = q['weather'][0]
            desc = w_obj['description']
            weather_data['\nDescription'] = desc
            w_id = str(w_obj['id'])
            col = { '8': 0xbababa,
                    '7': 0xc2eaea,
                    '6': 0xdde5f4,
                    '5': 0x68707c,
                    '3': 0xb1c4d8,
                    '2': 0x4d5665 }
            if w_id == '800':
                col = 0xd8d1b4
            else:
                col = col.get(w_id[0], 0x000000)
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
            embed.set_footer(text='Requested by {ctx.message.author.name}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Utils(client))