import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID

class Command_bot_stats_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="bot_stats", description="Displays stats for the bot")
    async def bot_stats(self, interaction: nextcord.Interaction):
        command = 'bot_stats'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        
        await interaction.send("Bot Stats")
        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_bot_stats_Cog(bot))