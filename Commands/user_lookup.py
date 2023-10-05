import nextcord
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID, fetchUserData
from Configs.ST_config import max_level

class Command_user_lookup_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="user_lookup", description="Lookup stats for a user")
    async def user_lookup(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        command = 'user_lookup'
        searched_user_id = userID = interaction.user.id

        if user == None: user = await self.bot.fetch_user(userID) # if no user is specified, default to the user who used the command
        user = str(user)
        if user[-2:] == "#0": user = user[:-2] # remove #0

        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await interaction.response.defer(with_message=True)

        data = fetchUserData(searched_user_id)
        try: # Data Found
            join_date = data["join_date"]
            messages_sent = data["messages_sent"]
            commands_sent = data["commands_sent"]
            level = data["level_stats"]["level"]
            xp = data["level_stats"]["xp"]
            skill_tree_progress = data["level_stats"]["skill_tree_progress"]
            xp_multi = data["level_stats"]["xp_multi"]

            if level != max_level: embed = nextcord.Embed(title="Showing Stats for "+str(user)+" | ID: ("+str(searched_user_id)+")", description="Join Date: "+str(join_date)+"\nMessages Sent: "+str(messages_sent)+"\nCommands Sent: "+str(commands_sent)+"\n**Level Data**\n-->> Level: "+str(level)+"\n-->> XP: "+str(xp)+"\n-->> XP Multi: "+str(1 + xp_multi)+"\n-->> Skill Tree Progress: "+str(skill_tree_progress))
            else: embed = nextcord.Embed(title="Showing Stats for "+str(user)+" | ID: ("+str(searched_user_id)+")", description="Join Date: "+str(join_date)+"\nMessages Sent: "+str(messages_sent)+"\nCommands Sent: "+str(commands_sent)+"\n**Level Data**\n-->> Level: "+str(level)+"\n-->> Overflow XP: "+str(xp)+"\n-->> XP Multi: "+str(1 + xp_multi)+"\n-->> Skill Tree Progress: "+str(skill_tree_progress))
            await interaction.send(embed=embed)
        except Exception as e: # replies with error message
            await interaction.send(data)
        finally: # then save
            await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_user_lookup_Cog(bot))