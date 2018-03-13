import discord
from sys import argv
import discall

me = discord.Client()
config = open(".config", "r")
token = config.read()[:-1]
chanfile = open(".channel", "r")
if len(argv) == 2:
    channel = int(argv[1])
else:
    channel = None #defer
@me.event
async def on_ready():
    global channel
    if channel == None:
        channel = discall.pickchannel(me)
    print("Ready!")
    
@me.event
async def on_message(message):
    global channel
    if message.channel.id == channel:
        print(str(message.author),": ", message.content)
    channel = await check_chanchange()
        
async def check_chanchange():
    try:
        return int(chanfile.read())
    except:
        #print(int(chanfile.read())) #debug, remove...
        return channel
    
me.run(token, bot=False)
