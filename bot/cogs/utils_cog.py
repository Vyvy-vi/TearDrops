import discord
import wikipedia
import wolframalpha
from discord.ext import commands


class UtilsCog(commands.Cog):
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
        output = args.join('')
        await ctx.send(baseurl + output)

    @commands.command(pass_context=True)
    async def define(self, ctx, *args):
        '''searches merriam-webster for meanings of words'''
        baseurl = "https://www.merriam-webster.com/dictionary/"
        output = args.join('%20')
        await ctx.send(baseurl + output)

    @commands.command(pass_context=True)
    async def user(self, ctx, user: discord.Member):
        '''gives user info'''
        embed = discord.Embed(
            title="{}'s info".format(
                user.name),
            description="Here's what I could find.",
            color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name='Account Created on', value=user.created_at)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def wiki(self, ctx, *args):
        '''Displays wikipedia info about given arguments'''
        qu = ' '.join(list(args))
        searchResults = wikipedia.search(qu)
        if not searchResults:
            embed = discord.Embed(
                title=f'**{qu}**',
                description='It appears that there is no instance of this in Wikipedia index...',
                colour=discord.Color.dark_red())
            embed.set_footer(text='Powered by Wikipedia...')
            await ctx.send(embed=embed)
        else:
            try:
                page = wikipedia.page(searchResults[0])
                pg = 0
            except wikipedia.DisambiguationError as err:
                page = wikipedia.page(err.options[0])
                pg = err.options
            wikiTitle = str(page.title.encode('utf-8'))
            wikiSummary = page.summary
            embed = discord.Embed(title=f'**{wikiTitle[1:]}**', description=str(
                wikiSummary[1:900]) + '...', color=discord.Color.dark_orange(), url=page.url)
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
        ques = ' '.join(list(args))
        wolfram = wolframalpha.Client("QYKRJ8-YT2JP8U85T")
        res = wolfram.query(ques)
        await ctx.send(next(res.results).text)


def setup(client):
    client.add_cog(UtilsCog(client))
