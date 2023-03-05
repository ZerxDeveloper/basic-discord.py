import discord 
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True 
client = commands.Bot(command_prefix=".", intents=intents) # u can change Prefix if u want 
client.remove_command('help')

@client.event()
async def on_ready():
  print("Bot is ready!!") # this wil display in your cmd/terminal for notification if bot is online!
  
@client.command()
async def help(ctx):
  await ctx.send(""" ``` 
.help = Show List of Commands!!
.invite = Send Bot Invite!!
.github = Send my Github :D (You can change all this staff :D)
 ```""")
 
@client.command()
async def invite(ctx):
  await ctx.send("paste here your bot invite")
  
@client.command() 
async def github(ctx): 
  await ctx.send("https://github.com/ZerxDeveloper/")

client.run("bot token past here")
