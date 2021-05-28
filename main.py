import discord
import os

#Client init
client = discord.Client()

#run client on server
client.run(os.getenv('TOKEN'))