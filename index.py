import asyncio, discord
import os, random

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

class Client(commands.Cog):
    @commands.command()
    async def roll(ctx, dice: str):
        '''Rola dados.

        Exemplo: !roll 1d6
                !roll 2d20'''
        try: 
            rolls, limit = map(int, dice.split('d'))
            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await ctx.send(result)
        except Exception:
            await ctx.send('O dado deve ser NdN')
            
    @commands.command()
    async def joined(ctx, message, member: discord.Member):
        """Diz a quanto tempo o camarada está entre a gente.

        Exemplo: !joined @beelu"""
        if(subcommand(ctx)):
            await message.reply(f'{member.name} entrou {member.joined_at}')
        
    @commands.command(description='Uni-du-ni-tê')
    async def choose(message, *choices: str):
        '''Escolhe entre multiplas escolhas.

        Exemplo: !choose 1 2 3 4'''
        await message.reply(random.choice(choices))

    async def subcommand(ctx):
        '''Checks if a subcommand is being invoked.'''
        return 1 if ctx.invoked_subcommand != None else 0

intents = discord.Intents.default()
description = '''BeeluBot v1.0.0'''

bot = commands.Bot(
    command_prefix='!',
    description=description,
    intents = intents
)

@bot.event
async def on_ready():
    print('~~~~~~~~~~')
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('~~~~~~~~~~')

async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.add_cog(Client(bot))
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())