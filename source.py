# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content == '$hello':
            response = "Hi " + str(message.author).split("#", 1)[0] + "!"
            await message.channel.send(response)
    
    async def eight_ball(self, context):
        possible_responses1 = [
            'That is a resounding no',
            'It does not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
            'Ask Mahad',
        ]
        await client.say(random.choice(possible_responses1) + ", " + context.message.author.mention)

client = CustomClient()
client.run(TOKEN)