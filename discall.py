import logging
import discord
me = discord.Client()
config = open(".config", "r")
token = config.read()[:-1]

@me.event
async def on_ready():
    guils = me.guilds
    print(number(guils))
    guild = guils[int(input("which? [0-n] numbering, choose by number"))]
    print("\n".join([str(x) + " " + str(x.id) for x in guild.channels]))
    await me.logout()

def number(lst):
    endstr = ""
    for num,i in enumerate(lst):
        endstr += str(num) + " " + str(i) + "\n"
    return endstr


me.run(token, bot=False)



    
