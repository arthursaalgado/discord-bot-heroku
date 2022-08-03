import asyncio
import discord
import os

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


intents = discord.Intents.default()
description = 'BeeluBot v1.0'

bot = commands.Bot(
    command_prefix='!',
    description=description,
    intents = intents
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})\nCurrently connected to:')
    async for guild in bot.fetch_guilds():
        print(' '+guild.name)

async def main():
    async with bot:    
        await bot.add_cog(Music(bot))
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())