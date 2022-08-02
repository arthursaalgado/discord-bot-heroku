import asyncio
import logging
import os

from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{client.user.name} is online!\n Currently connect to:')
    async for guild in client.fetch_guilds():
        print('- '+guild.name)



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client.run(os.environ['TOKEN_KEY'])
