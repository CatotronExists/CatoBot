import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID

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

class Command_command_leaderboard_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="command_leaderboard", description="Shows leaderboard for each command usage")
    async def command_leaderboard(self, interaction: nextcord.Interaction):
        await interaction.send("Command Leaderboard:")
        command = 'command_leaderboard'
        userID = interaction.user.id
        await save(command, userID)

def setup(bot):
    bot.add_cog(Command_command_leaderboard_Cog(bot))