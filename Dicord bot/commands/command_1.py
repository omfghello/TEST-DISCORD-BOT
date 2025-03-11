import discord
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):