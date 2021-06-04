import discord
from discord.ext import commands

import botconstants

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        await ctx.send("```{}```".format(botconstants.help_msg))


#setup
def setup(bot):
    bot.add_cog(Help(bot))