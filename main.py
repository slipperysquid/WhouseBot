import os
import discord
from discord.ext import commands

import botconstants
import helper


#Bot init
intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '~', intents = intents)
bot.remove_command('help')

#cog init
helper.load_cogs(bot)

#run bot
bot.run(os.getenv('TOKEN'))
