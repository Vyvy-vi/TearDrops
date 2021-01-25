import random
import discord
import wikipedia
import requests
import wolframalpha

from discord.ext import commands
from translate import Translator
from .utils import COLOR


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def echo(self, ctx, *args):
        '''echos the words'''
        output = ''
        for word in args:
            output += word
            output += ' '
        await ctx.send(output)

    @commands.command(pass_context=True)
    async def say(self, ctx, *args):
        """Gives the user's statement a nice richtext quote format"""
        output = ''
        for word in args:
            output += word
            output += ' '
        user = ctx.message.author
        embed = discord.Embed(
            title=f'{output}',
            description=f'~{user}',
            colour=discord.Color.greyple())
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def urban(self, ctx, *args):
        '''searches urban dictionary for words'''
        baseurl = "https://www.urbandictionary.com/define.php?term="
        output = ''.join(args)
        await ctx.send(baseurl + output)

    @commands.command(pass_context=True)
    async def define(self, ctx, *args):
        '''searches merriam-webster for meanings of words'''
        baseurl = "https://www.merriam-webster.com/dictionary/"
        output = '%20'.join(args)
        await ctx.send(baseurl + output)

    @commands.command(pass_context=True)
    async def wiki(self, ctx, *, args):
        '''Displays wikipedia info about given arguments'''
        searchResults = wikipedia.search(args)
        if not searchResults:
            embed = discord.Embed(
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
            embed = discord.Embed(title=f'**{wikiTitle[1:]}**', description=str(
                wikiSummary[0:900]) + '...', color=COLOR.WIKI, url=page.url)
            embed.set_footer(text='Powered by Wikipedia...')
            if pg != 0:
                s = pg[1:10] + ['...']
                s = ','.join(s)
                embed.add_field(name='Did you mean?:', value=s)
            embed.set_image(url=page.images[0])

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def wolfram(self, ctx, *args):
        '''displays info from wolfram'''
        ques = ''.join(args)
        wolfram = wolframalpha.Client("QYKRJ8-YT2JP8U85T")
        res = wolfram.query(ques)
        if res['@success'] == 'false':
            await ctx.send('Question cannot be resolved')
        else:
            await ctx.send(next(res.results).text)

    @commands.command(pass_context=True)
    async def weather(self, ctx, *, loc):
        '''displays weather data'''
        p = {"http": "http://111.233.225.166:1234"}
        k = "353ddfe27aa4b3537c47c975c70b58d9"  # dummy key(for now)
        api_r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?appid={k}&q={loc}, verify= False, proxies=p")
        q = api_r.json()
        if q["cod"] != 404:
            weather_data = {}
            temp = q['main']['temp']
            weather_data['Temperature'] = f'{str(round(temp-273.16, 2))} °C'

            p = q['main']['pressure']
            weather_data['Pressure'] = f'{str(p)} hpa'

            hum = q['main']['humidity']
            weather_data['Humidity'] = f'str{hum} %'

            wind = q['wind']['speed']
            weather_data['Wind Speed'] = wind

            w_obj = q['weather'][0]
            desc = w_obj['description']
            weather_data['\nDescription'] = desc
            w_id = str(w_obj['id'])
            if '8' in w_id[0]:
                col = 0xd8d1b4 if w_id == '800' else 0xbababa
            elif '7' in w_id[0]:
                col = 0xc2eaea
            elif '6' in w_id[0]:
                col = 0xdde5f4
            elif '5' in w_id[0]:
                col = 0x68707c
            elif '3' in w_id[0]:
                col = 0xb1c4d8
            elif '2' in w_id[0]:
                col = 0x4d5665
            else:
                col = 0x000000
            weather_data = [
                f'**{field}**: {weather_data[field]}' for field in weather_data]
            embed = discord.Embed(
                title='Weather',
                description=f'displaying weather of {loc}...',
                color=col)
            embed.add_field(name='\u200b', value='\n'.join(weather_data))
            embed.set_footer(text=f'Requested by {ctx.message.author.name}')
        else:
            embed = discord.Embed(title='Weather',
                                  description='API Connection Refused',
                                  color=discord.Color.red())
            embed.set_footer(text='Requested by {ctx.message.author.name}')

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def translate(self, ctx, lang, *, args):
        '''Converts text to different language'''

        translator = Translator(to_lang=f"{lang}", from_lang='autodetect')
        translated = translator.translate(f"{args}")
        embed = discord.Embed(
            title="---> translating",
            description=f'{translated}\n~{ctx.message.author.mention}',
            colour=COLOR.RANDOM())
        embed.set_footer(text=f'Translated to {lang}...')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['multitrans', 'mt'])
    async def multi_translate(self, ctx, *, args):
        '''Converts text multiple times'''
        LANGS = [
            'Zulu',
            'Welsh',
            'Uzbek',
            'Turkish',
            'Thai',
            'Swedish',
            'Swahili',
            'Somali',
            'Slovak',
            'Russian',
            'Romanian',
            'Persian',
            'Polish',
            'Panjabi',
            'Nepali',
            'Mongolian',
            'Macedonian',
            'Latin',
            'Korean',
            'Japanese',
            'Italian',
            'Irish',
            'Hebrew',
            'German',
            'French',
            'Finnish',
            'Estonian',
            'Dutch',
            'Danish',
            'Czech',
            'Chinese',
            'Catalan',
            'Armenian',
            'Arabic',
            'Afrikaans']
        REPS = random.randint(8, 18)
        conversion_hist = f"---> Translated {REPS} times... "
        translated = f"{args}"
        RAND_LANGS = list({random.choice(LANGS) for __ in range(REPS)})
        for _ in RAND_LANGS:
            conversion_lang = _
            conversion_hist += f'> {conversion_lang} '
            translator = Translator(to_lang=f'{conversion_lang}',
                                    from_lang='autodetect')
            translated = translator.translate(translated)
        embed = discord.Embed(title="Multi-translate",
                              description=conversion_hist + '> English',
                              color=COLOR.RANDOM())
        translated = Translator(to_lang='en',
                                from_lang='autodetect').translate(translated)
        embed.add_field(name='Original text', value=f"`{args}`")
        embed.add_field(
            name='Translated text',
            value=f"`{translated}`",
            inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utils(client))
