# This example requires the 'message_content' intent.
import discord
import os
import random
from typing import List
from dotenv import load_dotenv

from gameLogic import startGame
from models.Game import Game

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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
        # get random word from list of words.txt
        word: str = ""
        with open("words.txt", encoding = 'utf-8') as file:
            words: List[str]= file.readlines()
            word: str = random.choice(words).strip()
        # create a game and start it    
        game: Game = Game(word=word, maxGuesses=5, totalGuesses=0)
        await startGame(message, game)


client.run(os.getenv('TOKEN'))
