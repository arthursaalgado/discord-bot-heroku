import asyncio
import discord
import os

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


intents = discord.Intents.default()

client = commands.Bot(
    command_prefix='!',
    intents = intents
)

@client.event
async def on_ready():
    print('~~~~~~~~~~')
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('~~~~~~~~~~')

async def main():
    with client:
        await client.add_cog(Music(client))
        await client.start(os.environ['TOKEN'])

asyncio.run(main())