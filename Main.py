from Modules import *
#from Content_Notifications import getLatestVideo, getLatestShort
from Config import * 

def updateCommandUsage(command): ### Updates how many times each command has been use
    print(command + " Command Used")

    # Update the command usage in the database
    result = bot_stats.find_one({command + "_command_usage": {"$exists": True}}) # checks if x commmand has data
    if result is not None: # yes
        current_usage = result[command + "_command_usage"] # builds query (x_command_usage)
        bot_stats.update_one(
            {command + "_command_usage": current_usage}, # find
            {"$set": {command + "_command_usage": current_usage + 1}} # set
        )
        print(command + " updated (" + str(current_usage) + " -> " + str(current_usage + 1) + ")")
    else: # no
        print("//----------------------------------------")
        print(command + " does not exist in the collection")
        data = {command + "_command_usage": 1}
        x = bot_stats.insert_one(data)
        print(command + " added to collection "+command + " updated (0 -> 1)")
        print("----------------------------------------//")

def updateCommandsUsed(): ### Total Commands used
    global commands_used, x
    commands_used += 1
    
    check = commands_used - 1 # -1 as the value is increased by 1
    if check <0: # anytime the count is reset the value is pushed to 0  
        check = 0
    result = bot_stats.find_one({"Commands_Used": check}) #  checking if the previous value is saved

    if result is not None:
        bot_stats.update_one(
            {"Commands_Used": check}, 
            {"$set": {"Commands_Used": commands_used}}
        )
        print("Commands_Used updated ("+str(check)+" -> "+str(commands_used)+")\n")
    else:
        print("Commands_Used does not exist in the collection")
        data = {"Commands_Used": commands_used }
        x = bot_stats.insert_one(data) # gets stats collection -> inserts 'data'
        print("Commands_Used added to collection\n")

def updateMessagesSent(userID): # Updates messages sent per user
    result = user_stats.find_one({str(userID) + "_messages_sent": {"$exists": True}}) # checks if user has sent a message before
    if result is not None: # yes
        current = result[str(userID) + "_messages_sent"] # builds query (x_messages_sent)
        user_stats.update_one(
            {str(userID) + "_messages_sent": current}, # find
            {"$set": {str(userID) + "_messages_sent": current + 1}} # set
        )
        print(str(userID)+ " messages_sent updated (" + str(current) + " -> " + str(current + 1) + ")")
    else: # no
        print("//----------------------------------------")
        print(str(userID) + " does not exist in the collection [_messages_sent]")
        data = {str(userID) + "_messages_sent": 1}
        x = user_stats.insert_one(data)
        print(str(userID) + " added to collection"+str(userID)+" updated (0 -> 1)")
        print("----------------------------------------//")

def updateCommandsSent(userID): # Updates commands sent per user
    result = user_stats.find_one({str(userID) + "_commands_sent": {"$exists": True}}) # checks if user has sent a command before
    if result is not None: # yes
        current = result[str(userID) + "_commands_sent"] # builds query (x_commands_sent)
        user_stats.update_one(
            {str(userID) + "_commands_sent": current}, # find
            {"$set": {str(userID) + "_commands_sent": current + 1}} # set
        )
        print(str(userID)+ " commands_sent updated (" + str(current) + " -> " + str(current + 1) + ")")
    else: # no
        print("//----------------------------------------")
        print(str(userID) + " does not exist in the collection [_commands_sent]")
        data = {str(userID) + "_commands_sent": 1}
        x = user_stats.insert_one(data)
        print(str(userID) + " added to collection"+str(userID)+" updated (0 -> 1)")
        print("----------------------------------------//")

def getUserJoinDate(userID): # Gets join date for user
    result = user_stats.find_one({str(userID) + "_join_date": {"$exists": True}}) # checks if user has data
    global joined_at
    if result is not None: # yes
        joined_at = result[str(userID) + "_join_date"] # extracts data
    else: # no
        joined_at = "USER NOT FOUND | Contact Catotron#6333"
        print("//----------------------------------------")
        print(str(userID) + " does not exist in the collection [_join_date]")
        print("----------------------------------------//")

def getUserMessagesSent(userID): # Gets messages sent for user
    result = user_stats.find_one({str(userID) + "_messages_sent": {"$exists": True}}) # checks if user has data
    global messages_sent
    if result is not None: # yes
        messages_sent = result[str(userID) + "_messages_sent"] # extracts data
    else: # no
        messages_sent = "USER NOT FOUND | Contact Catotron#6333"
        print("//----------------------------------------")
        print(str(userID) + " does not exist in the collection [_messages_sent]")
        print("----------------------------------------//")

def getUserCommandsSent(userID): # Gets commands sent for user
    result = user_stats.find_one({str(userID) + "_commands_sent": {"$exists": True}}) # checks if user has data
    global commands_sent
    if result is not None: # yes
        commands_sent = result[str(userID) + "_commands_sent"] # extracts data
    else: # no
        commands_sent = "USER NOT FOUND | Contact Catotron#6333"
        print("//----------------------------------------")
        print(str(userID) + " does not exist in the collection [_commands_sent]")
        print("----------------------------------------//")

def getCommandUsage(): # Gets usage for all commands
    global command_list, leaderboard_data
    query = bot_stats.find_one({"Commands_Used": {"$exists": True}})
    leaderboard_data = ["Total Commands Sent: "+str(query["Commands_Used"])]
    for i in sorted(command_list, key=lambda x: bot_stats.find_one({x + "_command_usage": {"$exists": True}})[x + "_command_usage"], reverse=True):
        result = bot_stats.find_one({i + "_command_usage": {"$exists": True}})
        leaderboard_data.append(i.capitalize() + " Used "+(str((result[i + "_command_usage"])))+" times")

def saveJoinDate(userID,joined_at): # Saves date and time a user joined
    result = user_stats.find_one({str(userID) + "_join_date": {"$exists": True}}) # checks if user has data
    if result is not None: # yes
        print("This user ("+str(userID)+") already has joined before\nfirst joined: "+str(joined_at)+" UTC\n")
    else: # no
        data = {str(userID) + "_join_date": joined_at}
        print("//----------------------------------------")
        print(str(userID) + " does not exist in the collection")
        x = user_stats.insert_one(data)
        print(str(userID) + " added to collection, Joined: "+str(joined_at)+" UTC")
        print("----------------------------------------//")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    global start_time
    print(print(f'------------------------------\n| Logged on as CatoBot#1701\n| Running Version '+version+'\n------------------------------'))
    try: # Wait for bot to connect         
        try: # Send a ping to confirm a successful connection
            client.admin.command('ping')
            print("Successfully connected to MongoDB")
        except Exception as e:
            print(e)

        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)\nBot Ready\n------------------------------\n")
        start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    except Exception as e:
        print(e)

# Slash Commands
    
@bot.tree.command(name='shutdown', description='Shutdown the bot')
@commands.guild_only()
async def shutdown_command(interaction: discord.Interaction): 
    command = 'shutdown'
    updateCommandUsage(command)
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    try:
        await interaction.response.send_message("Shutting down")
        await bot.close()
    except discord.errors.NotFound:
        print("Interaction not found or expired")

@bot.tree.command(name='bot_stats', description='Shows stats of the bot')
@commands.guild_only()
async def bot_stats_command(interaction: discord.Interaction): 
    global commands_used, start_time, current_time, uptime
    command = 'bot_stats'
    updateCommandUsage(command)
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    uptime = datetime.datetime.strptime(current_time,'%d-%m-%Y %H:%M:%S') - datetime.datetime.strptime(start_time,'%d-%m-%Y %H:%M:%S')
    try:
        await interaction.response.send_message("Current Version: "+str(version)+"\nTotal Commands Used: "+str(commands_used)+"\nBot Uptime: "+str(uptime)+" // Online Since: "+str(start_time)+" AEST\n-------------------------------\nCatoBot - Made by Catotron#6333")
    except discord.errors.NotFound:
        print("Interaction not found or expired")

@bot.tree.command(name='user_lookup', description='Look at stats for a user')
@commands.guild_only()
async def test_command(interaction: discord.Interaction, user: discord.User = None):
    global joined_at, messages_sent, commands_sent
    command = 'user_lookup'
    updateCommandUsage(command)
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    if user is None: # if no user is selected, chooses author
        user = interaction.user
    userID = user.id # converts Username to ID
    getUserJoinDate(userID)
    getUserMessagesSent(userID)
    getUserCommandsSent(userID)
    try:
        await interaction.response.send_message("Information for "+str(user)+" | UserID: ("+str(userID)+")\nJoin Date: "+str(joined_at)+" UTC\nMessages Sent: "+str(messages_sent)+"\nCommands Sent: "+str(commands_sent))
    except discord.errors.NotFound:
        print("Interaction not found or expired")

@bot.tree.command(name='command_leaderboard', description='Displays leaderboard for top commands')
@commands.guild_only()
async def shutdown_command(interaction: discord.Interaction): 
    command = 'command_leaderboard'
    updateCommandUsage(command)
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    getCommandUsage()
    try: 
        await interaction.response.send_message("Command Leaderboard\n"+'\n'.join(leaderboard_data))
    except discord.errors.NotFound:
        print("Interaction not found or expired")
###

# Button Commands 

class Button_test1(discord.ui.View):
    @discord.ui.button(label="Button",style=discord.ButtonStyle.gray)
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.response.send_message("This is a button response!")

@bot.tree.command(name='button_test1', description='Testing Buttons') # Create a slash command
@commands.guild_only()
async def button(interaction: discord.Interaction):
    command = 'button_test1'
    updateCommandUsage(command) 
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    try:
        await interaction.response.send_message("This is a button!", view=Button_test1()) # Send a message with our View class that contains the button
    except discord.errors.NotFound:
        print("Interaction not found or expired")

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
@commands.guild_only()
async def socials_command(interaction: discord.Interaction):
    command = 'socials'
    updateCommandUsage(command)  
    updateCommandsUsed() 
    userID = interaction.user.id
    updateCommandsSent(userID)
    social_buttons = Social_Buttons()
    social_buttons.add_item(social_buttons.youtube_button)
    social_buttons.add_item(social_buttons.twitch_button)
    social_buttons.add_item(social_buttons.tiktok_button)
    social_buttons.add_item(social_buttons.twitter_button)
    try:
        await interaction.response.send_message("Youtube: <https://youtube.com/@catotron>\nTwitch: <https://twitch.tv/catotronlive>\nTiktok: <https://tiktok.com/@catotronshorts> \nTwitter: <https://twitter.com/nortotaC>",view=social_buttons)
    except discord.errors.NotFound:
        print("Interaction not found or expired")
###

### Soon - (Content Creation)

@bot.tree.command(name='update_api', description='Refreshes API data')
@commands.guild_only()
async def lastest_short_command(interaction: discord.Interaction):
    command = 'update_api'
    updateCommandUsage(command)
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    try:
        await interaction.response.send_message("Refreshing API data")
    except discord.errors.NotFound:
        print("Interaction not found or expired")

@bot.tree.command(name='latest_video', description='Shows Latest Video')
@commands.guild_only()
async def lastest_video_command(interaction: discord.Interaction):
    command = 'latest_video'
    updateCommandUsage(command)
    updateCommandsUsed()
    #getLatestVideo()
    userID = interaction.user.id
    updateCommandsSent(userID)
    try:
        await interaction.response.send_message("Catotron's Last video was: x\nPosted on: (date)")
    except discord.errors.NotFound:
        print("Interaction not found or expired")

@bot.tree.command(name='latest_short', description='Shows Latest Short')
@commands.guild_only()
async def lastest_short_command(interaction: discord.Interaction):
    command = 'latest_short'
    updateCommandUsage(command)
    updateCommandsUsed()
    #getLatestShort()
    userID = interaction.user.id
    updateCommandsSent(userID)
    try:
        await interaction.response.send_message("Catotron's Last short was: x\nPosted on (date)")
    except discord.errors.NotFound:
        print("Interaction not found or expired")

@bot.tree.command(name='social_stats', description='Shows Stats from socials')
@commands.guild_only()
async def lastest_short_command(interaction: discord.Interaction):
    command = 'social_stats'
    updateCommandUsage(command)
    updateCommandsUsed()
    userID = interaction.user.id
    updateCommandsSent(userID)
    try:
        await interaction.response.send_message("Youtube: x Subscribers // Uploads: // Views:  \nTwitch: x Followers // Subscribers: \n TikTok: x Followers // Likes: \n Twitter: x Followers // Tweets: \n Last Updated: [Will update every 12 hours]")
    except discord.errors.NotFound:
        print("Interaction not found or expired")
###    

# Moderation - (Soon)

class Moderation_Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.warn_button = discord.ui.Button(
            label="Warn",
            style=discord.ButtonStyle.blurple
        )

        self.mute_button = discord.ui.Button(
            label="Mute",
            style=discord.ButtonStyle.blurple
        )

        self.kick_button = discord.ui.Button(
            label="Kick",
            style=discord.ButtonStyle.blurple
        )

        self.ban_button = discord.ui.Button(
            label="Ban",
            style=discord.ButtonStyle.blurple    
        )

        self.close_button = discord.ui.Button(
            label="Close",
            style=discord.ButtonStyle.red
        )

class BanReason(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",description="This is option 1!"),
            discord.SelectOption(label="Option 2",description="This is option 2!"),
            discord.SelectOption(label="Option 3",description="This is option 3!")
            ]
        super().__init__(placeholder="Select a Ban Reason",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Option 1":
            await interaction.response.send_message("Option 1")
        elif self.values[0] == "Option 2":
            await interaction.response.send_message("Option 2")
        elif self.values[0] == "Option 3":
            await interaction.response.send_message("Option 3")

@bot.tree.command(name='moderation', description="Opens Moderation Menu") 
@commands.guild_only()
async def moderation_command(interaction: discord.Interaction): 
    command = 'moderation'
    updateCommandUsage(command)
    updateCommandsUsed() 
    userID = interaction.user.id
    updateCommandsSent(userID)
    moderation_buttons = Moderation_Buttons()
    moderation_buttons.add_item(moderation_buttons.warn_button)
    moderation_buttons.add_item(moderation_buttons.mute_button)
    moderation_buttons.add_item(moderation_buttons.kick_button)
    moderation_buttons.add_item(moderation_buttons.ban_button)
    moderation_buttons.add_item(moderation_buttons.close_button)
    try:
        await interaction.response.send_message("Actions for (user)\n--------------------------------\nCurrent Warns:\nTimes Muted:\nTimes Kicked:\nTimes Banned:\n--------------------------------",view=moderation_buttons)
        await bot.wait_for('button_click', check=lambda i: i.component.label.startswith('Select Reason',view=BanReason()))
        #await interaction.response.send_message("Select Reason",view=BanReason())
    except discord.errors.NotFound:
        print("Interaction not found or expired")
###

# Passive Commands

@bot.event
async def on_member_join(member): # when a member joins
    userID = member.id
    print("Member Joined: "+str(member)+" | ID: "+str(userID)+"")
    channel = bot.get_channel(739608668152135773) # #welcome
    joined_at = member.joined_at.strftime("%d-%m-%Y %H:%M:%S")
    saveJoinDate(userID, joined_at)
    await channel.send("Welcome to Catotron's World, <@"+str(userID)+">!")

@bot.event
async def on_message(message): # waits for message
    if message.author.bot: # ignores itself (bot)
        pass
    else: # user message
        userID = message.author.id
        updateMessagesSent(userID)
###

bot.run(bot_token) 