import random
import datetime
import discord
from model.game import Game

async def checkIfWon(message: discord.Message, game: Game, guess: str, solution: str) -> bool:
    if solution and solution == game.word:
        await message.channel.send("you won, pal")
        await printBoard(message, game, "")
        await endGame(message, game)
        return True
    if guess and game.uniqChars == len(game.rightGuesses):
        await message.channel.send("you won, pal")
        await printBoard(message, game, guess)
        await endGame(message, game)
        return True
    return False


async def checkIfLost(message: discord.Message, game: Game, guess: str) -> bool:
    if game.totalGuesses == game.maxGuesses:
        await message.channel.send("you lost, bucko")
        await printBoard(message, game, guess)
        await endGame(message, game)
        await timeoutUser(message.author)
        return True
    return False


async def printBoard(message: discord.Message, game: Game, guess: str):
    # create --- string with right chars
    printWord = ""
    for letter in game.word:
        if letter in game.rightGuesses:
            printWord += letter
        else:
            printWord += "-"

    # create embed
    picture: str = "hangman" + str(game.totalGuesses) + ".png"
    file = discord.File("./static/" + picture, filename=picture)
    embed = discord.Embed(title="Hooligan Hangman", color=0xABA6A0)
    embed.set_image(url="attachment://" + picture)
    embed.add_field(name="word", value=printWord, inline=False)

    # only attach field if present
    if guess:
        embed.add_field(name="last guess", value=guess, inline=True)
    if game.solutions:
        solutionStr: str = " ".join(game.solutions)
        embed.add_field(name="solution guesses", value=solutionStr, inline=True)
    if game.wrongGuesses:
        embed.add_field(name="wrong guesses", value=game.wrongGuesses, inline=True)
    if game.rightGuesses:
        embed.add_field(name="right guesses", value=game.rightGuesses, inline=True)
    if game.totalGuesses > 0: 
        embed.add_field(name="total guesses", value=str(game.totalGuesses), inline=True)

    await message.channel.send(file=file, embed=embed)
    
    return


async def startGame(message: discord.Message, game: Game):
    # check game state
    if game.word == None:
        # get random word from list of words.txt
        word: str = ""
        with open("words.txt", encoding = 'utf-8') as file:
            words: List[str]= file.readlines()
            word: str = random.choice(words).strip()
        game.word = word
        game.uniqChars = len(set(word))
        await message.channel.send('starting a game of hangman')
        await printBoard(message, game, "")
    else:
        await message.channel.send('game already in progress!')
    return


async def guess(message: discord.Message, game: Game):
    # check game state
    if game.word != None:
        mStrings: List[str] = message.content.split()
        # check if they passed a character to guess
        if len(mStrings) == 1:
            await message.channel.send("make a guess, homie")
            return
        # make guess
        guess: str = mStrings[1][0]
    
        # check if already guessed
        if guess in game.wrongGuesses or guess in game.rightGuesses:
            await message.channel.send(f"you've already guessed {guess}")
            return
        # correct guess
        if guess in game.word:
            game.addRightGuess(guess)
        # incorrect guess
        else:
            game.incrGuesses()
            game.addWrongGuess(guess)

        # check if won
        if await checkIfWon(message, game, guess, ""):
            return
        # check if lost
        if await checkIfLost(message, game, guess):
            return

        await printBoard(message, game, guess)
    else:
        await message.channel.send("game hasn't started")
    return


async def solve(message: discord.Message, game: Game):
    # check game state
    if game.word != None:
        # make solution guess
        mStrings: List[str] = message.content.split()

        # check if they passed a word to guess a solution
        if len(mStrings) == 1:
            await message.channel.send("make a solution guess, homie")
            return

        solution: str = mStrings[1]

        # check if already guessed
        if solution in game.solutions:
            await message.channel.send(f"you've already guessed {solution}")
            return

        game.addSolution(solution)

        # check if won
        if await checkIfWon(message, game, "", solution):
            return
        # check if lost
        game.incrGuesses()
        if await checkIfLost(message, game, ""):
            return

        await printBoard(message, game, "")
    else:
        await message.channel.send("game hasn't started")
    return


async def endGame(message: discord.Message, game: Game):
    if game.word != None:
        await message.channel.send(f"game ended, the answer was **{game.word}**")
        game.resetGame()
    else:
        await message.channel.send("game hasn't started")
    return

async def timeoutUser(member: discord.Member):
    print("timeout!")
    until: datetime.datetime = (datetime.datetime.utcnow() + datetime.timedelta(minutes=1)).isoformat()
    print(until)
    print(member)
    return
    # await member.timeout(until, /, *, reason=None)
