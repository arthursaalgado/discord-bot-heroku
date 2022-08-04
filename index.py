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
class MyBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('~~~~~~~~~~')

    @commands.command()
    async def roll(self, ctx, dice: str):
        '''Rola dados.

        Exemplo: `!roll 1d6`
                 `!roll 2d20`'''
        try: 
            rolls, limit = map(int, dice.split('d'))
            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await ctx.send(result)
        except Exception:
            await ctx.send('Especifique quantos dados e qual dado deve ser lançado.\nExemplo: `!roll 1d6`')




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='!',
    intents = intents
)

async def setup(bot):
    await bot.add_cog(Music(bot))
    await bot.add_cog(MyBot(bot))
        

async def main():
    async with bot:
        await setup(bot)
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())