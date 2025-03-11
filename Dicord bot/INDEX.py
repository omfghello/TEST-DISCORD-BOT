import discord
from discord.ext import commands

description = "a bot"
status = discord.Status.online
activity = "testing bots"

import discord.state

class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name=activity))
        print("bot logged in as client")
        
        if ConnectionError == True:
            print("Bot failed to connect to client")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTM0ODc0MzE0MTk0NzIxNTg3Mw.Gn8c5J.9mDeoSIGslwPIVtDvSbYvzWS0j6nnGAcDFO4Og')