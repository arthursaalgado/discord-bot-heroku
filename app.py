import discord
import logging


with open('token', 'r') as file:
    TOKEN = file.read()

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}')
    
    async def on_message(self):
        print(f'Message from {self.author}: {self.content}')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encondig='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = MyClient()
client.run(TOKEN)
