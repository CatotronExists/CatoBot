### CATOBOT ###
## Created by @Catotron // youtube.com/@catotron // for use in discord.gg/vxZnsy2 (Catotron's World)
# Modules #
import datetime
import nextcord
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

### Startup
error = False
start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("<<<------ Catobot "+ str(version)+" Terminal ------>>>")
print(CBLUE + "Current Time: "+str(start_time) + CLEAR)
print(CYELLOW + "Connecting to MongoDB..." + CLEAR)

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
    print(CBOLD + "Version: "+str(version)+"\nDev Mode = "+str(dev_mode)+"\nGuild: "+str(guild_ID) + CLEAR)
    print("\nConnecting to Discord...")

    @bot.event
    async def on_ready():
        print(CGREEN + f"-----------------------------------------\n| Logged on as {bot.user}\n| Running Version "+version+"\n-----------------------------------------" + CLEAR)
        end_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        startup_time = datetime.datetime.strptime(end_time,'%d-%m-%Y %H:%M:%S') - datetime.datetime.strptime(start_time,'%d-%m-%Y %H:%M:%S')
        print("Time Taken: "+str(startup_time))
    ready = True

while ready == True: pass


### Slash Commands

bot.run(bot_token)