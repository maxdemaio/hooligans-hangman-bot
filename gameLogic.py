import discord
from models.Game import Game

async def startGame(message: discord.Message, game: Game):
    print(game)
    await message.channel.send('Starting a game of hangman!')
    return