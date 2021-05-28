import discord
import os

import botconstants

#Client init
client = discord.Client()


#events

@client.event
async def on_ready():
    print("I am ready master.")

@client.event
async def on_message(message):

    readable_message = message.content.lower()

    if message.author == client.user:
        return
    if ("cole" in readable_message):
        await message.channel.send("Did somebody mention the greatest person on Earth?")
    
    if any(x in readable_message for x in constants.reply_monch):
        await message.channel.send("<:ColeMonch:819365182114496514>")
    
    if ("ping" in readable_message):
        await message.channel.send("Pong!")

#run client on server
client.run(os.getenv('TOKEN'))