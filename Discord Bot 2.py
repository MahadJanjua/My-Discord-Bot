import random
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!", "?")
TOKEN = "TOKEN"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name = '8ball',
                description = "Answers a yes/no question.",
                brief = "Ask yes/no question.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses1 = [
        'That is a resounding no',
        'It does not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Ask Mahad',
        ]
    await client.say(random.choice(possible_responses1) + ", " + context.message.author.mention)

@client.command(name = 'flip',
                description = "Replies randomly with heads or tails!",
                brief = "Coin flip!",
                aliases=['coinflip', 'cointoss'],
                pass_context=True)
async def coin_flip(context):
    possible_responses2 = [
        'Heads',
        'Tails'
        ]
    await client.say(random.choice(possible_responses2) + "!")
    
@client.command()
async def square(number):
    square_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(square_value) + ".")

@client.command(name = 'hello',
                description = "replies with a common greeting!",
                brief = "Greets you",
                aliases=['Hello'],
                pass_context=True)
async def coin_flip(context):
    possible_responses3 = [
        'Hello',
        'Allo',
        'Hey',
        'Hi'
        ]
    await client.say(random.choice(possible_responses3) + ", " + context.message.author.mention)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans..."))
    await message.channel.send('Hello!')
    print("Logged in as " + client.user.name)
        
    

client.run(TOKEN)
