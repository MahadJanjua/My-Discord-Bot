# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

BOT_PREFIX = ("!", "?")
client = Bot(command_prefix=BOT_PREFIX)

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.lower() == '$hello' or message.content == '$mallo':
            response = str(message.content).replace("$", "") + " " + str(message.author).split("#", 1)[0] + "!"
            await message.channel.send(response)
        elif str(message.content).lower() == 'mwo':
            await message.channel.send('mwo')
    
    # @client.command(name = '8ball',
    #             description = "Answers a yes/no question.",
    #             brief = "Ask yes/no question.",
    #             aliases=['eight_ball', 'eightball', '8-ball'],
    #             pass_context=True)
    # async def eight_ball(self, context):
    #     possible_responses1 = [
    #         'That is a resounding no',
    #         'It does not look likely',
    #         'Too hard to tell',
    #         'It is quite possible',
    #         'Definitely',
    #         'Ask Mahad',
    #         'MWO?',
    #     ]
    #     await client.say(random.choice(possible_responses1) + ", " + context.message.author.mention)

client = CustomClient()
client.run(TOKEN)