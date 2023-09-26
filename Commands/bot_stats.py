import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID, start_time
from Config import version

class Command_bot_stats_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="bot_stats", description="Displays stats for the bot")
    async def bot_stats(self, interaction: nextcord.Interaction):
        command = 'bot_stats'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await interaction.response.defer(with_message=True)

        current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        uptime = datetime.datetime.strptime(current_time, '%d-%m-%Y %H:%M:%S') - datetime.datetime.strptime(start_time, '%d-%m-%Y %H:%M:%S')
        await interaction.send("Bot Stats\nCurrent Version: "+str(version)+"\nBot Uptime: "+str(uptime)+" // Online Since "+str(start_time)+" AEST")
        await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_bot_stats_Cog(bot))