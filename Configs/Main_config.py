### CATOBOT CONFIG ###
from Keys import db

version = "v0.6.d-19"
guild_ID = 739608667594162206

# Channels
level_channel = 1158919090073784452
welcome_channel = 739608668152135773
rule_channel = 739610703354265631
announcement_channel = 739609803365810176

# Database Links
db_bot_stats = db["BotStats"] # defines stats (BotStats Collection)
db_user_data = db["UserData"] # defines userdata (UserData Collection)
db_bot_setup = db["BotSetup"] # defines setup (BotSetup Collection)