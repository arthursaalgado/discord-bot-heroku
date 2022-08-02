import asyncio
import os

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print( f'{bot.user.name} has connected to Discord on server!\nCurrently connected to: ')
    async for guild in bot.fetch_guilds():
        print('- '+guild.name)


bot.run(os.environ['TOKEN_KEY'])