import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID

class Command_command_leaderboard_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="command_leaderboard", description="Shows leaderboard for each command usage")
    async def command_leaderboard(self, interaction: nextcord.Interaction):
        await interaction.send("Command Leaderboard:")
        command = 'command_leaderboard'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_command_leaderboard_Cog(bot))