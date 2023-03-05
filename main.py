import discord 
from discord.ext import commands, has_permissions

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
.kick = Kick member from Discord Server
 ```""")
 
@client.command()
async def invite(ctx):
  await ctx.send("paste here your bot invite")
  
@client.command() 
async def github(ctx): 
  await ctx.send("https://github.com/ZerxDeveloper/")

@client.command()
@commands.has_permissions(Administrator=True) # This means What Permissions need member for use this command
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} Has been kicked from this server!")
    
@error.kick # error message if the member used the command without enough permissions!
async def mute_error(ctx, error): 
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Sorry, You Don't have Permissions to use this command!")
  
client.run("bot token past here")
