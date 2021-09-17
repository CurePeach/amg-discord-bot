"""
This file is the entryway to the bot. If you want to run the bot, this is the file you should run.
"""

# Package imports
import dotenv 
import os
import random
from discord.ext import commands

# Local imports
from src import dice

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="f")
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

  if MESSAGE.startswith("f"):
    await bot.process_commands(context)
  # TODO(someone): refactor this into its own file
  elif MESSAGE.startswith("<:misakihydrate:879345153041661963>"):
    await CHANNEL.send(f"Stay Hydrated! {MESSAGE}")
  elif "alright" in MESSAGE_WORDS:
    await CHANNEL.send("No you're all left! <:childefingerguns:879342498340823040>")
  elif AUTHOR_NAME.startswith("Rayshine69"):
    for word in MESSAGE_WORDS:
      if word in RAY_WORD_BANK:
        await CHANNEL.send("Raymond stop spending money!")
        break

@bot.command(name="roll")
async def echo(context, *, arg):
  """
  Basic command that rolls a combination of dice
  """
  CHANNEL = context.channel
  AUTHOR_NAME = context.author.name
  AUTHOR_USERNAME = context.author.display_name
  MESSAGE = arg.split()

  result, total = dice.roll(MESSAGE)

  if result == 0:
    await CHANNEL.send("Invalid dice roll you idiot")
  else:
    # Funny easter egg
    if AUTHOR_NAME.startswith("NightRaven"):
      if random.randint(1,2) == 1:
        total = 1
        result = "[1]"
    # Don't tell him
    await CHANNEL.send(f"__{AUTHOR_USERNAME}__ rolled {result} for a total of `{total}`")
    if total == 1:
      await CHANNEL.send("<:kekw:784692105678553138>")

bot.run(TOKEN)
