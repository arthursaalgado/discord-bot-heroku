import asyncio
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print( f'{client.user} in online!\nCurrently connected to: ')
    async for guild in bot.fetch_guilds():
        print('- '+guild.name)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if

client.run(os.environ['TOKEN_KEY'])