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
    '''Roda um dado NxN. 
    Meio incoerente'''
    try: 
        rolls, limit = map(int, dice.split('x'))
    except Exception:
        await ctx.send('O dado deve ser NxN')
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

'''

@bot.command()
async def joined(ctx, membe:discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} entrou {discord.utils.format_dt(member.joined_at)}')
'''

bot.run(os.environ['TOKEN'])