import asyncio
import discord
import os

from discord.ext import commands

class MyBot(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('----------')
        async for guild in bot.fetch_guilds():
            print('~ '+guild.name)


intents = discord.Intents.default()
description = 'BeeluBot v1.0'

bot = commands.Bot(
    command_prefix='!',
    description=description,
    intents = intents
)

async def main():
    async with bot:    
        await bot.add_cog(MyBot(bot))
        await bot.run(os.environ['TOKEN'])

asyncio.run(main())