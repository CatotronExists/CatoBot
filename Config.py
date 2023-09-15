### CATOBOT CONFIG ###
from Keys import db

version = "v0.5 | Experimental-8"
guild_ID = 739608667594162206

# Database Links
bot_stats = db["Bot_Stats"] # defines stats (Bot_Stats Collection)
#bot_stats = db["BotStats"] # defines stats (BotStats Collection)
user_data = db["UserData"] # defines userdata (UserData Collection)
moderation = db["Moderation"] # defines moderation (Moderation Collection)
bot_setup = db["Bot_Setup"] # defines setup (Bot_Setup Collection)