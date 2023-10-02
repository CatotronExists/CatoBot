import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID
from Config import db_user_data

def updateSkillData(userID, skill_purchased):
    formatOutput(output="Skill ["+str(skill_purchased)+"] Purchased by ("+str(userID)+")", status="Normal")

    data = db_user_data.find_one({"userID": userID})
    join_date = data["join_date"]
    messages_sent = data["messages_sent"]
    commands_sent = data["commands_sent"]
    level = data["level_stats"]["level"]
    xp = data["level_stats"]["xp"]
    skill_tree_progress = data["level_stats"]["skill_tree_progress"]
    skill_points = data["level_stats"]["skill_points"] - 1
    purchased_nodes = data["level_stats"]["purchased_nodes"]
    purchased_nodes.append(skill_purchased)
    purchased_nodes.sort()

    db_user_data.update_one(
        {"userID": userID},
        {"$set": {
            "userID": userID,
            "join_date": join_date,
            "messages_sent": messages_sent,
            "commands_sent": commands_sent,                    
            "level_stats": {
                "level": level,
                "xp": xp,
                "skill_tree_progress": skill_tree_progress,
                "skill_points": skill_points,
                "purchased_nodes": purchased_nodes
            }
        }}
    )
    formatOutput(output="    Saved Purchase of ["+str(skill_purchased)+"] by ("+str(userID)+")", status="Good")

def changePage(direction):
    ### Level Requirements
    level_xp_requirements = [0, 10, 40, 80, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750]
    #                        0   1   2   3    4    5    6    7    8    9   10   11   12    13    14    15    16    17    18    19    20
        
    # get user data
    global skill_points, purchased_nodes
    data = db_user_data.find_one({"userID": userID})
    level = data["level_stats"]["level"]
    xp = data["level_stats"]["xp"]
    skill_tree_progress = data["level_stats"]["skill_tree_progress"]
    skill_points = data["level_stats"]["skill_points"]
    purchased_nodes = data["level_stats"]["purchased_nodes"]

    # Skill Tree Calculations
    max_skill_tree_progress = 100
    next_level = level + 1
    next_level_percentage = int((xp / level_xp_requirements[next_level]) * 100)
    
    global page, main_page
    main_page = int(level / 5)

    ### Pages
    global skill_tree_pages
    skill_tree_pages = [
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              _________\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|_________\n=================================================== \n[ 0 ]-----[ 1 ]-----[ 2 ]-----[ 3 ]-----[ 4 ]-----[ 5 ]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              _________\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|_________\n=================================================== \n[ 6 ]-----[ 7 ]-----[ 8 ]-----[ 9 ]-----[1 0]-----[1 1]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              _________\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|_________\n=================================================== \n[1 2]-----[1 3]-----[1 4]-----[1 5]-----[1 6]-----[1 7]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend."
    ]

    if direction == "main":
        page = main_page
        return correct(level, next_level_percentage, message=skill_tree_pages[page])

    elif direction == "next":
        page += 1
        return correct(level, next_level_percentage, message=skill_tree_pages[page])
    
    elif direction == "prev":
        page -= 1
        return correct(level, next_level_percentage, message=skill_tree_pages[page])

    elif direction == "none":
        return correct(level, next_level_percentage, message=skill_tree_pages[page])

def correct(level, next_level_percentage, message):
    message = message.replace("-", "~", int((level*5)+(int(next_level_percentage)/20))) # progress bar updater, level x 5 + % to next level (in 20% increments)
    message = message.replace("_", "\_")
    message = message.replace("~", "\~")
    return message

class skill_tree_view(nextcord.ui.View): # Skill Tree View
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    @nextcord.ui.button(label="Back", style=nextcord.ButtonStyle.red, custom_id="skill_tree:back")
    async def back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            if page != 0:
                message = changePage(direction="prev")
                await interaction.response.edit_message(content=message, view=self) # wont work on page 0
    
    @nextcord.ui.button(label="Reset", style=nextcord.ButtonStyle.blurple, custom_id="skill_tree:reset")
    async def reset(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            if page != main_page:
                message = changePage(direction="main")
                await interaction.response.edit_message(content=message, view=self) # wont if already on main page

    @nextcord.ui.button(label="Next", style=nextcord.ButtonStyle.green, custom_id="skill_tree:next")
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            if page != 2:
                message = changePage(direction="next")
                await interaction.response.edit_message(content=message, view=self) # wont work on last page
    
    @nextcord.ui.button(label="Buy Skills", style=nextcord.ButtonStyle.green, custom_id="skill_tree:buy")
    async def buy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            await interaction.response.edit_message(view=purchase_dropdown_view(interaction))

    @nextcord.ui.button(label="Close", style=nextcord.ButtonStyle.red, custom_id="skill_tree:close")
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            await interaction.response.edit_message(view=None)
    
class purchase_dropdown_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.add_item(purchase_dropdown())

class purchase_dropdown(nextcord.ui.Select):
    def __init__(self):
        global skills
        skills = [["Index Setter", "Reaction Perms", "Image Perms", "1.25xp Multi", "Custom Color", "Embed Perms"], ["Index Setter", "placeholder"], ["Index Setter", "placeholder"]]
        # Set No.  0                                                                                      1                     2

        options = []
        for i in skills[page]: # builds dropdown options
            i = nextcord.SelectOption(label=i, value=i)
            options.append(i)
        options.append(nextcord.SelectOption(label="Close", value="Close")) # add close to each dropdown

        super().__init__(placeholder="Select a skill to buy", min_values=1, max_values=1, options=options)
    
    async def callback(self, interaction: nextcord.Interaction):
        if interaction.user.id == userID:
            if skill_points > 0: # has skill points
                if self.values[0] != "Close": # save if chose skill
                    skill_purchased = "1."+ str(skills[page].index(self.values[0])) # get index of skill (eg. 1.1)
                    skill_purchased = float(skill_purchased)
                    updateSkillData(userID, skill_purchased=skill_purchased)
                message = changePage(direction="none")
                await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
            else: # no skill points
                message = changePage(direction="none") 
                await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
                if self.values[0] != "Close": await interaction.followup.send("You don't have any skill points to spend.", ephemeral=True)

class Command_skill_tree_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="skill_tree", description="Show skill tree")
    async def skill_tree(self, interaction: nextcord.Interaction):
        command = 'skill_tree'
        global userID, username
        userID = interaction.user.id
        username = interaction.user.name
        username = username.capitalize()

        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

        await interaction.response.defer(with_message=True)
        message = changePage(direction="main")

        await interaction.send(message, view=skill_tree_view(interaction))

        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_skill_tree_Cog(bot))