import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID
from Config import db_user_data

class Command_skill_tree_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="skill_tree", description="Show skill tree")
    async def skill_tree(self, interaction: nextcord.Interaction):
        ### Level Requirements
        level_xp_requirements = [0, 10, 40, 80, 150, 250, 350, 450, 550]
        #                        0   1   2   3    4    5    6    7    8
        command = 'skill_tree'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

        await interaction.response.defer(with_message=True)
        # get user data
        data = db_user_data.find_one({"userID": userID})
        level = data["level_stats"]["level"]
        xp = data["level_stats"]["xp"]
        skill_tree_progress = data["level_stats"]["skill_tree_progress"]
        skill_points = data["level_stats"]["skill_points"]

        # Skill Tree Calculations
        username = interaction.user.name
        username = username.capitalize()
        max_skill_tree_progress = 100
        next_level = level + 1
        next_level_percentage = int((xp / level_xp_requirements[next_level]) * 100)

        skill_tree_page_1 = f"{username}, Level {level} ({next_level_percentage})% | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              __\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|__\n=================================================== \n[ 0 ]-----[ 1 ]-----[ 2 ]-----[ 3 ]-----[ 4 ]-----[ 5 ]\n===================================================\n{level_xp_requirements[next_level] - xp} xp until level {next_level}, You have {skill_points} SP to spend."
        skill_tree_edit0 = skill_tree_page_1.replace("-", "~", int((level*5)+(int(next_level_percentage)/20))) # progress bar updater, level x 5 + % to next level (in 20% increments)

        skill_tree_edit1 = skill_tree_edit0.replace("_", "\_")
        skill_tree_edit2 = skill_tree_edit1.replace("~", "\~")
        await interaction.send(skill_tree_edit2)

        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_skill_tree_Cog(bot))