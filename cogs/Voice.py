import discord
import random
from discord.ext import commands
from discord.voice_client import VoiceClient

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def join(self, ctx):
        vc = await ctx.message.author.voice.channel.connect()
    
    @commands.command(
        name = 'leave',
        pass_context=True
    )
    async def destroy(self, ctx):
        for x in self.client.voice_clients:
            if(x.guild == ctx.message.guild):
                return await x.disconnect()

def setup(client):
    client.add_cog(Voice(client))