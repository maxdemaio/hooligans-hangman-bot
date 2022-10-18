# This example requires the 'message_content' intent.
import discord
import os
import random
from typing import List
from dotenv import load_dotenv

from gameLogic import startGame
from models.game import Game

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# create global game
game: Game = Game(word=None, maxGuesses=5, totalGuesses=0)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hangman'):
        # check game state if game already in progress
        if game.getWord() == None:
            # get random word from list of words.txt
            word: str = ""
            with open("words.txt", encoding = 'utf-8') as file:
                words: List[str]= file.readlines()
                word: str = random.choice(words).strip()
            game.setWord(word)
            await startGame(message, game)


client.run(os.getenv('TOKEN'))
