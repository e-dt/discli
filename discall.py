import discord

def pickchannel(me):
    guils = me.guilds
    print(number(guils))
    guild = guils[int(input("which? [0-n] numbering, choose by number"))]
    print(number(guild.channels))
    channel = guild.channels[int(input("which? [0-n] numbering, choose by number"))]
    return channel.id

def number(lst):
    endstr = ""
    for num,i in enumerate(lst):
        endstr += str(num) + " " + str(i) + "\n"
    return endstr




    
