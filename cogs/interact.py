import discord
from discord.ext import commands


import botconstants
import helper

class Interact(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        #val = await self.bot.process_commands(message)
        words = helper.make_readable_list(message.content.lower())
        if message.author == self.bot.user:
            return
        if ("cole" in words):
            await message.channel.send("Did somebody mention the greatest person on Earth?")
        
        if any(x in words for x in botconstants.reply_monch):
            await message.channel.send("<:ColeMonch:819365182114496514>")

        if ("ping" in words):
            await message.channel.send("Pong!")
        
        if ("pong" in words):
            await message.channel.send("Ping!")

        if ("thomas" in words):
            await message.channel.send("SOOOOOOOOOOOOOOOOOOOOOS!!!!")

    @commands.Cog.listener()
    async def on_ready():
        print("I am ready master.")


def setup(bot):
    bot.add_cog(Interact(bot))
