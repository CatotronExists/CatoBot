### CATOBOT ###
## Created by @Catotron // youtube.com/@catotron // for use in discord.gg/vxZnsy2 (Catotron's World)
# Modules #
import datetime
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from Configs.Main_config import *
from Configs.ST_config import lowerXP_gain, upperXP_gain, level_xp_requirements, max_level, skills
from Keys import bot_token, client, dev_mode
import pymongo
import random
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

# Vars #
extension_command_list = ["bot_stats", "user_lookup", "command_leaderboard", "skill_tree", "help", "moderation"]
full_command_list = ["shutdown", "reload", "bot_stats", "user_lookup", "command_leaderboard", "skill_tree", "help", "moderation"]
#      #

### Discord Setup
intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

### Terminal Functions
def formatOutput(output, status):
    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f')[:-3]
    if status == "Normal": print("| "+str(current_time)+" || "+output)
    elif status == "Good": print(CGREEN +"| "+str(current_time)+" || "+output+ CLEAR)
    elif status == "Error": print(CRED +"| "+str(current_time)+" || "+output+ CLEAR)
    elif status == "Warning": print(CYELLOW +"| "+str(current_time)+" || "+output+ CLEAR)

### Save Functions
async def saveData(command, userID, Type):
    updateCommandUsage(command)
    updateUserData(userID, Type)

def updateCommandUsage(command):
    try: # Command Usage
        db_bot_stats.find_one_and_update({"Commands_Used": {"$exists": True}}, {"$inc": {"Commands_Used": + 1, command+"_usage": + 1}}) # +1 to Commands Used, then also +1 to the command used
        formatOutput(output="    Command Usage Successfully Saved", status="Good")

    except Exception as e: 
        formatOutput(output="    Error occured while saving Command Usage // Error: "+str(e), status="Error")

def updateUserData(userID, Type):
    try: # User Data
        db_user_data.find_one_and_update({"userID": userID}, {"$inc": {Type.lower()+"s_sent": + 1}}) # +1 to {type}_sent

    except Exception as e: 
        formatOutput(output="    Error occured while saving "+Type+" // Error: "+str(e), status="Error")

def fetchUserData(searched_user_id):
    try:
        formatOutput(output="    Finding Data for "+str(searched_user_id), status="Normal")
        data = db_user_data.find_one({"userID": searched_user_id})
        formatOutput(output="    Data Found", status="Good")

    except Exception as e: 
        formatOutput(output="    Error Encountered when finding data // Error: "+str(e), status="Error")
        data = "Error Encountered when finding data!"

    finally: return data

async def updateXP(userID, Type, message):
    data = db_user_data.find_one({"userID": userID})
    level = data["level_stats"]["level"]
    xp = data["level_stats"]["xp"]
    skill_points = data["level_stats"]["skill_points"]
    xp_multi = data["level_stats"]["xp_multi"]

    # XP Calculation
    win = False
    if Type == "Message":  # gain xp on message & roll chance for pack
        channel = bot.get_channel(lucky_people_channel)
        xp_gain = random.randint(lowerXP_gain, upperXP_gain)
        roll = random.randint(1, 100) # 1 in 100 chance of a pack
        if roll == 1:
            roll = random.randint(1, 100)
            if roll == 1: xp_gain += 3000; win = "Massive" # massive, 1/100 chance
            elif roll <= 5: xp_gain += 1000; win = "Medium" # medium, 5/100 chance
            elif roll <= 30: xp_gain += 500; win = "Small" # small, 30/100 chance
            elif roll <= 100: xp_gain += 100; win = "Tiny" # tiny, 70/100 chance

    elif Type == "Pack_tiny": xp_gain = 100 # tiny pack
    elif Type == "Pack_small": xp_gain = 500 # small pack
    elif Type == "Pack_medium": xp_gain = 1000 # medium pack
    elif Type == "Pack_massive": xp_gain = 3000 # massive pack

    xp = float(round(xp + (xp_gain * (1 + xp_multi)), 2))
    xp_str = str(xp)
    if xp_str[:-2] == ".0": # Remove .0
        xp_str = xp_str[:-2]
    xp = float(xp_str)
    xp = int(xp)

    if win != False: await channel.send(f"<@{userID}> Recieved a {win} pack of XP! Containing {xp_gain}XP")

    if level <= max_level: # level while not max
        try:
            while xp >= level_xp_requirements[level+1]: # level up
                xp = xp - level_xp_requirements[level+1]
                level += 1
                skill_points += 1
                formatOutput(output="Level Up! "+str(userID)+" is now level "+str(level), status="Normal")
                channel = bot.get_channel(level_channel)
                await channel.send("Level Up! <@"+str(userID)+"> is now level "+str(level))
        except Exception as e: pass # if a user hits max levvel with lots of overflow xp, this will stop it from looping
    else: pass

    db_user_data.find_one_and_update(
        {"userID": userID},
        {"$set": {
                "level_stats.level": level,
                "level_stats.xp": xp,
                "level_stats.skill_points": skill_points
    }})

### Startup
startup_start_time = datetime.datetime.now().strftime('%M:%S.%f')[:-3]
start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("<<<------ Catobot "+str(version)+" Terminal ------>>>")
print(CBLUE +"Current Time: "+str(start_time)+ CLEAR)
print(CYELLOW +"Connecting to MongoDB..."+ CLEAR)

try: # Ping MongoDB
    client.admin.command('ping')
    print(CGREEN + "    Successfully connected to MongoDB" + CLEAR)
    error = False
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
    for i in extension_command_list:
        try: 
            bot.load_extension("Commands."+i)
            formatOutput(output="    /"+i+" Successfully Loaded", status="Good")
        except Exception as e: 
            formatOutput(output="    /"+i+" Failed to Load // Error: "+str(e), status="Warning")
    @bot.event
    async def on_ready():
        startup_end_time = datetime.datetime.now().strftime('%M:%S.%f')[:-3]
        startup_time_delta = datetime.datetime.strptime(startup_end_time,'%M:%S.%f') - datetime.datetime.strptime(startup_start_time,'%M:%S.%f')
        startup_time_ms = int((startup_time_delta.total_seconds())*1000)
        startup_time_sec = float(startup_time_ms/1000)
        print(CGREEN + f"-----------------------------------------------\n| Logged on as {bot.user}\n| Running Version "+version+"\n| Time Taken: "+str(startup_time_ms)+" ms ("+str(startup_time_sec)+"s)\n-----------------------------------------------"+ CLEAR)

### Core Commands
# Shutdown
@bot.slash_command(guild_ids=[guild_ID], name="shutdown", description="Turns off the bot")
async def shutdown(interaction: nextcord.Interaction):
    command = 'shutdown'
    userID = interaction.user.id
    formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

    if interaction.user.guild_permissions.administrator == True: # is Admin
        await interaction.send("Shutting Down")
        await saveData(command, userID, Type="Command")
        try: 
            formatOutput(output="    Shutting Down Bot", status="Good")
            await bot.close()
        except Exception as e: formatOutput(output="    Shutdown Failed // Error: "+str(e), status="Error")

    else: # not Admin
        await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions", ephemeral=True)
        await saveData(command, userID, Type="Command")
        formatOutput(output="    Insufficient Permissions for "+str(userID), status="Warning")

# Reload
@bot.slash_command(guild_ids=[guild_ID], name="reload", description="Reload Bot Commands")
async def CommandName(interaction: nextcord.Interaction):
    command = 'reload'
    userID = interaction.user.id
    formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

    if interaction.user.guild_permissions.administrator == True: # is Admin
        await interaction.response.defer(with_message=True)

        formatOutput(output="Refreshing Commands", status="Normal")
        for i in extension_command_list:
            try:
                bot.reload_extension("Commands."+i)
                formatOutput(output="    /"+i+" Successfully Refreshed", status="Good")
            except Exception as e:
                formatOutput(output="    /"+i+" Failed to Reload // Error: "+str(e), status="Warning")

        await interaction.send("Commands Reloaded")
        await saveData(command, userID, Type="Command")

    else: # not Admin
        await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions", ephemeral=True)
        await saveData(command, userID, Type="Command")
        formatOutput(output="    Insufficient Permissions for "+str(userID), status="Warning")

### Passive Commands
# Member Join
@bot.event
async def on_member_join(member: nextcord.Member):
    userID = member.id
    channel = bot.get_channel(welcome_channel)
    await channel.send("Welcome to Catotron's World, <@"+str(userID)+"> !")
    formatOutput(output="Member Joined: "+str(member)+" | ID: "+str(userID), status="Normal")
    formatOutput(output="    Checking for existing user profile...", status="Normal")

    try: # check for existing profile
        data = db_user_data.find_one({"userID": userID})
        if data is not None: 
            try: # update join date
                formatOutput(output="    User already has a profile! Updating join_date!", status="Warning")
                db_user_data.find_one_and_update(
                    {"userID": userID},
                    {"$set": {"join_date": member.joined_at.strftime("%d-%m-%Y %H:%M:%S")}}
                )
                formatOutput(output="    Successful Update of join_date for "+str(userID), status="Good")
            except Exception as e: formatOutput(output="    Failed to Update join_date for "+str(userID)+" // Error: "+str(e), status="Error")

            try: # Give Roles
                formatOutput(output="    Giving Roles to "+str(userID), status="Normal")

                ## Basic Roles
                role = bot.get_guild(guild_ID).get_role(everyone_role) 
                await member.add_roles(role)
                role = bot.get_guild(guild_ID).get_role(skill_tree_role)
                await member.add_roles(role)

                for i in data["level_stats"]["purchased_nodes"]:
                    if i == 0: pass # skip placholder index
                    else:
                        print(i)
                        roleID = skills[int(str(i).split(".")[0])][float(str(i).split(".")[1])]["roleID"]
                        if roleID != "n/a": pass # skip if no role
                        else: # give role
                            role = bot.get_guild(guild_ID).get_role(roleID)
                            await member.add_roles(role)

                formatOutput(output="    Successfully gave Roles to "+str(userID), status="Good")
            except Exception as e: formatOutput(output="    Failed to Give Roles to "+str(userID)+" // Error: "+str(e), status="Error")

        else: # Create user profile
            try:
                join_date = member.joined_at.strftime("%d-%m-%Y %H:%M:%S")
                db_user_data.insert_one(
                    {"userID": userID,
                    "join_date": join_date,
                    "messages_sent": 0,
                    "commands_sent": 0,
                    "level_stats": {
                        "level": 0,
                        "xp": 0,
                        "skill_tree_progress": 0,
                        "skill_points": 0,
                        "purchased_nodes": [0],
                        "xp_multi": 0
                        }
                    }
                )

                formatOutput(output="    Successful Creation of user profile for "+str(userID), status="Good")
            except Exception as e: formatOutput(output="    Failed to Create user profile // Error: "+str(e), status="Error")
    except Exception as e: formatOutput(output="    Failed to Check for user profile // Error: "+str(e), status="Error")

# on message
@bot.event
async def on_message(message: nextcord.message): # waits for message
    try:
        if message.author.bot: # ignores itself (bot)
            pass
        else: # user message
            userID = message.author.id
            updateUserData(userID, Type="Message")
            await updateXP(userID, Type="Message", message=message)
    except Exception as e: formatOutput(output="    Failed to save message from "+str(userID)+" // Error: "+str(e), status="Warning")

bot.run(bot_token)