import asyncio, discord
import os, random

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

class MyClient(commands.Cog):
    @commands.Cog.listener()
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('~~~~~~~~~~')

intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='!',
    intents = intents
)

async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.add_cog(Client(bot))
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())