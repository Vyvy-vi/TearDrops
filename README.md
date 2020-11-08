# Tear Drops
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-13-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![built-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/Vyvy-vi/)
<p>
<a href="https://raw.githubusercontent.com/Vyvy-vi/TearDrops/main/LICENSE"><img src="https://img.shields.io/github/license/Vyvy-vi/TearDrops?style=flat-square" alt="MIT license"></a>
<a href="https://github.com/Rapptz/discord.py/releases/tag/v1.5.0"><img src="https://img.shields.io/badge/discord.py-v1.5.0-7289da.svg?style=flat-square" alt="discord.py version"></a>
</p>

[![TearDrops Support](https://discordapp.com/api/guilds/765880027467350047/widget.png?style=banner2)](https://discord.io/TearDropsSupport)

![tears gif](cries.gif)
![cri](https://images-ext-1.discordapp.net/external/s6Id0htXD7zAkT-yxz52y_YNj97WF9yzELQmtIk-iBs/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/627772985872220161/bdfd588427f4335fece00c0191ea1406.webp?width=292&height=294)
![sadblob](https://media.discordapp.net/attachments/771696574697832469/773264495006318623/sadblob.png)

A discord bot wrapped around the theme of tears and crying.
In concept, the idea is absurd but that's more of a reason to make this. :)
The bot uses tears as an economy and you can "cry" to get daily credit tears.

NOTE- It is recommended that you add your own discord token while running the bot.

- [Invite the bot to your server](https://discord.com/api/oauth2/authorize?client_id=627772985872220161&permissions=379968&scope=bot)
[*NOTE- The bot is still in v0.1 and is being constantly updated and bug fixed. Inviting this, might have unintentional complications. If you really want the bot, open an issue so that we can provide a Beta Version to you that is stable and updated slowly*]
- To test the bot join this [Support Server](https://discord.gg/jTzGuYx)
  [*NOTE- Bot is not active 24x7 as it is hosted on heroku. To get a sample, join* [TearDropsSupport](https://discord.gg/jTzGuYx) *and ping* **@Tissue**]

## Hosting the bot locally:

- NOTE: To replicate this bot, you will need a bot **token**. Go get yours at https://discord.com/developers/ (If you need help with this step, feel free to ask for help in our [Support Server](https://discord.gg/jTzGuYx)).
- Clone this repo using `git clone`
- cd into the bot folder.
- Add the token in a `.env` file in the project root as follows:
```text
DISCORD_BOT_TOKEN=<your token>
```
- Install [docker and docker-compose](https://docs.docker.com/desktop/) and then run:
```
docker-compose up
```
- Enjoy! (don't forget to add your own bot into your discord server by generating an invite link from the discord developers application page in [OAuth2 section](https://discord.com/developers/applications/) and choose application and check Oauth2 section)
- You may do bug-reporting or ask for help in on the SupportServer... or just open an issue on this repo.

## Requirements:
- python 3
- discord(rewrite branch)
- asyncio(inbuilt with python3.4)
- wikipedia
- requests
- aiohttp
- pymongo
- dnspython

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://allcontributors.org"><img src="https://avatars1.githubusercontent.com/u/46410174?v=4" width="100px;" alt=""/><br /><sub><b>All Contributors</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=all-contributors" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Vyvy-vi"><img src="https://avatars0.githubusercontent.com/u/62864373?v=4" width="100px;" alt=""/><br /><sub><b>Vyom Jain</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=Vyvy-vi" title="Code">💻</a> <a href="#projectManagement-Vyvy-vi" title="Project Management">📆</a> <a href="#design-Vyvy-vi" title="Design">🎨</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=Vyvy-vi" title="Documentation">📖</a> <a href="#maintenance-Vyvy-vi" title="Maintenance">🚧</a> <a href="https://github.com/Vyvy-vi/TearDrops/pulls?q=is%3Apr+reviewed-by%3AVyvy-vi" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://anubhav.codes"><img src="https://avatars0.githubusercontent.com/u/1628340?v=4" width="100px;" alt=""/><br /><sub><b>Anubhav</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=anubhavcodes" title="Code">💻</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=anubhavcodes" title="Documentation">📖</a> <a href="#ideas-anubhavcodes" title="Ideas, Planning, & Feedback">🤔</a> <a href="#infra-anubhavcodes" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/gamerrio"><img src="https://avatars0.githubusercontent.com/u/21240909?v=4" width="100px;" alt=""/><br /><sub><b>Gamerrio</b></sub></a><br /><a href="#ideas-gamerrio" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=gamerrio" title="Code">💻</a> <a href="#design-gamerrio" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/RascalTwo"><img src="https://avatars0.githubusercontent.com/u/9403665?v=4" width="100px;" alt=""/><br /><sub><b>Rascal_Two</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/issues?q=author%3ARascalTwo" title="Bug reports">🐛</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=RascalTwo" title="Code">💻</a> <a href="#ideas-RascalTwo" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/sayand0122"><img src="https://avatars1.githubusercontent.com/u/53222600?v=4" width="100px;" alt=""/><br /><sub><b>Sayan Dutta</b></sub></a><br /><a href="#ideas-sayand0122" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=sayand0122" title="Code">💻</a> <a href="#design-sayand0122" title="Design">🎨</a></td>
    <td align="center"><a href="http://www.nhcarrigan.com"><img src="https://avatars1.githubusercontent.com/u/63889819?v=4" width="100px;" alt=""/><br /><sub><b>Nicholas Carrigan (he/him)</b></sub></a><br /><a href="#ideas-nhcarrigan" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=nhcarrigan" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://mikeysan.hashnode.dev"><img src="https://avatars1.githubusercontent.com/u/13338176?v=4" width="100px;" alt=""/><br /><sub><b>Michael Mba</b></sub></a><br /><a href="#ideas-mikeysan" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/AllanRegush"><img src="https://avatars0.githubusercontent.com/u/17693494?v=4" width="100px;" alt=""/><br /><sub><b>Allan Regush</b></sub></a><br /><a href="#ideas-AllanRegush" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://mattcowley.co.uk/"><img src="https://avatars2.githubusercontent.com/u/12371363?v=4" width="100px;" alt=""/><br /><sub><b>Matt (IPv4) Cowley</b></sub></a><br /><a href="#ideas-MattIPv4" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/AbstractUmbra"><img src="https://avatars0.githubusercontent.com/u/16031716?v=4" width="100px;" alt=""/><br /><sub><b>Alex Nørgaard</b></sub></a><br /><a href="#ideas-AbstractUmbra" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/LazybuddyNK"><img src="https://avatars3.githubusercontent.com/u/59273928?v=4" width="100px;" alt=""/><br /><sub><b>Nitesh Kumar</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=LazybuddyNK" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/IcemanEtika"><img src="https://avatars0.githubusercontent.com/u/44535539?v=4" width="100px;" alt=""/><br /><sub><b>TJ LeBlanc</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=IcemanEtika" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
