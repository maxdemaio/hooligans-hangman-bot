import random
import discord
from model.game import Game

async def printBoard(message: discord.Message, game: Game, guess: str):
    # create --- string with right chars
    printWord = ""
    for letter in game.getWord():
        if letter in game.rightGuesses:
            printWord += letter
        else:
            printWord += "-"
    
    picture: str = "hangman" + str(game.getTotalGuesses()) + ".png"
    file = discord.File("./static/" + picture, filename=picture)

    # create embed
    embed = discord.Embed(title="Hooligan Hangman", color=0xABA6A0) #creates embed
    embed.set_image(url="attachment://" + picture)
    embed.add_field(name="word", value=printWord, inline=False)

    # only attach field if present
    if guess:
        embed.add_field(name="you guessesed", value=guess, inline=True)
    if game.getWrongGuesses():
        embed.add_field(name="wrong guesses", value=game.getWrongGuesses(), inline=True)
    if game.getRightGuesses():
        embed.add_field(name="right guesses", value=game.getRightGuesses(), inline=True)
    if game.getTotalGuesses() > 0: 
        embed.add_field(name="total guesses", value=str(game.getTotalGuesses()), inline=True)

    await message.channel.send(file=file, embed=embed)
    
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
        await printBoard(message, game, "")
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
            # increase total amount of guesses
            game.incrGuesses()
            game.addWrongGuess(guess)

        # check if won
        if game.getUniqChars() == len(game.getRightGuesses()):
            await message.channel.send("you won, pal")
            await printBoard(message, game, guess)
            await endGame(message, game)
            return

        # check if lost
        if game.getTotalGuesses() == game.getMaxGuesses():
            await message.channel.send("you lost, bucko")
            await printBoard(message, game, guess)
            await endGame(message, game)
            return
    
        await printBoard(message, game, guess)
    else:
        await message.channel.send("game hasn't started")
    return


async def endGame(message: discord.Message, game: Game):
    await message.channel.send(f"game ended, the answer was **{game.getWord()}**")
    game.resetGame()
    return