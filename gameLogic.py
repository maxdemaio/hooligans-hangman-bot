import random
import discord
from model.game import Game

async def startGame(message: discord.Message, game: Game):
    # check game state if game already in progress
    if game.getWord() == None:
        # get random word from list of words.txt
        word: str = ""
        with open("words.txt", encoding = 'utf-8') as file:
            words: List[str]= file.readlines()
            word: str = random.choice(words).strip()
        game.setWord(word)
        await message.channel.send('starting a game of hangman')
    else:
        await message.channel.send('game already in progress!')
    return

async def guess(message: discord.Message, letter: chr, game: Game):
    return
    