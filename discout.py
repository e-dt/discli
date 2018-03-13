import discord
import sys
import os
import discall

me = discord.Client()    
config = open(".config", "r")
token = config.read()[:-1]
chanfile = open(".channel", "w+")


@me.event
async def on_ready():
    global chanfile
    if len(sys.argv) == 2:
        channel = int(sys.argv[1])
    else:
        channel = discall.pickchannel(me)
    chan = me.get_channel(channel)
    print(channel)
    chanfile.write(str(channel))
    print("Ready to send messages to " + chan.name + "!")
    while 1:
        inp = input("> ")
        if inp == "":
            pass
        elif inp[0] == "/": # command
            splinp = inp.split(" ")
            if splinp[0] == "/sync":
                try:
                    chan.send("")
                except:
                    pass
            elif splinp[0] == "/join":
                try:
                    channel = int(splinp[1])
                except:
                    channel = discall.pickchannel(me)
                print(str(channel))
                chan = me.get_channel(channel)
                chanfile.write(str(channel))
            elif splinp[0] == "/quit":
                os.remove(".channel")
                await me.logout()
                exit()
            else:
                print("Invalid command!")
        else:
            await chan.send(inp)
    
me.run(token, bot=False)
