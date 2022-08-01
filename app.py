import discord

class MyClient(discord.Client):
    async def on_ready():
        print(f'Logged on as {self.user}')
    
    async def on_message():
        print(f'Message from {self.author}: {self.content}')


client = MyClient()
client.run('MTAwMzcwMzMxNDc2NjExNDg5OA.GnboW4.s7KJru0qF59tmH_-OxQK5nOJ-VBVxXku4C45xE')
