import asyncio, discord
import os, random

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

class Client(discord.Client):
    @bot.event
    async def on_ready():
        print('~~~~~~~~~~')
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('~~~~~~~~~~')

intents = discord.Intents.default()
description = '''BeeluBot v1.0.0'''

bot = commands.Bot(
    command_prefix='!',
    description=description,
    intents = intents
)

async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.add_cog(Client(bot))
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())