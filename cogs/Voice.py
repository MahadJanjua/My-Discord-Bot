import discord
import random
import youtube_dl
import os
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
from discord import FFmpegPCMAudio

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
        mwos = [
            'extra/mwo1.mp3',
            'extra/mwo2.mp3',
            'extra/mwo3.mp3'
        ]

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable="extra/ffmpeg.exe", source=random.choice(mwos)))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    
    @commands.command(name = 'play', aliases=['pl', 'p'], pass_context=True)
    async def play(self, ctx, url: str):
        for file in os.listdir("./"):
            if file == "song.mp3":
                os.remove("song.mp3")
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("song.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)




def setup(client):
    client.add_cog(Voice(client))