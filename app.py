import discord

class MyClient(discord.Client):
    async def on_ready():
        print(f'Logged on as {self.user}')
    
    async def on_message():
        print(f'Message from {self.author}: {self.content}')


client = MyClient()
client.run('LIUqR-7zBHSeMtTMZrMEqZ7of_8iYMny')
