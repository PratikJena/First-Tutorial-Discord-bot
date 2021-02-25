import discord
from discord.ext import commands
import os

client=commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("Ready to go!")

@client.command()
async def ping(ctx)
await ctx.send("Pong!)

client.run(os.getenv(token))
