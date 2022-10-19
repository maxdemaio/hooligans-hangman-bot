# This example requires the 'message_content' intent.
import discord
import os
from typing import List, Dict
from dotenv import load_dotenv

from gameLogic import startGame, guess, endGame
from model.game import Game

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# in-memory map of discord guild to hangman games
serverGameMap: Dict[int, Game] = {}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    game = discord.Game("$hangman")
    await client.change_presence(activity=game)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    # get discord guild of message event and relative game
    guildId: int = message.guild.id
    if guildId not in serverGameMap:
        serverGameMap[guildId] = Game(word=None, maxGuesses=6, totalGuesses=0, 
    wrongGuesses="", rightGuesses="", uniqChars=0)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hangman'):
        await startGame(message, serverGameMap[guildId])
    
    if message.content.startswith('$guess'):
        await guess(message, serverGameMap[guildId])

    if message.content.startswith('$endgame'):
        await endGame(message, serverGameMap[guildId])


client.run(os.getenv('TOKEN'))
