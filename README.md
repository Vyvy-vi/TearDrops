![](.github/resources/title.svg)

<!---
```yaml
▄▄▄█████▓  ▓█████  ▄▄▄         ██▀███    ▓█████▄    ██▀███     ▒█████     ██▓███      ██████ 
▓  ██▒ ▓▒  ▓█   ▀  ▒████▄      ▓██ ▒ ██  ▒▒██▀ ██▌  ▓██ ▒ ██  ▒▒██▒  ██▒  ▓██░  ██▒  ▒██    ▒ 
▒ ▓██░ ▒░  ▒███    ▒██  ▀█▄    ▓██ ░▄█   ▒░██   █▌  ▓██ ░▄█   ▒▒██░  ██▒  ▓██░ ██▓▒  ░ ▓██▄   
░ ▓██▓ ░   ▒▓█  ▄  ░██▄▄▄▄██   ▒██▀▀█▄    ░▓█▄   ▌  ▒██▀▀█▄    ▒██   ██░  ▒██▄█▓▒   ▒  ▒   ██▒
  ▒██▒ ░   ░▒████  ▒▓█   ▓██▒  ░██▓ ▒██▒  ░▒████▓   ░██▓ ▒██▒░   ████▓▒░  ▒██▒ ░    ░▒██████▒▒
  ▒ ░░     ░░ ▒░   ░▒▒   ▓▒█░  ░ ▒▓ ░▒▓░   ▒▒▓  ▒   ░▒▓ ░▒▓░░   ▒░▒░▒░ ▒  ▓▒░ ░  ░  ▒ ▒▓▒ ▒ ░
    ░       ░ ░  ░   ▒   ▒▒ ░   ░▒ ░ ▒░ ░   ▒  ▒    ░▒ ░ ▒░  ░   ▒ ▒░ ░   ▒  ░       ░ ░▒  ░ ░
  ░           ░      ░   ▒      ░░   ░  ░   ░  ░    ░░   ░ ░ ░   ░ ▒  ░        ░  ░    ░  
              ░   ░      ░  ░    ░          ░        ░           ░ ░                    ░  
                                   ░                                          
```
-->

<p align='center'>
<a href="https://discord.io/TearDropsSupport"><img src="https://discordapp.com/api/guilds/765880027467350047/widget.png?style=banner2" alt="Link to discord server"><br>
<a href="https://www.python.org/"><img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="made with Python"></a>
<a href="https://github.com/Vyvy-vi/"><img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built with Love"></a><br>
<a href="https://raw.githubusercontent.com/Vyvy-vi/TearDrops/main/LICENSE"><img src="https://img.shields.io/github/license/Vyvy-vi/TearDrops?style=flat-square" alt="MIT license"></a>
<a href="https://github.com/Rapptz/discord.py/releases/tag/v1.5.0"><img src="https://img.shields.io/badge/discord.py-v1.5.0-7289da.svg?style=flat-square" alt="discord.py version"></a>
</p>



  
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-21-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<p align='right'>
   <a href="https://github.com/Vyvy-vi/TearDrops/releases/latest/"><img src="https://img.shields.io/badge/Bot_Version-v1.0.9-green.svg?style=flat-square" alt="bot version"></a>
</p>      


![sadblob](https://media.discordapp.net/attachments/771696574697832469/773264495006318623/sadblob.png)
![tears](.github/resources/crying.gif)
![cri](.github/resources/cri.png)


#### Python based discord bot built to add fun to the guild with memes, provide wisdom with book-recommendations along with XP rating system with <strong>TEARS</strong> currency.

A discord bot wrapped around the theme of tears and crying.
In concept, the idea is absurd but that's more of a reason to make this. :)
The bot uses tears as an economy and you can "cry" to get daily credit tears.

**NOTE**- It is recommended that you add your own discord token while running the bot.

## How to test the bot before running it on your server
To test the bot join this [Support Server](https://discord.gg/jTzGuYx)
  [*NOTE- Bot is not active 24x7 as it is hosted on heroku. To get a sample, join* [TearDropsSupport](https://discord.gg/jTzGuYx) *and ping* **@Tissue**]

## How to run the bot on your own server
[Invite the bot to your server](https://discord.com/api/oauth2/authorize?client_id=627772985872220161&permissions=379968&scope=bot)
[*NOTE- The bot is still in v0.1 and is being constantly updated and bug fixed. Inviting this, might have unintentional complications. If you really want the bot, open an issue so that we can provide a Beta Version to you that is stable and updated slowly*]

## Hosting the bot locally:

**NOTE**: To replicate this bot, you will need a bot **token**. Go get yours at https://discord.com/developers/ (If you need help with this step, feel free to ask for help in our [Support Server](https://discord.gg/jTzGuYx)).
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

## How to contribute
Before contributing, here is some information that might help your **PR (Pull Request)** get merged.
### How to set up the development environment
    
Requirements:
- git
- pip
- python `3.8.1` or higher

**Note**: If you're not on Windows, you should also have GNU make installed, and you can optionally install [pyenv](https://github.com/pyenv/pyenv), which can help you run tests for different python versions.

1. Fork and clone the repository with `git clone https://github.com/Vyvy-vi/TearDrops` 
1. Get in the clone directory using the command `cd TearDrops`
1. Execute the following command `python3 -m venv venv`
1. Activate the virtual environment with the following command:
    - Posix
    ```
    source .venv/bin/activate
    ```
    - Windows
    ```
    .venv\Scripts\activate
    ```
    
**Note**: From here onwards, we will assume you are executing commands from within this activated virtual environment.

**Note**: If you're comfortable with setting up virtual environments yourself and would rather do it manually, just run pip install -r bot/requirements.txt after setting it up.

### To contribute changes follow these steps:

**Note**: Make sure you have been assigned the issue to which you are making a PR. If you make PR before being assigned, It will be labeled invalid and closed without merging.


1. Add a upstream link to main branch in your cloned repo
  ```
  git remote add upstream https://github.com/Vyvy-vi/TearDrops.git
  ```
2. Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
  ```
  git pull upstream master
  ```
3. Create your feature branch
  ```
  git checkout -b <feature-name>
  ```
4. Commit all the changes
  ```
  git commit -am "Meaningful commit message"
  ```
5. Push the changes for review
  ```
  git push origin <branch-name>
  ```
6. Create a PR from our repo on Github.

### How to report a bug
Submit an issue on GitHub and add as much information as you can about the bug, with screenshots of inputs to the bot and bot response if possible (if the issue is regarding bugs). 

**Note**: Try to make issues that are not blank and are in their respective category.

**Note**: For more detailed information about how to contribute, please refere to the [CONTRIBUTING.md](https://github.com/Vyvy-vi/TearDrops/blob/main/CONTRIBUTING.md) file.

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
    <td align="center"><a href="https://allcontributors.org"><img src="https://avatars1.githubusercontent.com/u/46410174?v=4?s=100" width="100px;" alt=""/><br /><sub><b>All Contributors</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=all-contributors" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Vyvy-vi"><img src="https://avatars0.githubusercontent.com/u/62864373?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vyom Jain</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=Vyvy-vi" title="Code">💻</a> <a href="#projectManagement-Vyvy-vi" title="Project Management">📆</a> <a href="#design-Vyvy-vi" title="Design">🎨</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=Vyvy-vi" title="Documentation">📖</a> <a href="#maintenance-Vyvy-vi" title="Maintenance">🚧</a> <a href="https://github.com/Vyvy-vi/TearDrops/pulls?q=is%3Apr+reviewed-by%3AVyvy-vi" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://anubhav.codes"><img src="https://avatars0.githubusercontent.com/u/1628340?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anubhav</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=anubhavcodes" title="Code">💻</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=anubhavcodes" title="Documentation">📖</a> <a href="#ideas-anubhavcodes" title="Ideas, Planning, & Feedback">🤔</a> <a href="#infra-anubhavcodes" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/gamerrio"><img src="https://avatars0.githubusercontent.com/u/21240909?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Gamerrio</b></sub></a><br /><a href="#ideas-gamerrio" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=gamerrio" title="Code">💻</a> <a href="#design-gamerrio" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/RascalTwo"><img src="https://avatars0.githubusercontent.com/u/9403665?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rascal_Two</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/issues?q=author%3ARascalTwo" title="Bug reports">🐛</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=RascalTwo" title="Code">💻</a> <a href="#ideas-RascalTwo" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/sayand0122"><img src="https://avatars1.githubusercontent.com/u/53222600?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sayan Dutta</b></sub></a><br /><a href="#ideas-sayand0122" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=sayand0122" title="Code">💻</a> <a href="#design-sayand0122" title="Design">🎨</a></td>
    <td align="center"><a href="http://www.nhcarrigan.com"><img src="https://avatars1.githubusercontent.com/u/63889819?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nicholas Carrigan (he/him)</b></sub></a><br /><a href="#ideas-nhcarrigan" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=nhcarrigan" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://mikeysan.hashnode.dev"><img src="https://avatars1.githubusercontent.com/u/13338176?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael Mba</b></sub></a><br /><a href="#ideas-mikeysan" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/AllanRegush"><img src="https://avatars0.githubusercontent.com/u/17693494?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Allan Regush</b></sub></a><br /><a href="#ideas-AllanRegush" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=AllanRegush" title="Documentation">📖</a></td>
    <td align="center"><a href="https://mattcowley.co.uk/"><img src="https://avatars2.githubusercontent.com/u/12371363?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matt (IPv4) Cowley</b></sub></a><br /><a href="#ideas-MattIPv4" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/AbstractUmbra"><img src="https://avatars0.githubusercontent.com/u/16031716?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alex Nørgaard</b></sub></a><br /><a href="#ideas-AbstractUmbra" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/LazybuddyNK"><img src="https://avatars3.githubusercontent.com/u/59273928?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nitesh Kumar</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=LazybuddyNK" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/IcemanEtika"><img src="https://avatars0.githubusercontent.com/u/44535539?v=4?s=100" width="100px;" alt=""/><br /><sub><b>TJ LeBlanc</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=IcemanEtika" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/s04"><img src="https://avatars2.githubusercontent.com/u/70141652?v=4?s=100" width="100px;" alt=""/><br /><sub><b>s04</b></sub></a><br /><a href="#ideas-s04" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/SKULLXL"><img src="https://avatars3.githubusercontent.com/u/68315325?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rayn Islam</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/issues?q=author%3ASKULLXL" title="Bug reports">🐛</a> <a href="#ideas-SKULLXL" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/AkshayaKulasekaran"><img src="https://avatars2.githubusercontent.com/u/61582763?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Akshaya</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/issues?q=author%3AAkshayaKulasekaran" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/jveer634"><img src="https://avatars0.githubusercontent.com/u/47923507?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jay</b></sub></a><br /><a href="#ideas-jveer634" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=jveer634" title="Documentation">📖</a> <a href="https://github.com/Vyvy-vi/TearDrops/issues?q=author%3Ajveer634" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/mstanciu552"><img src="https://avatars3.githubusercontent.com/u/34579048?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mstanciu552</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=mstanciu552" title="Documentation">📖</a></td>
    <td align="center"><a href="https://utkarsh299-tech.github.io/myportfolio/"><img src="https://avatars3.githubusercontent.com/u/60184229?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Utkarsh Singh</b></sub></a><br /><a href="#ideas-Utkarsh299-tech" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Vyvy-vi/TearDrops/commits?author=Utkarsh299-tech" title="Documentation">📖</a></td>
    <td align="center"><a href="http://sreekaransrinath.github.io"><img src="https://avatars.githubusercontent.com/u/50989977?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sreekaran Srinath</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=sreekaransrinath" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/OBITORASU"><img src="https://avatars.githubusercontent.com/u/65222459?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Souhit Dey</b></sub></a><br /><a href="https://github.com/Vyvy-vi/TearDrops/commits?author=OBITORASU" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
