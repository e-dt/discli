import discord
from sys import argv
import discall

me = discord.Client()    
config = open(".config", "r")
token = config.read()[:-1]



@me.event
async def on_ready():
    if len(argv) > 1:
        channel = int(argv[1])
    else:
        channel = discall.pickchannel(me)
    chan = me.get_channel(channel)
    print("Ready to send messages to " + chan.name + "!")
    while 1:
        inp = input("> ")
        if inp != "":
            await chan.send(inp)
    
me.run("MjY3NDMzODc3NzY3ODQ3OTQ2.DYCHqA.NwxsS_nRJCHCjSm39ubzhWD0RCs", bot=False)
