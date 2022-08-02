import discord
from discord.ext import commands

import os
import random

print(discord.__version__)

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id}')
    printt('----------')

@bot.command()
async def add(ctx, left:int, right:int):
    await ctx.send(left+right)

bot.run(os.getenv['TOKEN_KEY'])