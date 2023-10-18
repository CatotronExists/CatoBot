import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID

class Command_server_stats_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="server_stats", description="View the server stats/information")
    async def server_stats(self, interaction: nextcord.Interaction):
        command = 'server_stats'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

        guild = interaction.guild
        channels = interaction.guild.channels
        channelno = []
        for i in channels: # filter catergory channels
            if i.type == nextcord.ChannelType.text or i.type == nextcord.ChannelType.voice:
                channelno.append(i)
        members = interaction.guild.members
 
        embed = nextcord.Embed(color=0xff6100, title="Server Stats", type="rich")
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(name="Server Name", value=guild.name, inline=True)
        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(name="Server Owner", value=guild.owner.name, inline=True)
        embed.add_field(name="Server Created At", value=str(guild.created_at)[:-13], inline=True)
        embed.add_field(name="Server Members", value=len(members), inline=True)
        embed.add_field(name="Server Channels", value=len(channelno), inline=True)
        embed.add_field(name="Server Roles", value=len(guild.roles), inline=True)
        embed.set_footer(text="wow, numbers")

        await interaction.send(embed=embed)

        await saveData(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_server_stats_Cog(bot))