import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID
from Config import db_user_data

def changePage(direction):
    ### Level Requirements
    level_xp_requirements = [0, 10, 40, 80, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750]
    #                        0   1   2   3    4    5    6    7    8    9   10   11   12    13    14    15    16    17    18    19    20
        
    # get user data
    data = db_user_data.find_one({"userID": userID})
    level = data["level_stats"]["level"]
    xp = data["level_stats"]["xp"]
    skill_tree_progress = data["level_stats"]["skill_tree_progress"]
    skill_points = data["level_stats"]["skill_points"]

    # Skill Tree Calculations
    max_skill_tree_progress = 100
    next_level = level + 1
    next_level_percentage = int((xp / level_xp_requirements[next_level]) * 100)
    
    global page, main_page
    main_page = int(level / 5)

    ### Pages
    global skill_tree_pages
    skill_tree_pages = [
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              __\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|__\n=================================================== \n[ 0 ]-----[ 1 ]-----[ 2 ]-----[ 3 ]-----[ 4 ]-----[ 5 ]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              __\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|__\n=================================================== \n[ 6 ]-----[ 7 ]-----[ 8 ]-----[ 9 ]-----[1 0]-----[1 1]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              __\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|__\n=================================================== \n[1 2]-----[1 3]-----[1 4]-----[1 5]-----[1 6]-----[1 7]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend."
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

def correct(level, next_level_percentage, message):
    message = message.replace("-", "~", int((level*5)+(int(next_level_percentage)/20))) # progress bar updater, level x 5 + % to next level (in 20% increments)
    message = message.replace("_", "\_")
    message = message.replace("~", "\~")
    return message

class skill_tree_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    @nextcord.ui.button(label="Back", style=nextcord.ButtonStyle.red, custom_id="skill_tree:back")
    async def back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id: # Command user
            if page != 0: 
                message = changePage(direction="prev")
                await interaction.response.edit_message(content=message, view=self) # wont work on page 0
    
    @nextcord.ui.button(label="Reset", style=nextcord.ButtonStyle.blurple, custom_id="skill_tree:reset")
    async def reset(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id: # Command user
            if page != main_page: 
                message = changePage(direction="main")
                await interaction.response.edit_message(content=message, view=self) # wont if already on main page

    @nextcord.ui.button(label="Next", style=nextcord.ButtonStyle.green, custom_id="skill_tree:next")
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id: # Command user
            if page != 2: 
                message = changePage(direction="next")
                await interaction.response.edit_message(content=message, view=self) # wont work on last page
    
    @nextcord.ui.button(label="Buy Skills", style=nextcord.ButtonStyle.green, custom_id="skill_tree:buy")
    async def buy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id: # Command user
            message = message
            await interaction.response.edit_message(content="Buy Skills", view=skill_tree_buy_view)
    
    @nextcord.ui.button(label="Close", style=nextcord.ButtonStyle.red, custom_id="skill_tree:close")
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id: # Command user
            await interaction.response.edit_message(content="Close", view=None)

class skill_tree_buy_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction
    
    @nextcord.ui.button(label="Back", style=nextcord.ButtonStyle.red, custom_id="skill_tree_buy:back")
    async def back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id:
            await interaction.response.edit_message(content="Back", view=self)
        
    @nextcord.ui.button(label="Reset", style=nextcord.ButtonStyle.blurple, custom_id="skill_tree_buy:reset")
    async def reset(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id:
            await interaction.response.edit_message(content="Reset", view=self)
        
    @nextcord.ui.button(label="Next", style=nextcord.ButtonStyle.green, custom_id="skill_tree_buy:next")
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id:
            await interaction.response.edit_message(content="Next", view=self)
    
    @nextcord.ui.button(label="Buy", style=nextcord.ButtonStyle.green, custom_id="skill_tree_buy:buy")
    async def buy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id:
            await interaction.response.edit_message(content="Buy", view=self)
        
    # OPEN DROPDOWN WITH OPTIONS ^^^^


    @nextcord.ui.button(label="Close", style=nextcord.ButtonStyle.red, custom_id="skill_tree_buy:close")
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.interaction.user.id:
            await interaction.response.edit_message(content="Close", view=skill_tree_view)
    



    

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