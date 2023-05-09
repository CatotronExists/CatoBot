from Modules import *
from Content_Notifications import getlatestvideo, getlatestshort
from Config import * 

intents = discord.Intents.all()
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

# Slash Commands
@bot.tree.command(name='test', description='Test Command') 
async def test_command(interaction: discord.Interaction):
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("test")
    
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
    await interaction.response.send_message("Current Version: "+version+"\nTotal Commands Used: "+str(commands_used)+"\nBot Uptime: "+str(uptime)+" // Online Since: "+str(start_time)+" AEST\n-------------------------------\nCatoBot - Made by Catotron #6333")

# Button Commands 

class Button_test1(discord.ui.View):
    @discord.ui.button(label="Button",style=discord.ButtonStyle.gray)
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.response.send_message("This is a button response!")

@bot.tree.command(name='button_test1', description='Testing Buttons') # Create a slash command
async def button(interaction: discord.Interaction): 
    await interaction.response.send_message("This is a button!", view=Button_test1()) # Send a message with our View class that contains the button

class Social_Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.youtube_button = discord.ui.Button(
            label="Youtube",
            style=discord.ButtonStyle.link,
            url="https://youtube.com/@catotron"
        )

        self.twitch_button = discord.ui.Button(
            label="Twitch",
            style=discord.ButtonStyle.link,
            url="https://twitch.tv/catotronlive"
        )

        self.tiktok_button = discord.ui.Button(
            label="Tiktok",
            style=discord.ButtonStyle.link,
            url="https://tiktok.com/@catotronshorts"
        )

        self.twitter_button = discord.ui.Button(
            label="Twitter",
            style=discord.ButtonStyle.link,
            url="https://twitter.com/nortotaC"
        )

@bot.tree.command(name='socials', description="Catotron's Socials") 
async def socials_command(interaction: discord.Interaction): 
    global commands_used 
    commands_used += 1 
    social_buttons = Social_Buttons()
    social_buttons.add_item(social_buttons.youtube_button)
    social_buttons.add_item(social_buttons.twitch_button)
    social_buttons.add_item(social_buttons.tiktok_button)
    social_buttons.add_item(social_buttons.twitter_button)
    await interaction.response.send_message("Youtube: <https://youtube.com/@catotron>\nTwitch: <https://twitch.tv/catotronlive>\nTiktok: <https://tiktok.com/@catotronshorts> \nTwitter: <https://twitter.com/nortotaC>",view=social_buttons)

### Soon - (Content Creation)
@bot.tree.command(name='update_api', description='Refreshes API data')
async def lastest_short_command(interaction: discord.Interaction):
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("Refreshing API data")

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

@bot.tree.command(name='social_stats', description='Shows Stats from socials')
async def lastest_short_command(interaction: discord.Interaction):
    global commands_used 
    commands_used += 1
    await interaction.response.send_message("Youtube: x Subscribers // Uploads: // Views:  \nTwitch: x Followers // Subscribers: \n TikTok: x Followers // Likes: \n Twitter: x Followers // Tweets: \n Last Updated: [Will update every 12 hours]")
###    

bot.run(bot_token) 