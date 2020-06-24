import discord
import random
from discord.ext import commands
from discord.voice_client import VoiceClient

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def join(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = self.client.voice_clients

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else: voice = await channel.connect()
        await ctx.send(f"Joined {channel}")
        
    
    @commands.command(name = 'leave', pass_context=True)
    async def destroy(self, ctx):
        channel = ctx.message.author.voice.channel
        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"Left {channel}")
    
    @commands.command(name = 'mwo', pass_context=True)
    async def mwo(self, ctx):
        channel = ctx.message.author.voice.channel

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable="extra/ffmpeg.exe", source="extra/mwo.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)



def setup(client):
    client.add_cog(Voice(client))