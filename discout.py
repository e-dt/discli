import discord
from sys import argv

me = discord.Client()
channel = int(argv[1])
config = open(".config", "r")
token = config.read()[:-1]



@me.event
async def on_ready():
    chan = me.get_channel(channel)
    print("Ready to send messages to " + chan.name + "!")
    while 1:
        inp = input("> ")
        if inp == "":
            inp = "_ _"
        await chan.send(inp)
    
me.run("MjY3NDMzODc3NzY3ODQ3OTQ2.DYCHqA.NwxsS_nRJCHCjSm39ubzhWD0RCs", bot=False)
