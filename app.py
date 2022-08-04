import discord
from discord.ext import commands

import os
import random

description = '''TODO: bot description'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('----------')
    async for guild in bot.fetch_guilds():
        print('~ '+guild.name)

@bot.command()
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

@bot.command()
async def joined(ctx, message, member: discord.Member):
    """Diz a quanto tempo o camarada está entre a gente.

    Exemplo: !joined @beelu"""
    if(subcommand(ctx)):
        await message.reply(f'{member.name} entrou {member.joined_at}')
    else:
        await message.reply(f'Por favor mencione (@) o nome do usuário.')
@bot.command(description='Uni-du-ni-tê')
async def choose(message, *choices: str):
    '''Escolhe entre multiplas escolhas.

    Exemplo: !choose 1 2 3 4'''
    await message.reply(random.choice(choices))

    async def subcommand(ctx):
        '''Checks if a subcommand is being invoked.'''
        return 1 if ctx.invoked_subcommand != None else 0



bot.run(os.environ['TOKEN'])