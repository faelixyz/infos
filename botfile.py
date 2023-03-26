######################

#!#!#!#!#!#!#!#!#!#!#!
# Zuerst Py-Cord installieren: 
# Bei mac:
# cmd + space, terminal eingeben, und dann:
## python3 -m pip install py-cord ##
#bei Windows: 
# Windows Taste, cmd eingeben und dann:
## pip install py-cord ##


# Hier der Bot Code, sobald Py-Cord installiert wurde:
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import time
import discord
from discord.ext import commands
from discord import utils
bot = discord.Bot()
from datetime import time, timezone
from discord.ext import tasks
import random as rd
BotToken = "discord.com/developers"
client = discord.Client
intents = discord.Intents().all()
from discord.ext import commands
Client= commands.Bot(command_prefix="$", intents=intents)
discord.Activity(name="einen Film :)", type=5)
import discord
import re
from discord.ext import commands
from discord.ext import commands
from discord.utils import get
from discord import Embed, Color
from discord.utils import *
import os
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio
client = discord.Client()
#guild = 1025086724105318471
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "$", intents = intents)
client.remove_command("help")
from discord.ext import tasks, commands

@bot.slash_command()
async def get_help(ctx):
  await ctx.respond("Hi!)
                    
#NICHT EDITIEREN!
bot.run(BotToken)
