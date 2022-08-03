import asyncio
import discord
import os

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix='!',
    intents = intents
)

@bot.event
async def on_ready():
    print('~~~~~~~~~~')
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('~~~~~~~~~~')


bot.add_cog(Music(bot))
bot.run(os.environ['TOKEN'])