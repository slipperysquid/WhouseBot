import os
from discord.ext import commands

import botconstants
import helper


#Bot init
intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '~', intents = intents)
bot.remove_command('help')

#cog init
helper.load_cog(bot, 'say')
helper.load_cog(bot, 'interact')
helper.load_cog(bot, 'help')



#events
@bot.event
async def on_ready():
    print("I am ready master.")


#run client on server
bot.run(os.getenv('TOKEN'))
