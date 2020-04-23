import os

import discord
from discord.ext import commands
import csv

TOKEN = 'YOUR TOKEN GOES HERE'

client = discord.Client()

def generate_words():
    l = ["l", "I", "1", "|", "ï", "ì", "í"]
    o = ["0"]
    words = ["polis", "p0lis"]
    for i in l:
        words.append("po" + i + "is")
        words.append("p0" + i + "is")
    new = []
    for word in words:      
        for i in l:
            aux = word[:3] + i + "s"
            new.append(aux)

    words.append("update")
    return words + new

async def should_we_ban(user):
    response = "hi"
    for word in words:
        if (word in user.name.lower()):
            print(user.name.lower())
            response = await user.ban()
    return response

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await should_we_ban(member)

@client.event
async def on_user_update(before, after):
    await should_we_ban(after)

@client.event
async def on_member_update(before, after):
    await should_we_ban(after)

words = generate_words()

client.run(TOKEN)