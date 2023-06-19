import datetime
import nextcord
from nextcord.ext import commands
from Config import version, guild_ID
from Keys import bot_token, client, dev_mode
import pymongo

### Discord Setup
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

### Startup
start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("<<<------ Catobot Terminal ------>>>")
print("Current Time: "+str(start_time))
print("Connecting to MongoDB...")

try: # Ping MongoDB
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except Exception as e:
    print(e)

print("--------------------------")
print("Bot is starting up...")
print("Loading Bot Settings...")
print("Version: "+str(version)+"\nDev Mode = "+str(dev_mode)+"\nGuild: "+str(guild_ID))
print("\nConnecting to Discord...")

@bot.event
async def on_ready():
    print(f"-----------------------------------------\n| Logged on as {bot.user}\n| Running Version "+version+"\n-----------------------------------------")
    end_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    startup_time = datetime.datetime.strptime(end_time,'%d-%m-%Y %H:%M:%S') - datetime.datetime.strptime(start_time,'%d-%m-%Y %H:%M:%S')
    print("Time Taken: "+str(startup_time))

### Slash Commands

bot.run(bot_token)