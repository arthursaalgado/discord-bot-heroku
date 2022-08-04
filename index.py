import asyncio, discord
import os

from discord.ext import commands

#music.py
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    '''
    TODO: ADD MUSIC METHODS
    '''


#MainClient.py
class MainClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('~~~~~~~~~~')

    @commands.command()
    async def hello(self, message):
        await message.reply('wassup')



intents = discord.Intents.default()
intents = message_content = True

bot = commands.Bot(
    command_prefix='!',
    intents = intents
)

async def setup(bot):
    await bot.add_cog(Music(bot))
    await bot.add_cog(MainClient(bot))
        

async def main():
    async with bot:
        await setup(bot)
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())