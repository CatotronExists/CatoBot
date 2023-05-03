from Modules import *
from Content_Notifications import getlatestvideo
from Config import * 


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    global start_time
    print(print(f'------------------------------\n| Logged on as CatoBot#1701\n| Running Version '+version+'\n------------------------------'))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
        start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    except Exception as e:
        print(e)

@bot.tree.command(name='test', description='Test Command') 
async def test_command(interaction: discord.Interaction):
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("test")
    
@bot.tree.command(name='bot_info', description='Basic Bot Info') 
async def botinfo_command(interaction: discord.Interaction): 
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("Current Version: "+version+"\n\nCatoBot - Made by Catotron #6333")

@bot.tree.command(name='shutdown', description='Shutdown the bot')
async def shutdown_command(interaction: discord.Interaction): 
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("Shutting down")
    await bot.close()

@bot.tree.command(name='bot_stats', description='Shows stats of the bot')
async def bot_stats_command(interaction: discord.Interaction): 
    global commands_used, start_time, current_time, uptime
    commands_used += 1
    current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    uptime = (datetime.datetime.strptime(current_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
    await interaction.response.send_message("Total Commands Used: "+str(commands_used)+"\nBot Uptime: "+str(uptime)+" // Online Since: "+str(start_time)+" AEST")

@bot.tree.command(name='socials', description="Catotron's Socials") 
async def socials_command(interaction: discord.Interaction): 
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("Youtube: <https://youtube.com/@catotron>\nTwitch: <https://twitch.tv/catotronlive>\nTiktok: <https://tiktok.com/@catotronshorts> \nTwitter: <https://twitter.com/nortotaC>")

@bot.tree.command(name='latest_video', description='Shows Latest Video')
async def lastest_video_command(interaction: discord.Interaction):
    global commands_used 
    commands_used += 1
    getlatestvideo()
    
    await interaction.response.send_message("Catotron's Last video was: x\nPosted on: (date)")

@bot.tree.command(name='latest_short', description='Shows Latest Short')
async def lastest_short_command(interaction: discord.Interaction):
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("Catotron's Last short was: x\nPosted on (date)")

@bot.command() # 'Classic' Command
async def shutdown(ctx,arg): # arg is the second word following command // 
    if arg == 'now':
        global commands_used 
        commands_used += 1
        await ctx.send(f'Shutting Down')
        await bot.close()
    else:
        print(f'Not a vaild Command')

@bot.command() # 'Classic' Command
async def sync(ctx,arg): # arg is the second word following command // 
    if arg == 'now':
        global commands_used 
        commands_used += 1
        await ctx.send(f'Syncing Bot to Discord')
        await bot.close()
    else:
        print(f'Not a vaild Command')

bot.run(bot_token) 
