import asyncio, discord
import os

from discord.ext import commands

#music.py
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    '''
    TODO: ADD MUSIC METHODS
    '''


#MainClinet.py
class MainClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('~~~~~~~~~~')

    @commands.command()
    async def roll(self, ctx, dice: str):
        '''Rola dados.

        Exemplo: !roll 1d6
                !roll 2d20'''
        try: 
            rolls, limit = map(int, dice.split('d'))
            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await ctx.send(result)
        except Exception:
            await ctx.send('O dado deve ser NdN')

    @commands.command()
    async def joined(self, ctx, message, member: discord.Member):
        """Diz a quanto tempo o camarada está entre a gente.

        Exemplo: !joined @beelu"""
        if(subcommand(ctx)):
            await message.reply(f'{member.name} entrou {member.joined_at}')
        else:
            await message.reply(f'Por favor mencione (@) o nome do usuário.')

    @commands.command(description='Uni-du-ni-tê')
    async def choose(self, message, *choices: str):
        '''Escolhe entre multiplas escolhas.

        Exemplo: !choose 1 2 3 4'''
        await message.reply(random.choice(choices))

    #misc
    async def subcommand(self, ctx):
        '''Checks if a subcommand is being invoked.'''
        return 1 if ctx.invoked_subcommand != None else 0


intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='!',
    intents = intents
)

async def setup(bot):
    await bot.add_cog(Music(bot))
    await bot.add_cog(MainClient(bot))
        

async def main():
    async with bot:
        await setup(bot)
        await bot.start(os.environ['TOKEN'])

asyncio.run(main())