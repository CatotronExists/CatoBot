import nextcord
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID, fetchUserData
from Configs.ST_config import max_level

class Command_user_lookup_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="user_lookup", description="Lookup stats for a user")
    async def user_lookup(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        command = 'user_lookup'
        userID = interaction.user.id
        if user != None: searched_user_id = user.id
        else: searched_user_id = userID
        user = interaction.guild.get_member(searched_user_id)

        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await interaction.response.defer(with_message=True)

        try:
            data = fetchUserData(searched_user_id)
            join_date = data["join_date"]
            messages_sent = data["messages_sent"]
            commands_sent = data["commands_sent"]
            level = data["level_stats"]["level"]
            xp = data["level_stats"]["xp"]
            skill_tree_progress = data["level_stats"]["skill_tree_progress"]
            xp_multi = data["level_stats"]["xp_multi"]

            if user.avatar == None: avatar = user.default_avatar
            else: avatar = user.display_avatar

            username = user.name
            color = user.color
            embed = nextcord.Embed(color=color, title=f"/user_lookup {username}", description=f"User Stats for {username} ({searched_user_id})", type="rich")
            embed.set_thumbnail(url=avatar)
            embed.add_field(name="Join Date", value=join_date, inline=True)
            embed.add_field(name="Messages Sent", value=messages_sent, inline=True)
            embed.add_field(name="Commands Sent", value=commands_sent, inline=True)
            embed.add_field(name="Level", value=level, inline=True)
            if level == max_level: embed.add_field(name="Overflow XP", value=xp, inline=True)
            else: embed.add_field(name="XP", value=xp, inline=True)
            embed.add_field(name="XP Multi", value=xp_multi, inline=True)
            embed.add_field(name="Skill Tree Progress", value=skill_tree_progress, inline=True)
            await interaction.send(embed=embed)
        except Exception as e: # replies with error message
            await interaction.send(data)
        finally: # then save
            await saveData(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_user_lookup_Cog(bot))