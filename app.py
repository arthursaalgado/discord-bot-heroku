import asyncio
import os

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print( f'{bot.user.name} in online!\nCurrently connected to: ')
    async for guild in bot.fetch_guilds():
        print('- '+guild.name)

@bot.event
async def on_message(message):
	if (message.author == client.user) :
		return
	print(
		message.author,
		message.content,
		message.channel,
	)

	await message.channel.send('salve')

bot.run(os.environ['TOKEN_KEY'])