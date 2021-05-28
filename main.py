import discord
import os

#Client init
client = discord.Client()


#events

@client.event
async def on_ready():
    print("I am ready master.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if (message.content.lower() == "ping"):
        await message.channel.send("Pong!")

#run client on server
client.run(os.getenv('TOKEN'))