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
        # save data
        formatOutput(output="    Successfully Saved", status="Good")
    except Exception as e: formatOutput(output="        Error occured while saving: "+str(e), status="Error")

def updateCommandsUsed(command): pass

def updateCommandsSent(userID): pass

### Startup
error = False
start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("<<<------ Catobot "+ str(version)+" Terminal ------>>>")
print(CBLUE + "Current Time: "+str(start_time)+ CLEAR)
print(CYELLOW + "Connecting to MongoDB..."+ CLEAR)

try: # Ping MongoDB
    client.admin.command('ping')
    print(CGREEN + "Successfully connected to MongoDB" + CLEAR)
except Exception as e:
    error = True
    print(e)
    input(CRED + "There was an error connecting to MongoDB\nError: " + str(e) + CLEAR)

if error == True: ready = False # END if no connection

else:
    print(CBLUE + "--------------------------" + CLEAR)
    print("Bot is starting up...")
    print("Loading Bot Settings...")
    print(CBOLD + "Version: "+str(version)+"\nDev Mode = "+str(dev_mode)+"\nGuild: "+str(guild_ID)+ CLEAR)
    print("\nConnecting to Discord...")

    @bot.event
    async def on_ready():
        end_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        startup_time = datetime.datetime.strptime(end_time,'%d-%m-%Y %H:%M:%S') - datetime.datetime.strptime(start_time,'%d-%m-%Y %H:%M:%S')
        print(CGREEN + f"-----------------------------------------\n| Logged on as {bot.user}\n| Running Version "+version+"\n| Time Taken: "+str(startup_time)+"\n-----------------------------------------"+ CLEAR)

### Slash Commands
@bot.slash_command(guild_ids=[guild_ID], name="shutdown", description="Turns off the bot")
async def testCommand(interaction: nextcord.Interaction):
    await interaction.send("Shutting Down Bot!")
    command = 'shutdown'
    userID = interaction.user.id
    await save(command, userID)

@bot.slash_command(guild_ids=[guild_ID], name="bot_stats", description="Displays stats for the bot")
async def botStats(interaction: nextcord.Interaction):
    await interaction.send("Bot Stats")
    command = 'bot_stats'
    userID = interaction.user.id
    await save(command, userID)

@bot.slash_command(guild_ids=[guild_ID], name="user_lookup", description="Lookup stats for a user")
async def userLookup(interaction: nextcord.Interaction):
    await interaction.send("Stats for (user)")
    command = 'user_lookup'
    userID = interaction.user.id
    await save(command, userID)

@bot.slash_command(guild_ids=[guild_ID], name="command_leaderboard", description="Shows leaderboard for each command usage")
async def commandLeaderboard(interaction: nextcord.Interaction):
    await interaction.send("Command Leaderboard:")
    command = 'command_leaderboard'
    userID = interaction.user.id
    await save(command, userID)

# @bot.slash_command(guild_ids=[guild_ID], name="placeholder", description="placeholder")
# async def CommandName(interaction: nextcord.Interaction):
#     await interaction.send("a response")
#     command = 'command_name'
#     userID = interaction.user.id
#     await save(command, userID)

bot.run(bot_token)