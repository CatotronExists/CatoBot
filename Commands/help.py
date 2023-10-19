import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID
from Configs.Main_config import rule_channel, announcement_channel

class Command_help_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[guild_ID], name="help", description="Use /help [command] or just /help help for information")
    async def help(self, interaction: nextcord.Interaction, searched_command: str = nextcord.SlashOption (name="command", description="Pick a command or \"help\"", choices={"help": "help", "bot_stats": "bot_stats", "user_lookup": "user_lookup", "leaderboard": "leaderboard", "skill_tree": "skill_tree", "server_stats": "server_stats"})):
        command = 'help'
        userID = interaction.user.id
        formatOutput(output="/"+command+" Used by ("+str(userID)+")", status="Normal")

        channel1 = self.bot.get_channel(rule_channel)
        channel2 = self.bot.get_channel(announcement_channel)

        if searched_command == "bot_stats": await interaction.send(f"**Help Menu** | /{searched_command}\n\n/bot_stats Shows the bot's stats.\nCurrently it shows showing bot version, uptime and what time it started up.\n\nThere isn't much in here for now, but there will be more soon.\n")
        elif searched_command == "user_lookup": await interaction.send(f"**Help Menu** | /{searched_command}\n\n/user_lookup can be used to find information on you or any other member.\nType /user_lookup user: (a user). If you leave the user field blank it shows you your information.\n/user_lookup shows join date, commands and messages sent, level, current xp, xp multi and skill tree progress.\n\nNote: Any user that had joined before June 2nd 2023, Had join time set to midnight UTC of join date.")
        elif searched_command == "leaderboard": await interaction.send(f"**Help Menu** | /{searched_command}\n\n/leaderboard Shows the top 10 leveled users or top 10 most used commands\nUse /leaderboard type: (type) to choose which leaderboard to open.")
        elif searched_command == "skill_tree": await interaction.send(f"**Help Menu** | /{searched_command}\nThe skill tree is a different take on the typical level system.\nGain XP by sending messages. There is a rare chance of getting bonus xp 'packs'.\nWhen you reach a new level you gain a Skill Point (SP). These are spent buying skills in /skill_tree.\nTo buy a perk you need to have the required skill, these can be seen by the lines linking them together.\nYou have to own the previous skill to purchase the next!")
        elif searched_command == "server_stats": await interaction.send(f"**Help Menu** | /{searched_command}\n\n/server_stats Shows the server's stats.\nCurrently it shows server name, server ID, server owner, server created at, server members, server channels and server roles.")
        else: # open help menu
            await interaction.send(f"**Help Menu**\n\nRules: {channel1.mention}\nLatest News/Announcements: {channel2.mention}\nIf you need to contact a mod go here: (soon)\n--------------------------------------------------------\nType /help [command] to get information on that command.")
        await saveData(command, userID, Type="Command")

def setup(bot):
    bot.add_cog(Command_help_Cog(bot))