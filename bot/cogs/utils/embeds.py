from discord import Embed
from .colo import COLOR


def info_embed():
    embed = Embed(
        title='**Tear Drops:tm:**',
        description='A dynamic bot for _crying_, entertainment, economy and _other_ purposes...\n\
I am here to reek sorrow and depression. Come let\'s cry together 😢\
The prefix for the bot is _"qq"_, cuz you know _"less qq, more pew pew..."_ \
The currency credits for the bot are _tears_(hahah obviously). Have fun being sad...\
\nNOTE- Even though this is OpenSource and under a BSD license, we request you to not start a commercial bot with the same name "Tear Drops:tm:"\
This bot is under BSD License(provided as is, do whatever you want) \
This has been uploaded to GitHub for educational and referencial purposes',
        colour=COLOR.DEFAULT,
        url='https://github.com/Vyvy-vi/TearDrops')
    embed.set_footer(text='We Hope that you enjoyed the bot....😭')
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
    return embed


def weather_embed_color(w_id):
    col = {'8': 0xbababa,
           '7': 0xc2eaea,
           '6': 0xdde5f4,
           '5': 0x68707c,
           '3': 0xb1c4d8,
           '2': 0x4d5665}
    col = 0xd8d1b4 if w_id == '800' else col.get(w_id[0], 0x000000)
    return col


def weather_embed(loc, q, author):
    weather_data = {}
    temp = q['main']['temp']

    weather_data['Temperature'] = f'{str(round(temp-273.16, 2))} °C'
    weather_data['Pressure'] = f"{q['main']['pressure']} hpa"
    weather_data['Humidity'] = f"{q['main']['humidity']} %"
    weather_data['Wind Speed'] = q['wind']['speed']

    w_obj = q['weather'][0]
    weather_data['\nDescription'] = w_obj['description']

    col = weather_embed_color(str(w_obj['id']))
    weather_data = [f'**{field}**: {data}' for field, data in weather_data.items()]
    embed = Embed(title='Weather',
                  description=f'displaying weather of {loc}',
                  color=col)
    embed.add_field(name='\u200b', value='\n'.join(weather_data))
    embed.set_footer(text=f'Requested by {author}')
    return embed
