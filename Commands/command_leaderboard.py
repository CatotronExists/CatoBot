import nextcord
import datetime
from nextcord.ext import commands
from Configs.Main_config import db_bot_stats
from Main import formatOutput, saveData, guild_ID

class Command_command_leaderboard_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="command_leaderboard", description="Shows leaderboard for each command usage")
    async def command_leaderboard(self, interaction: nextcord.Interaction):
        command = 'command_leaderboard'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await interaction.response.defer(with_message=True)

        data = db_bot_stats.find_one({"Commands_Used": {"$exists": True}})
        
        if data is not None:
            leaderboard_data = []
            for field_name, value in data.items():
                leaderboard_data.append(f"{field_name} : {value}")
        del leaderboard_data[0:2] # Removes _id and Command_Used
        leaderboard_data = sorted(leaderboard_data, key=lambda x: int(x.split(' : ')[1]))
        leaderboard_data.reverse()

        # Formats Leaderboard
        for i in range(len(leaderboard_data)):
            leaderboard_data[i] = "/"+leaderboard_data[i] # add slash
            leaderboard_data[i] = leaderboard_data[i].replace('_usage', ' usage') # change x_usage to x usage
            leaderboard_data[i] = leaderboard_data[i].replace(' : ', ': ') # push ':' next to usage
        await interaction.send("Command Leaderboard for Catotron's World\n"+'\n'.join(leaderboard_data))

        await saveData(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_command_leaderboard_Cog(bot))