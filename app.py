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
async def on_message(ctx):
	print(
		ctx.author,
		ctx.content,
		ctx.guild,
	)
	await ctx.send('salve')

bot.run(os.environ['TOKEN_KEY'])