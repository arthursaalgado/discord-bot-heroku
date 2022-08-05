import asyncio
from types import NoneType
import discord
import random
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
    async def roll(self, message, dice: str):
        '''Rola dados.

        Exemplo: `!roll 1d6`
                 `!roll 2d20`'''
        if (await self.subcommand(ctx)):
            try: 
                rolls, limit = map(int, dice.split('d'))
                result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
                await message.reply(result)
            except Exception:
                await message.reply('Especifique quantos dados e qual dado deve ser lançado.\nExemplo: `!roll 1d6`')
        else:
            await message.reply('Especifique quantos dados e qual dado deve ser lançado.\nExemplo: `!roll 1d6`')

    @commands.command()
    async def joined(self, ctx, message, member: discord.Member):
        """Diz a quanto tempo o camarada está entre a gente.

        Exemplo: !joined @beelu"""
        if(await self.subcommand(ctx)):
            await message.reply(f'{member.name} entrou {member.joined_at}')
        else:
            member = ctx.author
            await message.reply(f'{member.name} entrou {member.joined_at}')
    
    async def subcommand(self, ctx):
        '''Checks if a subcommand is being invoked.'''
        return await 1 if ctx.invoked_subcommand != None else 0


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

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