import discord
import random
from discord.ext import commands

class Basics(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_context=True) #this means that the following will use the set prefix!
    async def hello(self, ctx):
        return await ctx.send('mwo')

    @commands.command(
        name = '8ball',
        description = 'Magic 8-ball. Mysteriously always correct.',
        brief = '8-ball!',
        aliases = ['eight', '8-ball', 'eight-ball'],
        pass_context=True)
    async def eightball(self, ctx):
        possible_responses1 = [
            'That is a resounding no',
            'It does not look likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
            'Ask Mahad',
            'MWO MWO? MWO',
        ]
        return await ctx.send(random.choice(possible_responses1) + ", " + ctx.message.author.mention)
    
    @commands.command(
        name = 'flip',
        description = "Replies randomly with heads or tails!",
        brief = "Coin flip!",
        aliases=['coinflip', 'cointoss'],
        pass_context=True)
    async def coinflip(self, ctx):
        possible_responses = [
            'Heads :man:',
            'Tails',
        ]
        return await ctx.send(random.choice(possible_responses))
    
def setup(client):
    client.add_cog(Basics(client))