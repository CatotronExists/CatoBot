### CATOBOT ###
## Created by @Catotron // youtube.com/@catotron // for use in discord.gg/vxZnsy2 (Catotron's World)
# Modules #
import datetime
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from Config import version, guild_ID, db_bot_stats, db_user_data, db_bot_setup
from Keys import bot_token, client, dev_mode, self_host
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

# Vars #
extension_command_list = ["bot_stats", "user_lookup", "command_leaderboard"]
full_command_list = ["shutdown", "reload", "bot_stats", "user_lookup", "command_leaderboard"]
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
async def save(command, userID, Type):
    updateCommandUsage(command)
    updateUserData(userID, Type)

def updateCommandUsage(command):
    try:
        data = db_bot_stats.find_one({"Commands_Used": {"$exists": True}})

        Commands_Used = data["Commands_Used"] + 1 # always + 1
        if command == "shutdown": shutdown_usage = data["shutdown_usage"] + 1
        else: shutdown_usage = data["shutdown_usage"]

        if command == "reload": reload_usage = data["reload_usage"] + 1
        else: reload_usage = data["reload_usage"]

        if command == "bot_stats": bot_stats_usage = data["bot_stats_usage"] + 1
        else: bot_stats_usage = data["bot_stats_usage"]

        if command == "user_lookup": user_lookup_usage = data["user_lookup_usage"] + 1
        else: user_lookup_usage = data["user_lookup_usage"]

        if command == "command_leaderboard": command_leaderboard_usage = data["command_leaderboard_usage"] + 1
        else: command_leaderboard_usage = data["command_leaderboard_usage"]
        
        db_bot_stats.update_one(
            {"Commands_Used": {"$exists": True}},
            {"$set": {"Commands_Used": Commands_Used,
            "shutdown_usage": shutdown_usage,
            "reload_usage": reload_usage,
            "bot_stats_usage": bot_stats_usage,
            "user_lookup_usage": user_lookup_usage,
            "command_leaderboard_usage": command_leaderboard_usage}}
        )
        formatOutput(output="    Command Usage Successfully Saved", status="Good")

    except Exception as e: formatOutput(output="    Error occured while saving // Error: "+str(e), status="Error")

def updateUserData(userID, Type): 
    data = db_user_data.find_one({"userID": userID})
    join_date = data["join_date"]

    if Type == "Message": messages_sent = data["messages_sent"] + 1
    else: messages_sent = data["messages_sent"]

    if Type == "Command": commands_sent = data["commands_sent"] + 1
    else: commands_sent = data["commands_sent"]

    db_user_data.update_one(
    {"userID": userID},
    {"$set": {"userID": userID,
    "join_date": join_date,
    "messages_sent": messages_sent,
    "commands_sent": commands_sent}}
)

def fetchUserData(user, searched_user_id):
    try:
        formatOutput(output="    Finding Data for "+str(user), status="Normal")
        data = db_user_data.find_one({"userID": searched_user_id})
        formatOutput(output="    Data Found", status="Good")
    except Exception as e: 
        formatOutput(output="    Error Encountered when finding data // Error: "+str(e), status="Error")
        data = "Error Encountered when finding data!"
    return data

def fetchBotData():
    data = db_bot_stats.find_one({"Commands_Used": {"$exists": True}})
    return data

### Startup ### DUE TO DOUBLE STARTUP, THIS WONT WORK
# if self_host == True: error = False # Hosted Locally
# else: # Using hosting Serivce
#     print("Checking for last mode")
#     result = db_bot_setup.find_one({"last_mode": {"$exists": True}})
#     if result is not None: 
#         mode = result["last_mode"]
#         print("Bot was last "+mode)

#         if mode == "ONLINE":
#             error = True
#             print("Bot was last online, Turning OFF")
#             db_bot_setup.update_one(
#                 {"last_mode": "ONLINE"}, # find
#                 {"$set": {"last_mode": "OFFLINE"}} # set
#             )   

#         elif mode == "OFFLINE": 
#             error = False
#             print("Bot was last offline, Turning ON")
#             db_bot_setup.update_one(
#                 {"last_mode": "OFFLINE"}, # find
#                 {"$set": {"last_mode": "ONLINE"}} # set
#             )   
    
#     else: 
#         print("Could not find last status...Setting to ONLINE")
#         error = False
#         db_bot_setup.insert_one(
#             {"last_mode": "ONLINE"}
#         )

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

if error == True: error == True # END if no connection 
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
        await save(command, userID, Type="Command")
        try: 
            formatOutput(output="    Shutting Down Bot", status="Good")
            await bot.close()
        except Exception as e: formatOutput(output="    Shutdown Failed // Error: "+str(e), status="Error")

    else: # not Admin
        await interaction.send("Insufficient Permissions\nMissing Administrator Permissions")
        await save(command, userID, Type="Command")
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
        await save(command, userID, Type="Command")

    else: # not Admin
        await interaction.send("Insufficient Permissions\nMissing Administrator Permissions")
        await save(command, userID, Type="Command")
        formatOutput(output="    Insufficient Permissions for "+str(userID), status="Warning")

### Passive Commands 
# Member Join
@bot.event
async def on_member_join(member: nextcord.Member):
    userID = member.id
    channel = bot.get_channel(739608668152135773)
    await channel.send("Welcome to Catotron's World, <@"+str(userID)+"> !")
    formatOutput(output="Member Joined: "+str(member)+" | ID: "+str(userID), status="Normal")
    formatOutput(output="    Checking for existing user profile...", status="Normal")

    try: # check for existing profile
        data = db_user_data.find_one({"userID": userID})
        if data is not None: formatOutput(output="    User already has a profile!", status="Warning")
            
        else: # Create user profile
            try: 
                join_date = member.joined_at.strftime("%d-%m-%Y %H:%M:%S")
                db_user_data.insert_one(
                {"userID": userID,
                "join_date": join_date,
                "messages_sent": 0,
                "commands_sent": 0})
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
    except Exception as e: formatOutput(output="    Failed to save message from "+str(userID)+" // Error: "+str(e), status="Warning")
        
bot.run(bot_token)