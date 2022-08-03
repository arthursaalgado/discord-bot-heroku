import asyncio
import discord
import os

from discord.ext import commands

class MyClient(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('----------')
        async for guild in bot.fetch_guilds():
            print('~ '+guild.name)


intents = discord.Intents.default()
description = 'BeeluBot v1.0'

client = commands.Bot(
    command_prefix='!',
    description=description,
    intents = intents
)

async def main():
    async with client:    
        await client.add_cog(MyClient(client))
        await client.run(os.environ['TOKEN'])

asyncio.run(main())