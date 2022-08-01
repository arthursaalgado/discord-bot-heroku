import discord

class MyClient(discord.Client):
    async def on_ready():
        print(f'Logged on as {self.user}')
    
    async def on_message():
        print(f'Message from {self.author}: {self.content}')


client = MyClient()
client.run('7270b5127502d5e40f1b6d1d7fa0d1b105f696745ad66ce62dc2f19be690229d')
