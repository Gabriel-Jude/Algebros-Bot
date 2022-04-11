import discord
from discord import guild
from discord import embeds
from discord import message
from discord.ext import commands
import random
from typing import ValuesView
import os
from keep_alive import keep_alive

from discord.ext.commands.core import has_guild_permissions

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Wakey Wakey I am {0.user}'.format(client))

@client.command()
async def poll(ctx,*,message):
  emb=discord.Embed(title=" POLL ",description=f"{message}")
  msg=await ctx.channel.send(embed=emb)
  await msg.add_reaction('🇾')
  await msg.add_reaction('🇳')

keep_alive()
client.run(os.environ['TOKEN'])