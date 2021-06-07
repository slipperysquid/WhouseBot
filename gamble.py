import discord
from discord.ext import commands

class Gamble(commands.command):

    def __init__(self, bot):
        self.bot = bot