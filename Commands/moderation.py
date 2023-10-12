import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID
from Configs.Main_config import db_user_data

class Command_moderation_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="moderation", description="Opens the Moderation Menu")
    async def moderation(self, interaction: nextcord.Interaction, user: nextcord.User):
        command = 'moderation'
        userID = interaction.user.id
        username = interaction.user.name
        searched_username = user.name
        searched_user_id = interaction.guild.get_member(user.id)
        
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")
        await interaction.response.defer()

        if interaction.user.guild_permissions.administrator == True:
            # add check if self -> dont open
            # add check is admin -> dont open
            data = db_user_data.find_one({"userID": user.id})
            join_date = data["join_date"]
            messages_sent = data["messages_sent"]
            warn_count = data["moderation_data"]["warns"]["warn_count"]
            warn_timestamps = data["moderation_data"]["warns"]["warn_timestamps"]
            warn_reasons = data["moderation_data"]["warns"]["warn_reasons"]
            kick_count = data["moderation_data"]["kicks"]["kick_count"]
            kick_timestamps = data["moderation_data"]["kicks"]["kick_timestamps"]
            kick_reasons = data["moderation_data"]["kicks"]["kick_reasons"]
            ban_count = data["moderation_data"]["bans"]["ban_count"]
            ban_timestamps = data["moderation_data"]["bans"]["ban_timestamps"]
            ban_reasons = data["moderation_data"]["bans"]["ban_reasons"]
            mute_count = data["moderation_data"]["mutes"]["mute_count"]
            mute_timestamps = data["moderation_data"]["mutes"]["mute_timestamps"]
            mute_reasons = data["moderation_data"]["mutes"]["mute_reasons"]

            if searched_user_id.avatar == None: avatar = searched_user_id.default_avatar
            else: avatar = searched_user_id.display_avatar

            color = interaction.user.color
            embed = nextcord.Embed(color=color, title="Moderation Menu", description=f"Moderation Menu for {searched_username} | ID:{user.id}",type="rich")
            embed.set_thumbnail(url=avatar)
            embed.add_field(name="Join Date", value=join_date, inline=True)
            embed.add_field(name="Messages Sent", value=messages_sent, inline=True)
            embed.add_field(name="Warns", value=warn_count, inline=True)
            embed.add_field(name="Kicks", value=kick_count, inline=True)
            embed.add_field(name="Bans", value=ban_count, inline=True)
            embed.add_field(name="Mutes", value=mute_count, inline=True)
            embed.set_footer(text=f"Moderation Menu opened by {username}")
            await interaction.send(embed=embed)
            await saveData(command, userID, Type="Command")
        
        else: 
            await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions", ephemeral=True)
            await saveData(command, userID, Type="Command")
            formatOutput(output="    Insufficient Permissions for "+str(userID), status="Warning")

def setup(bot):
    bot.add_cog(Command_moderation_Cog(bot))

# Moderation Menu Guide
# Key: |_____| = Loop Back. - [] = Options. ^ = comment
# "Alot less complex than it looks"
# =================================================================================================
#     ________________________________________________________________________________________
#    |                                                                                        \
# 'main' buttons: action, history, close                                                       \
#         __________/       |         \___________________________________________ [Close Menu] | 
#        |               'history' buttons: warn, kick, ban, mute, cancel ________ [Back to 'main']
#        |                    _____________/_____/_____/______/__________________/
#        |                   |                                                  /
#        |      'history {category}' buttons: back, forward, close ____________/
#        |                                    |_^page nav_|                   /
#        |                                                                   /
#     'action' buttons: warn, kick, ban, mute, cancel ______________________/
#              __________/_____/_____/_____/                               /
#             |                                                           /
#  'action {action}' buttons: reason, duration, confirm, cancel _________/
#                             |\_ Dropdown |\_ Dropdown \_ ^Confirms Action
#                             |_____|      |_____| - [0 (perm), 10m, 30m, 1h, 6h, 12h, 1d, 7d, 30d, 90d, 180d, 365d]
#                                    \ - [reason 1, reason 2, reason 3, reason 4, reason 5, reason 6]
