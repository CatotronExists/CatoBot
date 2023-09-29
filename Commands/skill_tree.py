import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID

username = "catotron"
username = username.capitalize()
level = 1
skill_tree_progress = 0
max_skill_tree_progress = 100
xp = 0
next_level = level + 1
skill_points = 0

skill_tree_page_1 = f"{username}, Level {level} | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms   _ Custom Color              __\n|_ Image Perms   /                             |\n|  |________________|   _ Embed Perms         |\n|_ 1.25xp Multi    \\___|_________________|__\n=================================================== \n[ 0 ]-----[ 1 ]-----[ 2 ]-----[ 3 ]-----[ 4 ]-----[ 5 ]\n===================================================\n{xp} xp until level {next_level}, You have {skill_points} SP to spend."

# {username}, Level {level}, {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked
# |_ Reaction Perms     _ Custom Color            __
# |_ Image Perms       /                         |
# |  |________________|     _ Embed Perms        |
# |_ 1.25xp Multi      \___|_____________________|__
# ==================================================
# [ 0 ]~~~~~[ 1 ]~~~~~[ 2 ]~~~~~[ 3 ]~~~~~[ 4 ]~~--[ 5 ]
# ==================================================
# {xp} xp until level {next_level}, You have {skill_points} skill points to spend.


# [ 1 ]
# [1 0]
# [100]

class Command_skill_tree_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="skill_tree", description="Show skill tree")
    async def skill_tree(self, interaction: nextcord.Interaction):
        command = 'skill_tree'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

        await interaction.response.defer(with_message=True)

        #skill_tree_edit0 = skill_tree_page_1.replace("|", "\|")

        skill_tree_edit1 = skill_tree_page_1.replace("_", "\_")
        skill_tree_edit2 = skill_tree_edit1.replace("~", "\~")
        await interaction.send(skill_tree_edit2)

        
        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_skill_tree_Cog(bot))

