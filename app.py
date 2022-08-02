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
        rolls, limit = map(int, dice.split('d'))
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)
    except Exception:
        await ctx.send('O dado deve ser NdN')

@bot.command()
async def joined(ctx, message, member:discord.Member):
    """Says when a member joined."""

    #TODO :: faça a conta (O <usuário> entrou a <X unidade de tempo>)
    await message.reply(f'@{member.name} entrou em {member.joined_at}', mention_author = Trye)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(os.environ['TOKEN'])