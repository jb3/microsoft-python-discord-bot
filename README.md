# microsoft-python-discord-bot
A bot for the Microsoft Python Discord community

## Setup

### Install poetry

Get the latest version of Poetry from https://python-poetry.org/.

Confirm installation by running `poetry -V`, you can expect to see an output like:
```
$ poetry -V
Poetry version 1.0.9
```

### Install dependencies

Run `poetry install` to install all dependencies needed to run the bot.

### Create a Discord application

Check out the guide from the discord.py docs on how to create a bot account: https://discordpy.readthedocs.io/en/latest/discord.html

Additionally invite the bot to your server at this stage.

### Create a .env file

Secrets are stored in the `.env` file.

You should create a `.env` file that looks like the following:

```
TOKEN=<the token from the Developer website>
```

### Create a non-secret TOML file

For configuration that is not a secret a TOML file is used. The defaults should be good enough for most people but if you want to override them then you can create a file named `config.toml` which will be used instead of the defaults.

### Run the bot!

You can run the bot with `poetry run bot`.
