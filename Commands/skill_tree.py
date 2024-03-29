import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID, updateXP
from Configs.Main_config import db_user_data
from Configs.ST_config import skills, skill_number, level_xp_requirements, max_level

def updateSkillData(userID, skill_purchased):
    formatOutput(output="Skill ["+str(skill_purchased)+"] Purchased by ("+str(userID)+")", status="Normal")

    # Data Calculations
    try: 
        data = db_user_data.find_one({"userID": userID})
        skill_points = data["level_stats"]["skill_points"] - skills[page][skill_purchased]["cost"] #(skill_points - cost)
        purchased_nodes = data["level_stats"]["purchased_nodes"]
        purchased_nodes.append(skill_purchased)
        purchased_nodes.sort()
        skill_tree_progress = data["level_stats"]["skill_tree_progress"]
        skill_tree_progress = len(purchased_nodes) - 1

        db_user_data.find_one_and_update(
        {"userID": userID},
        {"$set": {
                "level_stats.skill_tree_progress": skill_tree_progress,
                "level_stats.skill_points": skill_points,
                "level_stats.purchased_nodes": purchased_nodes     
        }})
        formatOutput(output="    Saved Purchase of ["+str(skill_purchased)+"] by ("+str(userID)+")", status="Good")

    except Exception as e: formatOutput(output="    Failed to save Purchase of ["+str(skill_purchased)+"] by ("+str(userID)+") // Error: "+str(e), status="Error")

def changePage(direction):
    # get user data
    global skill_points, purchased_nodes
    data = db_user_data.find_one({"userID": userID})
    level = data["level_stats"]["level"]
    xp = data["level_stats"]["xp"]
    skill_tree_progress = data["level_stats"]["skill_tree_progress"]
    skill_points = data["level_stats"]["skill_points"]
    purchased_nodes = data["level_stats"]["purchased_nodes"]

    # Skill Tree Calculations
    max_skill_tree_progress = skill_number
    global page, main_page

    if level != max_level: 
        next_level = level + 1
        next_level_percentage = int((xp / level_xp_requirements[next_level]) * 100)
        xp_required = level_xp_requirements[next_level] - xp
        main_page = int(level / 5)
    else: 
        next_level_percentage = "!!MAX LEVEL!!"
        xp_required = "Max Level Reached, no"
        next_level = "∞"
        main_page = 3

    ### Pages
    global skill_tree_pages
    skill_tree_pages = [
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              _________\n|_ Tiny XP Pack     /                              |\n|  |________________|   _ Embed Perms        |\n|_ 1.10xp Multi    \\___|_________________|_________\n===================================================\n[ 0 ]-----[ 1 ]-----[ 2 ]-----[ 3 ]-----[ 4 ]-----[ 5 ]\n===================================================\n{xp_required} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n____ Media Perms ________  _  _____ /report Command __\n        __ External Emojis ___/   \_ External Stickers ___\n____/                               /                                              /\n         \\\__ Small XP Pack __/              Talk in Threads ___/\n===================================================\n[ 6 ]-----[ 7 ]-----[ 8 ]-----[ 9 ]-----[1 0]-----[1 1]\n===================================================\n{xp_required} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n___ _______________________________________ \n       |_ Nickname Perms                  Medium XP Pack _|\n                   Tester Role _|                  |_ 1.25xp Multi\n                   |______________________________|__________\n===================================================\n[1 2]-----[1 3]-----[1 4]-----[1 5]-----[1 6]-----[1 7]\n===================================================\n{xp_required} xp until level {next_level}, You have {skill_points} SP to spend.",
    f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n                _____ MASSIVE XP PACK\n             /____ VC Status\n           /______________________ **(=[Completionist Role]=)**\n____/_____ Create Invites                     [Requires all skills]\n===================================================\n[1 8]-----[1 9]-----[2 0]               **More Comming Soon**\n===================================================\n{xp_required} xp until level {next_level}, You have {skill_points} SP to spend."
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
    if level != max_level: progress_bar = int((((level * 5)) + (int(next_level_percentage) / 20) - page*25))
    else: progress_bar = 25
    # Progress Bar Updater, (((level x 5) + (% to next level)) / 20) - (pageNUM x 25) << 'resets' bar every 5 levels
    #                                  (in 20% increments)^^     ^^(to get 20% 'chunks')
    if progress_bar < 0: progress_bar = 0 # if negative, set to 0
    message = message.replace("-", "~", progress_bar)
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
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
    
    @nextcord.ui.button(label="Main", style=nextcord.ButtonStyle.blurple, custom_id="skill_tree:main")
    async def main(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            if page != main_page:
                message = changePage(direction="main")
                await interaction.response.edit_message(content=message, view=self) # wont if already on main page
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

    @nextcord.ui.button(label="Next", style=nextcord.ButtonStyle.green, custom_id="skill_tree:next")
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            if page != len(skill_tree_pages)-1:
                message = changePage(direction="next")
                await interaction.response.edit_message(content=message, view=self) # wont work on last page
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
    
    @nextcord.ui.button(label="Buy Skills", style=nextcord.ButtonStyle.green, custom_id="skill_tree:buy")
    async def buy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            await interaction.response.edit_message(view=purchase_dropdown_view(interaction))
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

    @nextcord.ui.button(label="Close", style=nextcord.ButtonStyle.red, custom_id="skill_tree:close")
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == userID: # Command user
            await interaction.response.edit_message(view=None)
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
    
class purchase_dropdown_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.add_item(purchase_dropdown())

class purchase_dropdown(nextcord.ui.Select):
    def __init__(self):
        options = []
        for i, value in enumerate(skills[page]):
            skill_index = skills[page][value]["value"]
            label = skills[page][value]["label"]
            prerequisites = skills[page][value]["prerequisites"]
            description = skills[page][value]["description"]
            cost = skills[page][value]["cost"]
            emoji = skills[page][value]["emoji"]
            if skill_index in purchased_nodes: pass # Dont show already purchased
            else: # Only shows perks that can be purchased
                if all(prerequisites in purchased_nodes for prerequisites in prerequisites):
                    skill_index = str(skill_index)
                    i = nextcord.SelectOption(label=label, value=skill_index, description=str(description)+" [Cost: "+str(cost)+" SP]", emoji=emoji)
                    options.append(i)
                else: pass
        options.append(nextcord.SelectOption(label="Close", value="Close", description="Close buy menu.", emoji="❌")) # add close to each dropdown

        super().__init__(placeholder="Select a skill to buy", min_values=1, max_values=1, options=options)
    
    async def callback(self, interaction: nextcord.Interaction): # On dropdown click
        if interaction.user.id == userID:
            if skill_points > 0: # has skill points
                if self.values[0] != "Close": # save if chose skill
                    if skill_points < skills[page][float(self.values[0])]["cost"]: # not enough skill points
                        message = changePage(direction="none")
                        await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
                        await interaction.followup.send("You don't have enough skill points to buy this.", ephemeral=True)
                    else: # has enough skill points
                        skill_purchased = float(self.values[0])
                        updateSkillData(userID, skill_purchased)

                        role = skills[page][skill_purchased]["roleID"]
                        if role == "n/a": # if there is no role (XP packs, XP multipliers & color roles)
                            if skill_purchased == 0.4: # Custom Color Picker
                                message = changePage(direction="none")
                                await interaction.response.edit_message(content=message, view=color_dropdown_view(interaction))
                            elif skill_purchased == 0.2: await updateXP(userID, Type="Pack_tiny", message=None) # tiny xp pack
                            elif skill_purchased == 1.3: await updateXP(userID, Type="Pack_small", message=None) # small xp pack
                            elif skill_purchased == 2.2: await updateXP(userID, Type="Pack_medium", message=None) # medium xp pack
                            elif skill_purchased == 3.2: await updateXP(userID, Type="Pack_massive", message=None) # massive xp pack
                            elif skill_purchased == 0.3: # 10% multi
                                db_user_data.find_one_and_update(
                                    {"userID": userID},
                                    {"$inc": {"level_stats.xp_multi": + 0.1}}
                                )
                                
                            elif skill_purchased == 2.4: # 25% multi
                                db_user_data.find_one_and_update(
                                    {"userID": userID},
                                    {"$inc": {"level_stats.xp_multi": + 0.25}}
                                )

                            if skill_purchased != 0.4: # if not picking color, close menu
                                message = changePage(direction="none")
                                await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))

                        else: # give role
                            role = interaction.guild.get_role(role)
                            await interaction.user.add_roles(role)
                            message = changePage(direction="none")
                            await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
                            await interaction.followup.send("Granted "+str(role)+" role.", ephemeral=True)

                else: # is 'close'
                    message = changePage(direction="none")
                    await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
            else: # no skill points
                message = changePage(direction="none") 
                await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
                if self.values[0] != "Close": await interaction.followup.send("You don't have any skill points to spend.", ephemeral=True)
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

class color_dropdown_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.add_item(color_dropdown())

class color_dropdown(nextcord.ui.Select):
    def __init__(self):
        options = []
        options.append(nextcord.SelectOption(label="Red", value="red", description="Pick Red", emoji="🟥"))
        options.append(nextcord.SelectOption(label="Orange", value="orange", description="Pick Orange", emoji="🟧"))
        options.append(nextcord.SelectOption(label="Yellow", value="yellow", description="Pick Yellow", emoji="🟨"))
        options.append(nextcord.SelectOption(label="Green", value="green", description="Pick Green", emoji="🟩"))
        options.append(nextcord.SelectOption(label="Blue", value="blue", description="Pick Blue", emoji="🟦"))
        options.append(nextcord.SelectOption(label="Purple", value="purple", description="Pick Purple", emoji="🟪"))

        super().__init__(placeholder="Select a color", min_values=1, max_values=1, options=options)
    
    async def callback(self, interaction: nextcord.Interaction): # On dropdown click
        if interaction.user.id == userID:
            if self.values[0] == "red": role = 1160775712333123584
            elif self.values[0] == "orange": role = 1160776233181773914
            elif self.values[0] == "yellow": role = 1160776338567872592
            elif self.values[0] == "green": role = 1160776420587470928
            elif self.values[0] == "blue": role = 1160776569191661658
            elif self.values[0] == "purple": role = 1160776716256559175
            role = interaction.guild.get_role(role)
            await interaction.user.add_roles(role)
            message = changePage(direction="none")
            await interaction.response.edit_message(content=message, view=skill_tree_view(interaction))
        else: 
            await interaction.response.send_message("nuh uh, You need to open your own skill tree menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

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
        await saveData(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_skill_tree_Cog(bot))
