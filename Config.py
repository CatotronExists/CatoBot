### CONFIG SETTINGS ###
from Modules import *
##### Bot Setup
dev_mode = False
if dev_mode == True:
    version = "v0.4.1 BETA DEV"
if dev_mode == False:
    version = "v0.4.1 BETA"
guild_ID = 739608667594162206 

if dev_mode == True: # Testing Bot
    password = ""
    bot_token = ""
elif dev_mode == False: # Live Bot
    password = ""
    bot_token = ""
###

##### Database Link
ca = certifi.where()

if dev_mode == True: # Testing Bot
    client = pymongo.MongoClient("", tlsCAFile=ca)
    db = client["Catobot_Testing"] # defines db (database)
    bot_stats = db["Bot_Stats"] # defines stats (Bot_Stats Collection)
    user_stats = db["User_Stats"] # defines stats (User_Stats Collection)
    moderation = db["Moderation"] # defines moderation (Moderation Collection)
    bot_setup = db["Bot_Setup"] # defines setup (Bot_Setup Collection)
if dev_mode == False: # Live Bot
    client = pymongo.MongoClient("", tlsCAFile=ca)
    db = client["Catobot"] # defines db (database)
    bot_stats = db["Bot_Stats"] # defines stats (Bot_Stats Collection)
    user_stats = db["User_Stats"] # defines stats (User_Stats Collection)
    moderation = db["Moderation"] # defines moderation (Moderation Collection)
    bot_setup = db["Bot_Setup"] # defines setup (Bot_Setup Collection)
###

##### Stats
result = bot_stats.find_one({"Commands_Used": {"$exists": True}})
if result is None: # if "Commands_Used" doesn't exist -> set to 0
    commands_used = 0
else:
    commands_used = result["Commands_Used"] # Starting Value

###

##### Commands
command_list = [
                "shutdown",
                "bot_stats",
                "user_lookup",
                "command_leaderboard",
                "button_test1",
                "socials",
                "update_api",
                "latest_video",
                "latest_short",
                "social_stats",
                "moderation"
                ]
###