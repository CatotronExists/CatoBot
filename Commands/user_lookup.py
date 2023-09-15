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

class Command_user_lookup_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="user_lookup", description="Lookup stats for a user")
    async def user_lookup(self, interaction: nextcord.Interaction):
        await interaction.send("Stats for (user)")
        command = 'command_name'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_user_lookup_Cog(bot))