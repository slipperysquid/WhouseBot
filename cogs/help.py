import discord
from discord.ext import commands

import botconstants

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title = "List of commands", description = botconstants.help_msg, color = discord.Color.red())
        await ctx.send(embed = em)


#setup
def setup(bot):
    bot.add_cog(Help(bot))
