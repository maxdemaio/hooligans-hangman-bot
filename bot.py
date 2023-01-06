# This example requires the 'message_content' intent.
import discord
import os
import random
from typing import Dict, List
from dotenv import load_dotenv
from model.game import Game

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# in-memory map of discord guild to hangman games
serverGameMap: Dict[int, Game] = {}


async def check_if_won(message: discord.Message, game: Game, guess: str, solution: str, guild_id: int) -> bool:
    if solution and solution == game.word:
        print("you won, pal", f"guild id: {guild_id}")
        await message.channel.send("you won, pal")
        await print_board(message, game, "", guild_id)
        await end_game(message, game, guild_id)
        return True
    if guess and game.uniqChars == len(game.rightGuesses):
        print("you won, pal", f"guild id: {guild_id}")
        await message.channel.send("you won, pal")
        await print_board(message, game, guess, guild_id)
        await end_game(message, game, guild_id)
        return True
    return False


async def check_if_lost(message: discord.Message, game: Game, guess: str, guild_id: int) -> bool:
    if game.totalGuesses == game.maxGuesses:
        print("you lost, bucko", f"guild id: {guild_id}")
        await message.channel.send("you lost, bucko")
        await print_board(message, game, guess, guild_id)
        await end_game(message, game, guild_id)
        return True
    return False


async def print_board(message: discord.Message, game: Game, guess: str, guild_id: int):
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

    print("printing board", f"guild id: {guild_id}")
    await message.channel.send(file=file, embed=embed)

    return


async def start_game(message: discord.Message, game: Game, guild_id: int):
    # check game state
    if game.word is None:
        # get random word from list of words.txt
        word: str = ""
        with open("words.txt", encoding='utf-8') as file:
            words: List[str] = file.readlines()
            word: str = random.choice(words).strip()
        game.word = word.lower()
        game.uniqChars = len(set(word))
        print("starting a game of hangman", f"guild id: {guild_id}")
        await message.channel.send('starting a game of hangman')
        await print_board(message, game, "", guild_id)
    else:
        print("game already in progress!", f"guild id: {guild_id}")
        await message.channel.send('game already in progress!')
    return


async def guess(message: discord.Message, game: Game, guild_id: int):
    # check game state
    if game.word is not None:
        mStrings: List[str] = message.content.split()
        # check if they passed a character to guess
        if len(mStrings) == 1:
            await message.channel.send("make a guess, homie")
            return
        # make guess
        guess: str = mStrings[1][0].lower()

        # check if already guessed
        if guess in game.wrongGuesses or guess in game.rightGuesses:
            print(f"you've alread guessed {guess}", f"guild id: {guild_id}")
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
        if await check_if_won(message, game, guess, "", guild_id):
            return
        # check if lost
        if await check_if_lost(message, game, guess, guild_id):
            return

        await print_board(message, game, guess, guild_id)
    else:
        print("game hasn't started", f"guild id: {guild_id}")
        await message.channel.send("game hasn't started")
    return


async def solve(message: discord.Message, game: Game, guild_id: int):
    # check game state
    if game.word is not None:
        # make solution guess
        mStrings: List[str] = message.content.split()

        # check if they passed a word to guess a solution
        if len(mStrings) == 1:
            print("make a solution guess, home", f"guild id: {guild_id}")
            await message.channel.send("make a solution guess, homie")
            return

        solution: str = mStrings[1]

        # check if already guessed
        if solution in game.solutions:
            print(f"you've already guessed {solution}", f"guild id: {guild_id}")
            await message.channel.send(f"you've already guessed {solution}")
            return

        game.addSolution(solution)

        # check if won
        if await check_if_won(message, game, "", solution, guild_id):
            return
        # check if lost
        game.incrGuesses()
        if await check_if_lost(message, game, "", guild_id):
            return

        await print_board(message, game, "", guild_id)
    else:
        print("game hasn't started", f"guild id: {guild_id}")
        await message.channel.send("game hasn't started")
    return


async def end_game(message: discord.Message, game: Game, guild_id: int):
    if game.word is not None:
        print(f"game ended, the answer was **{game.word}**", f"guild id: {guild_id}")
        await message.channel.send(f"game ended, the answer was **{game.word}**")
    else:
        print("game hasn't started", f"guild id: {guild_id}")
        await message.channel.send("game hasn't started")
    # remove server/game key/value pair from in-memory map
    if guild_id in serverGameMap:
        del serverGameMap[guild_id]
    return


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
    guild_id: int = message.guild.id
    if guild_id not in serverGameMap:
        serverGameMap[guild_id] = Game(word=None, maxGuesses=6, totalGuesses=0,
                                      wrongGuesses="", rightGuesses="", uniqChars=0, solutions=[])

    if message.content.startswith('$hello'):
        print("Hello!", f"guild id: {guild_id}")
        await message.channel.send('Hello!')

    if message.content.startswith('$hangman'):
        await start_game(message, serverGameMap[guild_id], guild_id)

    if message.content.startswith('$guess'):
        await guess(message, serverGameMap[guild_id], guild_id)

    if message.content.startswith('$solve'):
        await solve(message, serverGameMap[guild_id], guild_id)

    if message.content.startswith('$endgame'):
        await end_game(message, serverGameMap[guild_id], guild_id)


client.run(os.getenv('TOKEN'))
