# hooligans-hangman-bot

![design2](./static/design2.png)

## Local Setup

1. clone the repo

2. create virtual environment for python libraries

```commandline
python3 -m venv venv
```

3. activate virtual environment

macOS way to do it:

```commandline
source venv/bin/activate
```

windows way to do it:

```commandline
venv\Scripts\activate.bat
```

If you'd like to deactivate the environment, type `deactivate` in your respective terminal where the virtual environment is active.

4. install required libraries from requirements.txt

```commandline
pip3 install -r requirements.txt
```

5. create a bot through discord's website, create a `.env` file like [env.example](./env.example), and paste the token there

6. invite the bot to your server and run the bot

```commandline
python3 bot.py
```

## Docker Setup

1. pull latest image from docker hub - https://hub.docker.com/repository/docker/maxwelldemaio/hooligans-hangman-bot

```commandline
docker pull maxwelldemaio/hooligans-hangman-bot:latest
```

2. run container with env variable

```commandline
docker run -e TOKEN='exampleToken' maxwelldemaio/hooligans-hangman-bot:latest
```

## Dictionary Curation

On my Mac, I started with the [local dictionary](<https://en.wikipedia.org/wiki/Words_(Unix)>) located at:

```
/usr/share/dict/words
```

Then, I created a histogram of the [Scrabble](https://en.wikipedia.org/wiki/Scrabble) scores of each dictionary word.

Once this histogram was created, I used integration to find the area under the curve. This is the cumulative probability distribution. This distribution levels out at the total count of all words in the dictionary. Using this, I was able to determine which bins are in the first, second, and third thirds of the distribution. These buckets correspond to easy, medium, and hard difficulties.

## Usages

- $hangman
  - $hangman {difficulty}
- $guess {guess}
- $solve {solution}
- $endgame

- [rankings.ipynb](./rankings.ipynb)

## Sponsors

<p align="center">
  <a href="https://cdn.jsdelivr.net/gh/maxdemaio/sponsors/sponsors.svg">
    <img src='https://cdn.jsdelivr.net/gh/maxdemaio/sponsors/sponsors.svg'/>
  </a>
</p>
