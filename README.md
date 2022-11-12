# hooligans-hangman-bot

![design2](./static/design2.png)

## Local Setup

1. clone the repo

2. create virtual environment for python libraries

```commandline
python3 -m venv hooligan-venv
```

3. activate virtual environment

```commandline
source hooligan-venv/bin/activate
```

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

## Sponsors

<p align="center">
  <a href="https://cdn.jsdelivr.net/gh/maxdemaio/sponsors/sponsors.svg">
    <img src='https://cdn.jsdelivr.net/gh/maxdemaio/sponsors/sponsors.svg'/>
  </a>
</p>
