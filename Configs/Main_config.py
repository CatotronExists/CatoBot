### CATOBOT CONFIG ###
from Keys import db

version = "v0.6.d-24"
guild_ID = 739608667594162206

# Channels
level_channel = 1158919090073784452
welcome_channel = 739608668152135773
rule_channel = 739610703354265631
announcement_channel = 739609803365810176
lucky_people_channel = 1160735835218513972

# Roles
everyone_role = 739609451342069840
skill_tree_role = 1158917747569348709

# Database Links
db_bot_stats = db["BotStats"] # defines stats (BotStats Collection)
db_user_data = db["UserData"] # defines userdata (UserData Collection)