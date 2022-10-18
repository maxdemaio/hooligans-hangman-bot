# This example requires the 'message_content' intent.
import discord
import os
from typing import List
from dotenv import load_dotenv

from gameLogic import startGame, guess
from model.game import Game

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# create global game
game: Game = Game(word=None, maxGuesses=5, totalGuesses=0, 
    wrongGuesses="", rightGuesses="", uniqChars=0)

print("global game")
print(game)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    global game
    print("on message game")
    print(game)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hangman'):
        await startGame(message, game)
    
    if message.content.startswith('$guess'):
        await guess(message, game)



client.run(os.getenv('TOKEN'))
