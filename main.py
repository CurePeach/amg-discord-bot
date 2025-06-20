"""
This file is the entryway to the bot. If you want to run the bot, this is the file you should run.
"""

# Package imports
import dotenv 
import os
import discord
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="f", intents=intents)
BOT_ID = 880775837522198528

@bot.event
async def on_ready():
  """
  Indication of whether or not the bot has activated.
  """
  print(f"{bot.user} has connected to Discord!")
  print("And connected to the servers:")
  for guild in bot.guilds:
    print(f"\t{guild.name}")

@bot.command(name="bday")
async def echo(context, *, arg):
  """
  Birthday command that sends a birthday message to a specified user.
  if arg has the string 'late', then a different message is sent instead.
  """
  await context.message.delete()
  ARGS = arg.split()
  if "late" in ARGS:
    # Assumption that there is only one specifed user 
    ARGS.remove("late")
    await context.send(f"{ARGS[0]} Happy late froggers birthday! <:frogsit:821689317042814988>")
  else:
    await context.send(f"{arg} Happy froggers birthday! <:frogsit:821689317042814988>")

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
  AUTHOR_NAME = context.author.name
  AUTHOR_ID = context.author.id
  MESSAGE = context.content
  MESSAGE_SPLIT = MESSAGE.lower().split()
  MESSAGE_WORDS = [a.strip(',.?! ') for a in MESSAGE_SPLIT]
  RAY_WORD_BANK = ['credit', 'account', 'money', 'whale', 'saving', 'savings', 
  'dolphin', 'spend', 'spent', 'spending', 'spends', 'accounts', 'card', 'buy', 
  'buying', 'bought']

  # If the bot is the author of the message, do not apply an event to it.
  if AUTHOR_ID == BOT_ID:
    return

  #if "hello" in context.content.split():
  #  user = []
  #  for i in range(len(author)):
  #      if author[i] == "#":
  #          break
  #      user.append(author[i])
  #  await channel.send(f"Hello {''.join(user)}!")

  if MESSAGE.startswith("f"):
    await bot.process_commands(context)
  elif MESSAGE.startswith("<:misakihydrate:879345153041661963>"):
    await CHANNEL.send(f"Stay Hydrated! {MESSAGE}")
  elif "alright" in MESSAGE_WORDS:
    await CHANNEL.send("No you're all left! <:childefingerguns:879342498340823040>")
  elif AUTHOR_NAME.startswith("Rayshine69"):
    for word in MESSAGE_WORDS:
      if word in RAY_WORD_BANK:
        await CHANNEL.send("Raymond stop spending money!")
        break

bot.run(TOKEN)
