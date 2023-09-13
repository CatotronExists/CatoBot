### CATOBOT CONFIG ###
from Keys import db

version = "v0.5 | Experimental-7"
guild_ID = 739608667594162206

# Database Links
bot_stats = db["Bot_Stats"] # defines stats (Bot_Stats Collection)
user_stats = db["User_Stats"] # defines stats (User_Stats Collection)
moderation = db["Moderation"] # defines moderation (Moderation Collection)
bot_setup = db["Bot_Setup"] # defines setup (Bot_Setup Collection)