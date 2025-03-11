import discord
from discord.ext import commands

import discord.state

class MyClient(discord.Client):
    async def on_ready(self):
        print("bot logged in as client")

if ConnectionError:
     
     print("Bot failed to connect to client")


description = "a bot"
status = discord.Status.online
activity = "testing bots"

activity = discord.Game(name= description)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('token')