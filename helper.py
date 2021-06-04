import os
import discord
from discord.ext import commands


#extention loader and Unloader
def load_cog(bot, cog):
    bot.load_extension('cogs.{}'.format(cog))

def unload_cog(bot, cog):
    bot.unload_extension('cogs.{}'.format(cog))

#loads all cogs
def load_cogs(bot):
    for cogs in os.listdir("./cogs"):
        cog = cogs.replace('.py', '')
    load_cog(bot, cog)
        
    
#returns a list of words in message
def make_readable_list(message):
    words = []
    word = ""
    for i in range(0, len(message)):
        if ((ord(message[i]) >= 97 and ord(message[i]) <= 122)):
            word += message[i]
            if(i == len(message) - 1):
                words.append(word)
        else:
            words.append(word)
            word = ""
    
    return words
