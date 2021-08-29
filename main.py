"""
This file is the entryway to the bot. If you want to run the bot, this is the file you should run.
"""

# Package imports
import dotenv 
import os
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="f")

@bot.event
async def on_ready():
  """
  Indication of whether or not the bot has activated.
  """
  print(f"{bot.user} has connected to Discord!")
  print("And connected to the servers:")
  for guild in bot.guilds:
    print(f"\t{guild.name}")

@bot.command(name="echo")
async def echo(context, *, arg):
  """
  Basic echo command that repeats what the user says and deletes the message that invoked it.
  """
  await context.message.delete()
  await context.send(arg)

bot.run(TOKEN)
