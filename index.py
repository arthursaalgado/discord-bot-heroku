import asyncio, discord
import os

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    '''
    TODO: ADD MUSIC METHODS
    '''

class Managing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('~~~~~~~~~~')

    '''
    TODO: ADD BASIC METHODS
    '''

intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='!',
    intents = intents
)

async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.add_cog(Managing(bot))
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())