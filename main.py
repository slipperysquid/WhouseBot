import discord
import os
from discord.ext import commands

import botconstants
import helper


#Bot command init
bot = commands.Bot(command_prefix = '~')
bot.remove_command('help')
#commands



#will say what the user tells the bont to say
@bot.command()
async def say(ctx, msg):
    await ctx.send(msg)


@bot.command()
async def help(ctx):
    await ctx.send("```{}```".format(botconstants.help_msg))
#events

@bot.event
async def on_ready():
    print("I am ready master.")

@bot.event
async def on_message(message):

    words = helper.make_readable_list(message.content.lower())
    print(words)
    if message.author == client.user:
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
