"""
This file is the entryway to the bot. If you want to run the bot, this is the file you should run.
"""

# Package imports
import dotenv 
import os
from discord.ext import commands
import discord

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

@bot.command(name="bday")
async def echo(context, *, arg):
  """
  Birthday command that sends a birthday message to a specified user.
  If arg has the string 'late', then a different message is sent instead.
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

@bot.command(name="embed")
async def embed(context, *, arg):
  """
  Embed command repeats what the user says in an embedded message.
  Different flags can be set with a hyphen. 
  -c: Set the colour of the message (default: yellow 0xFEE75C)
  -t: Set the title of the message
  -s: Set the author of the message to be the current server
  """
  ARGS = arg.split("-")
  DESC = ARGS[0]
  COLOUR = 0xFEE75C # yellow 
  SHOW_SERVER = False
  SHOW_TITLE = False
  for item in ARGS[1:]:
    parts = item.split()
    flag = parts[0]
    content = item[2: ] # Past the hyphen and flag letter
    if flag == "c":
        COLOUR = int(content, 16)
    elif flag == "t":
        TITLE = content
        SHOW_TITLE = True
    elif flag == "s":
        SHOW_SERVER = True

  if SHOW_TITLE:
    EMBED = discord.Embed(title = TITLE, description = DESC, colour = COLOUR)
  else:
    EMBED = discord.Embed(description = DESC, colour = COLOUR)

  if SHOW_SERVER:
    GUILD = context.message.guild
    AUTHOR = GUILD.name
    ICON_URL = GUILD.icon_url
    EMBED.set_author(name = AUTHOR, icon_url = ICON_URL)
  await context.send(embed = EMBED)

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
