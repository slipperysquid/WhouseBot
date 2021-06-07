import discord
from discord.ext import commands

import json


class Balance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        #returns false if user has account already
        open_account(ctx.author)
        #loading json
        users = get_bank_data()
        #Open wallet and bank
        usr_wall = users[str(ctx.author.id)]["wallet"]
        usr_bank = users[str(ctx.author.id)]["bank"]
        #Create Embed----------------------------------------------
        em = discord.Embed(title = "Bank Balance:",
                           color = discord.Color.red())

        em.set_author(name = ctx.author.display_name,
                      icon_url = ctx.author.avatar_url)

        em.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Mcol_money_bag.svg/1200px-Mcol_money_bag.svg.png")
        
        em.add_field(name = "Wallet Balance:", value = usr_wall, inline = True)
        em.add_field(name = "Bank Balance:", value = usr_bank, inline = True)



#helper functions----------------------------------------------------------------------------
def open_account(user):
    users = get_bank_data()

    if(user.id in users):
        return False
    else:
        users[str(user.id)]["wallet"] = "50"
        users[str(user.id)]["bank"] = "500"

    with open("bank.json", w) as f:
        json.dump(users, f)
    return True



def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)
    return users

#setup-------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog(Balance(bot))