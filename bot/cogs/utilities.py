import wikipedia

from discord import Embed, Color, app_commands, Interaction
from discord.ext import commands
from loguru import logger

from .utils.colo import COLOR
from .utils.embeds import weather_embed


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="wiki", description="Search something on wikipedia")
    async def wiki(self, interaction: Interaction, *, args):
        """Display result from wikipedia"""
        searchResults = wikipedia.search(args)
        if not searchResults:
            embed = Embed(
                title=f"**{args}**",
                description="It appears that there is no instance of this in Wikipedia index...",
                colour=COLOR.ERROR,
            )
            embed.set_footer(text="Powered by Wikipedia...")
        else:
            try:
                page = wikipedia.page(searchResults[0], auto_suggest=False)
                pg = 0
            except wikipedia.DisambiguationError as err:
                page = wikipedia.page(err.options[0], auto_suggest=False)
                pg = err.options
            wikiTitle = str(page.title.encode("utf-8"))
            wikiSummary = page.summary
            embed = Embed(
                title=f"**{wikiTitle[1:]}**",
                description=str(wikiSummary[0:900]) + "...",
                color=COLOR.WIKI,
                url=page.url,
            )
            embed.set_footer(text="Powered by Wikipedia...")
            if pg != 0:
                s = pg[1:10] + ["..."]
                s = ",".join(s)
                embed.add_field(name="Did you mean?:", value=s)
            embed.set_image(url=page.images[0])

        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="weather", description="Get weather information about a location"
    )
    async def weather(self, interaction: Interaction, loc: str):
        """Displays weather data"""
        key = "353ddfe27aa4b3537c47c975c70b58d9"  # dummy key(for now)
        url = f"http://api.openweathermap.org/data/2.5/weather?appid={key}&q={loc}, verify= False"
        async with self.client.HTTP_SESSION.get(url) as res:
            q = await res.json()

        if q["cod"] not in [404, 401]:
            embed = weather_embed(loc, q, interaction.user.name)
        else:
            embed = Embed(
                title="Weather", description="API Connection Refused", color=Color.red()
            )
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            logger.error("Error with weather command")
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(Utils(client))
