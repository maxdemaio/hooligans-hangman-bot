# hooligans-hangman-bot

![design2](./static/design2.png)

Invite the bot to your Discord server with this link: (https://discord.com/api/oauth2/authorize?client_id=1029887727438676019&permissions=2048&scope=bot](https://discord.com/api/oauth2/authorize?client_id=1029887727438676019&permissions=2048&scope=bot). The only permission needed is to send messages.

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

1. build image

```commandline
docker build -t hooligans-hangman-bot .
```

2. run container with env variable

```commandline
docker run -e TOKEN='exampleToken' exampleImageId
```
