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

@bot.event
async def on_message(context):
  """
  Waits until a particular message is sent and responds accordingly.
  """
  CHANNEL = context.channel
  AUTHOR = context.author.name
  #if "hello" in context.content.split():
  #  user = []
  #  for i in range(len(author)):
  #      if author[i] == "#":
  #          break
  #      user.append(author[i])
  #  await channel.send(f"Hello {''.join(user)}!")
  if context.content.startswith("f"):
    await bot.process_commands(context)
  elif context.content.startswith("<:misakihydrate:879345153041661963>"):
    await CHANNEL.send(f"Stay Hydrated! {context.content}")
  elif ("alright" in context.content.lower().split() or 
    "alright?" in context.content.lower().split()):
    await CHANNEL.send("No you're all left! <:childefingerguns:879342498340823040>")
  elif AUTHOR.startswith("Rayshine69"):
    await CHANNEL.send("Raymond stop spending money!")

bot.run(TOKEN)
