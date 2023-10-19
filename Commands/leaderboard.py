import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID
from Configs.Main_config import db_bot_stats, db_user_data
from Configs.ST_config import skill_number

class Command_leaderboard_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="leaderboard", description="Open the leaderboard")
    async def leaderboard(self, interaction: nextcord.Interaction, Type: str = nextcord.SlashOption(name="type", description="The type of leaderboard to open", choices={"Level": "level", "Commands": "commands"})):
        command = 'leaderboard'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        leaderboard_type = Type.capitalize()

        embed = nextcord.Embed(color=0xff6100, title=f"{leaderboard_type} Leaderboard", description="Showing Top 10\n", type="rich")
        embed.set_thumbnail(url=interaction.guild.icon)

        if leaderboard_type == "Level":
            data = list(db_user_data.find({"level_stats.level": {"$exists": True}}).sort("level_stats.level", -1).limit(10))
            leaderboard_data = []
            for i in range(len(data)):
                if interaction.guild.get_member(data[i]['userID']) is None: continue
                data[i] = f"**{interaction.guild.get_member(data[i]['userID']).name.capitalize()[:17]}** | Level: {data[i]['level_stats']['level']} | XP: {data[i]['level_stats']['xp']} | {data[i]['level_stats']['xp_multi'] + 1}x | _{data[i]['level_stats']['skill_tree_progress']}/{skill_number} Skills_"
                leaderboard_data.append(data[i])
            embed.add_field(name="User | Level | XP | XP Multi | Skill Tree Progress | Messages Sent", value='\n'.join(leaderboard_data))

        elif leaderboard_type == "Commands":
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
            embed.add_field(name="Commands Used", value='\n'.join(leaderboard_data))

        await interaction.send(embed=embed)
        await saveData(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_leaderboard_Cog(bot))