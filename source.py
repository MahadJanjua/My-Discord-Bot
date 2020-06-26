# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
EXTENSIONS = (
    'cogs.Basics',
    'cogs.Voice',
    'cogs.ImageClassify'
)

class YummyBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        '''Initializes a YummyBot object'''
        # Bot parameters:
        extensions = kwargs.pop('extensions', EXTENSIONS)

        super().__init__(*args, **kwargs)
        
        # Loading the cogs:
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as err:
                print("Could not load following extension: ", extension)

        @self.event
        async def on_ready():
            print(f'{self.user} has connected to Discord!')

client = YummyBot(command_prefix='?mwo ')
client.run(TOKEN)