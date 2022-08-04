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


#MainClinet.py
class MainClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('~~~~~~~~~~')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('salve')

    #misc
    async def subcommand(self, ctx):
        '''Checks if a subcommand is being invoked.'''
        return 1 if ctx.invoked_subcommand != None else 0


intents = discord.Intents.default()
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