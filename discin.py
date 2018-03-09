import discord
from sys import argv
import discall

me = discord.Client()
config = open(".config", "r")
token = config.read()[:-1]
if len(argv) > 1:
    channellist = list(map(int,argv[1:]))
else:
    channellist = [] #defer
@me.event
async def on_ready():
    global channellist
    if channellist == []:
        channellist = [discall.pickchannel(me)]
    print("Ready!")
    
@me.event
async def on_message(message):
    if message.channel.id in channellist:
        print(str(message.author),": ", message.content)

me.run(token, bot=False)
