import nextcord
from nextcord.ext import commands
from Main import formatOutput, save, guild_ID, fetchUserData

class Command_user_lookup_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="user_lookup", description="Lookup stats for a user")
    async def user_lookup(self, interaction: nextcord.Interaction, user: nextcord.User = None):
        command = 'user_lookup'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await interaction.response.defer(with_message=True)
        searched_user_id = user.id

        data = fetchUserData(user, searched_user_id)
        try: # Data Found
            join_date = data["join_date"]
            messages_sent = data["messages_sent"]
            commands_sent = data["commands_sent"]
            await interaction.send("Showing Stats for "+str(user)+" | ID: ("+str(searched_user_id)+")\nJoin Date: "+str(join_date)+"\nMessages Sent: "+str(messages_sent)+"\nCommands Sent: "+str(commands_sent))
        except Exception as e: # replies with error message
            await interaction.send(data)
        finally: # then save
            await save(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_user_lookup_Cog(bot))