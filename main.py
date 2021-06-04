import discord
import os
from discord.ext import commands

import botconstants
import helper


#Bot init
intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '%', intents = intents)
bot.remove_command('help')
#commands



#will say what the user tells the bot to say
@bot.command(name = 'say')
async def say(ctx, msg):
    await ctx.send(msg)


@bot.command(name = 'help')
async def help(ctx):
    print('helping')
    await ctx.send("```{}```".format(botconstants.help_msg))
#events

@bot.event
async def on_ready():
    print("I am ready master.")

@bot.event
async def on_message(message):

    words = helper.make_readable_list(message.content.lower())
    if message.author == bot.user:
        return
    if ("cole" in words):
        await message.channel.send("Did somebody mention the greatest person on Earth?")
        
    if any(x in words for x in botconstants.reply_monch):
        await message.channel.send("<:ColeMonch:819365182114496514>")

    if ("ping" in words):
        await message.channel.send("Pong!")
        
    if ("pong" in words):
        await message.channel.send("Ping!")


#run client on server
bot.run(os.getenv('TOKEN'))
