import discord
import random
import youtube_dl
import os
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
from discord import FFmpegPCMAudio
from .utils.opus_loader import load_opus_lib

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.last_audio = None


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
            'extra/mwos/mwo1.mp3',
            'extra/mwos/mwo2.mp3',
            'extra/mwos/mwo3.mp3'
        ]

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(random.choice(mwos)))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    
    @commands.command(pass_context=True)
    async def kevin(self, ctx):
        kevins = [
            'extra/kevin/kevin1.mp4',
            'extra/kevin/kevin2.mp4',
        ]

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(random.choice(kevins)))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    
    @commands.command(name = 'play', aliases=['pl', 'p'], pass_context=True)
    async def play(self, ctx, url: str):
        self.join(self, ctx)
        if self.last_audio == url:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("song.mp3"))
            ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        else:
            self.last_audio = url
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

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            await ctx.send("Paused the music :pause_button:")
        else:
            await ctx.send("No music is playing!")

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            voice.resume()
            await ctx.send("Resuming music :notes:")
        else:
            await ctx.send("No music to resume!")
    
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.stop()
            await ctx.send("Music stopped :stop_button:")
        else:
            await ctx.send("No music is currently playing!")



def setup(client):
    load_opus_lib()
    client.add_cog(Voice(client))