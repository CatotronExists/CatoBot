### CATOBOT ###
## Created by @Catotron // youtube.com/@catotron // for use in discord.gg/vxZnsy2 (Catotron's World)
# Modules #
import datetime
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from Config import version, guild_ID
from Keys import bot_token, client, dev_mode
import pymongo
#         #

# Terminal Colors #
import os
os.system("")
CLEAR = '\33[0m'
CGREEN = '\33[92m'
CBLUE = '\33[34m'
CRED = '\33[91m'
CYELLOW = '\33[93m'
CBEIGE = '\33[36m'
CBOLD = '\033[1m'
#                 #

# Issues
#startup prints twice
#/shutdown also loads all commands again

# Vars #
command_list = ["bot_stats", "user_lookup", "command_leaderboard"]
#      #

### Discord Setup
intents = nextcord.Intents.all()
bot = commands.Bot()

### Terminal Functions
def formatOutput(output, status):
    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
    if status == "Normal": print("| "+str(current_time)+" || "+output)
    elif status == "Good": print(CGREEN +"| "+str(current_time)+" || "+output+ CLEAR)
    elif status == "Error": print(CRED +"| "+str(current_time)+" || "+output+ CLEAR)
    elif status == "Warning": print(CYELLOW +"| "+str(current_time)+" || "+output+ CLEAR)

### Save Functions
async def save(command, userID):
    updateCommandUsage(command, userID)
    updateCommandsUsed(command)
    updateCommandsSent(userID)

def updateCommandUsage(command, userID):
    formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
    try:
        
        formatOutput(output="    Command Usage Successfully Saved", status="Good")
    except Exception as e: formatOutput(output="    Error occured while saving: "+str(e), status="Error")

def updateCommandsUsed(command): pass

def updateCommandsSent(userID): pass

### Startup
error = False
startup_start_time = datetime.datetime.now().strftime('%M:%S.%f')[:-3]
start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("<<<------ Catobot "+str(version)+" Terminal ------>>>")
print(CBLUE +"Current Time: "+str(start_time)+ CLEAR)
print(CYELLOW +"Connecting to MongoDB..."+ CLEAR)

try: # Ping MongoDB
    client.admin.command('ping')
    print(CGREEN + "    Successfully connected to MongoDB" + CLEAR)
except Exception as e:
    error = True
    print(e)
    input(CRED + "    There was an error connecting to MongoDB\nError: " + str(e) + CLEAR)

if error == True: ready = False # END if no connection
else:
    print(CBLUE + "--------------------------" + CLEAR)
    print("Bot is starting up...")
    print("Loading Bot Settings...")
    print(CBOLD + "--->> Version: "+str(version)+"\n--->> Dev Mode = "+str(dev_mode)+"\n--->> Guild: "+str(guild_ID)+ CLEAR)
    print("\nConnecting to Discord...")
    print("Loading Commands...")
    for i in command_list:
        try: 
            bot.load_extension("Commands."+i)
            formatOutput(output="    /"+i+" Successfully Loaded", status="Good")
        except Exception as e: 
            formatOutput(output="    /"+i+" Failed to Load // Error: "+str(e), status="Warning")
    @bot.event
    async def on_ready():
        startup_end_time = datetime.datetime.now().strftime('%M:%S.%f')[:-3]
        startup_time_delta = datetime.datetime.strptime(startup_end_time,'%M:%S.%f') - datetime.datetime.strptime(startup_start_time,'%M:%S.%f')
        startup_time = int((startup_time_delta.total_seconds())*1000)
        print(CGREEN + f"-----------------------------------------------\n| Logged on as {bot.user}\n| Running Version "+version+"\n| Time Taken: "+str(startup_time)+" ms\n-----------------------------------------------"+ CLEAR)

### Core Commands
# Shutdown
@bot.slash_command(guild_ids=[guild_ID], name="shutdown", description="Turns off the bot")
async def shutdown(interaction: nextcord.Interaction):
    command = 'shutdown'
    userID = interaction.user.id
    if interaction.user.guild_permissions.administrator == True: # is Admin
        await interaction.send("Shutting Down")
        await save(command, userID)
        try: 
            formatOutput(output="    Shutting Down Bot", status="Good")
            await bot.close()
        except Exception as e: formatOutput(output="    Shutdown Failed // Error: "+str(e), status="Error")
    else: # not Admin
        await interaction.send("Insufficient Permissions\nMissing Administrator Permissions")
        await save(command, userID)
        formatOutput(output="    Insufficient Permissions for "+str(userID), status="Warning")

# Reload
@bot.slash_command(guild_ids=[guild_ID], name="reload", description="Reload Bot Commands")
async def CommandName(interaction: nextcord.Interaction):
    await interaction.response.defer(with_message=True)

    formatOutput(output="Refreshing Commands", status="Normal")
    for i in command_list:
        try: 
            bot.reload_extension("Commands."+i)
            formatOutput(output="    /"+i+" Successfully Refreshed", status="Good")
        except Exception as e: 
            formatOutput(output="    /"+i+" Failed to Reload // Error: "+str(e), status="Warning")

    await interaction.send("Commands Reloaded")
    command = 'command_name'
    userID = interaction.user.id
    await save(command, userID)

# ON JOIN
# Create a "placeholder" user file
# user ID is an int
# all else is a string

# @bot.event()
# async def on_member_join(member: nextcord.Member):
#     userID = member.id
#     formatOutput(output="", status="")

# perk tree for leveling????

bot.run(bot_token)