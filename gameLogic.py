import random
import discord
from model.game import Game

async def printBoard(message: discord.Message, game: Game, guess: str):
    await message.channel.send(f"you guessed {guess}")
    await message.channel.send("wrong guesses: " + game.getWrongGuesses())
    await message.channel.send("right guesses: " + game.getRightGuesses())
    await message.channel.send("word: " + "_" * len(game.getWord()))
    await message.channel.send(f"you've made {game.getTotalGuesses()} guess{'es'[:game.getTotalGuesses()^1]}")
    return

async def startGame(message: discord.Message, game: Game):
    # check game state
    if game.getWord() == None:
        # get random word from list of words.txt
        word: str = ""
        with open("words.txt", encoding = 'utf-8') as file:
            words: List[str]= file.readlines()
            word: str = random.choice(words).strip()
        game.setWord(word)
        game.setUniqChars(len(set(word)))
        await message.channel.send('starting a game of hangman')
    else:
        await message.channel.send('game already in progress!')
    return


async def guess(message: discord.Message, game: Game):
    # check game state
    if game.getWord() != None:
        mStrings: List[str] = message.content.split()
        # check if they passed a character to guess
        if len(mStrings) == 1:
            await message.channel.send("make a guess, homie")
            return
        # make guess
        guess: str = mStrings[1][0]
        # check if already guessed
        if guess in game.getWrongGuesses() or guess in game.getRightGuesses():
            await message.channel.send(f"you've already guessed {guess}")
            return
        if guess in game.getWord():
            game.addRightGuess(guess)
        else:
            game.addWrongGuess(guess)
        # TODO: check if won/lost
        game.incrGuesses()
        await printBoard(message, game, guess)
    else:
        await message.channel.send("game hasn't started")
    return

