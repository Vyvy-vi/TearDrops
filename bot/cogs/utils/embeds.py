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
    embed.set_image(url='https://cdn.discordapp.com/attachments/582605227081990233/627388598181953548/unknown.png')
    return embed
