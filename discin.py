import discord
from sys import argv

me = discord.Client()
channellist = list(map(int,argv[1:]))
config = open(".config", "r")
token = config.read()[:-1]

@me.event
async def on_ready():
    print("Ready!")
    
@me.event
async def on_message(message):
    if message.channel.id in channellist:
        print(str(message.author),": ", message.content)

me.run(token, bot=False)
