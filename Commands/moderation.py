import nextcord
import datetime
from nextcord.ext import commands
from Main import formatOutput, saveData, guild_ID
from Configs.Main_config import db_user_data

##########################################################
### Views
##########################################################
###########################
### Main View
###########################
class moderation_menu_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    @nextcord.ui.button(label="Action", style=nextcord.ButtonStyle.blurple)
    async def action(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.response.edit_message(view=moderation_action_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

    @nextcord.ui.button(label="History", style=nextcord.ButtonStyle.blurple)
    async def history(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

    @nextcord.ui.button(label="Remove", style=nextcord.ButtonStyle.blurple)
    async def remove(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_remove_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

    @nextcord.ui.button(label="Close Menu", style=nextcord.ButtonStyle.red)
    async def fullclose(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=None)

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

###########################
### History Choice View
###########################
class moderation_history_choice_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    @nextcord.ui.button(label="Warns", style=nextcord.ButtonStyle.blurple)
    async def warns(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_view(interaction, mode="warns"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)

    @nextcord.ui.button(label="Kicks", style=nextcord.ButtonStyle.blurple)
    async def kicks(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_view(interaction, mode="kicks"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)")

    @nextcord.ui.button(label="Bans", style=nextcord.ButtonStyle.blurple)
    async def bans(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_view(interaction, mode="bans"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif)")

    @nextcord.ui.button(label="Mutes", style=nextcord.ButtonStyle.blurple)
    async def mutes(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_view(interaction, mode="mutes"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)")

###########################
### History View {mode}
###########################
class moderation_history_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction, mode=None):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.mode = mode
    
    @nextcord.ui.button(label="Back", style=nextcord.ButtonStyle.blurple)
    async def back(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_choice_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Forward", style=nextcord.ButtonStyle.blurple)
    async def forward(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_history_choice_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Close", style=nextcord.ButtonStyle.red)
    async def close(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_menu_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

###########################
### Action View
###########################
class moderation_action_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    @nextcord.ui.button(label="Warn", style=nextcord.ButtonStyle.blurple)
    async def warn(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_action_form_view(interaction, action="warn"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Kick", style=nextcord.ButtonStyle.blurple)
    async def kick(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.response.edit_message(view=moderation_action_form_view(interaction, action="kick"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Ban", style=nextcord.ButtonStyle.blurple)
    async def ban(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.response.edit_message(view=moderation_action_form_view(interaction, action="ban"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Mute", style=nextcord.ButtonStyle.blurple)
    async def mute(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.response.edit_message(view=moderation_action_form_view(interaction, action="mute"))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.response.edit_message(view=moderation_menu_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

###########################
### Action Form View (Builds reason, duration)
###########################
class moderation_action_form_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction, action=None):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.action = action
    
    @nextcord.ui.button(label="Reason", style=nextcord.ButtonStyle.blurple)
    async def reason(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_reason_dropdown())
                
            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
    
    @nextcord.ui.button(label="Duration", style=nextcord.ButtonStyle.blurple)
    async def duration(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                if self.action == "warn": await interaction.response.edit_message(view=moderation_duration_dropdown(interaction, action=self.action))
                else: await interaction.response.edit_message(view=moderation_duration_dropdown(interaction, action=self.action))
                
            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.blurple)
    async def confirmaction(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_menu_view(interaction))
                # 'commit' action & save
                # plus followup confirming action has been done

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.response.edit_message(view=moderation_menu_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/)", ephemeral=True)

###########################
### Removal View
###########################
class moderation_remove_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    @nextcord.ui.button(label="Case 1", style=nextcord.ButtonStyle.blurple)
    async def case1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.send("Case Removed", ephemeral=True)

            else: await interaction.send("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
        else: await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

    @nextcord.ui.button(label="Case 2", style=nextcord.ButtonStyle.blurple)
    async def case2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.send("Case Removed", ephemeral=True)

            else: await interaction.send("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
        else: await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

    @nextcord.ui.button(label="Case 3", style=nextcord.ButtonStyle.blurple)
    async def case3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                await interaction.send("Case Removed", ephemeral=True)

            else: await interaction.send("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
        else: await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

    @nextcord.ui.button(label="Case 4", style=nextcord.ButtonStyle.blurple)
    async def case4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.send("Case Removed", ephemeral=True)

            else: await interaction.send("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
        else: await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:    
                await interaction.response.edit_message(view=moderation_menu_view(interaction))

            else: await interaction.send("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)
        else: await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

##########################################################
### Dropdowns
##########################################################
###########################
### Reason Dropdown
###########################
class moderation_reason_dropdown_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction, action=None):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.action = action
        self.add_item(moderation_reason_dropdown())

class moderation_reason_dropdown(nextcord.ui.Select):
    def __init__(self):
        options = []
        options.append(nextcord.SelectOption(label="Reason 1", value="Reason 1"))
        options.append(nextcord.SelectOption(label="Reason 2", value="Reason 2"))
        options.append(nextcord.SelectOption(label="Reason 3", value="Reason 3"))
        options.append(nextcord.SelectOption(label="Reason 4", value="Reason 4"))
        options.append(nextcord.SelectOption(label="Reason 5", value="Reason 5"))
        options.append(nextcord.SelectOption(label="Cancel", value="Cancel"))
        super().__init__(placeholder="Select a Reason", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                if self.values[0] == "Cancel": await interaction.response.edit_message(view=moderation_menu_view(interaction))
                else: await interaction.response.edit_message(view=moderation_action_form_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

###########################
### Duration Dropdown
###########################
class moderation_duration_dropdown_view(nextcord.ui.View):
    def __init__(self, interaction: nextcord.Interaction, action=None):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.action = action
        self.add_item(moderation_duration_dropdown())

class moderation_duration_dropdown(nextcord.ui.Select):
    def __init__(self):
        options = []
        options.append(nextcord.SelectOption(label="Permanent", value="Permanent"))
        options.append(nextcord.SelectOption(label="10m", value="10m"))
        options.append(nextcord.SelectOption(label="30m", value="30m"))
        options.append(nextcord.SelectOption(label="1h", value="1h"))
        options.append(nextcord.SelectOption(label="6h", value="6h"))
        options.append(nextcord.SelectOption(label="12h", value="12h"))
        options.append(nextcord.SelectOption(label="1d", value="1d"))
        options.append(nextcord.SelectOption(label="7d", value="7d"))
        options.append(nextcord.SelectOption(label="30d", value="30d"))
        options.append(nextcord.SelectOption(label="90d", value="90d"))
        options.append(nextcord.SelectOption(label="180d", value="180d"))
        options.append(nextcord.SelectOption(label="365d", value="365d"))
        options.append(nextcord.SelectOption(label="Cancel", value="Cancel"))
        super().__init__(placeholder="Select a Duration", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator == True:
            if interaction.user.id == self.interaction.user.id:
                if self.values[0] == "Cancel": await interaction.response.edit_message(view=moderation_action_form_view(interaction, action=self.action))
                else: await interaction.response.edit_message(view=moderation_action_form_view(interaction))

            else: await interaction.response.send_message("nuh uh, You need to open your own moderation menu!\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
        else: await interaction.response.send_message("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh)", ephemeral=True)

##########################################################
### Command
##########################################################
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

        if interaction.user.guild_permissions.administrator == True:
            if user.id != userID: # if self -> dont open
                if user.guild_permissions.administrator != True: # if admin -> dont open
                    await interaction.response.defer()
                    formatOutput(output="    "+str(userID)+" Opened Moderation Menu for "+str(user.id), status="Normal")

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
                    embed = nextcord.Embed(color=color, title="Moderation Menu", description=f"Moderation Menu for {searched_username} | ID:{user.id}", type="rich")
                    embed.set_thumbnail(url=avatar)
                    embed.add_field(name="Join Date", value=join_date, inline=True)
                    embed.add_field(name="Messages Sent", value=messages_sent, inline=True)
                    embed.add_field(name="Warns", value=warn_count, inline=True)
                    embed.add_field(name="Kicks", value=kick_count, inline=True)
                    embed.add_field(name="Bans", value=ban_count, inline=True)
                    embed.add_field(name="Mutes", value=mute_count, inline=True)
                    embed.set_footer(text=f"Moderation Menu opened by {username}")
                    await interaction.send(embed=embed, view=moderation_menu_view(interaction))
                    await saveData(command, userID, Type="Command")

                else:
                    await interaction.send("nuh uh, you cant moderate a mod/admin\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
                    await saveData(command, userID, Type="Command")
                    formatOutput(output="    "+str(userID)+" Attempted to moderate a mod/admin", status="Warning")

            else: 
                await interaction.send("nuh uh, you cant moderate yourself\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
                await saveData(command, userID, Type="Command")
                formatOutput(output="    "+str(userID)+" Attempted to moderate self", status="Warning")

        else: 
            await interaction.send("nuh uh, Insufficient Permissions\nMissing Administrator Permissions\n[Nuh Uh](https://tenor.com/view/nuh-uh-nuh-uh-starved-eggman-gif-26280682)", ephemeral=True)
            await saveData(command, userID, Type="Command")
            formatOutput(output="    Insufficient Permissions for "+str(userID), status="Warning")

def setup(bot):
    bot.add_cog(Command_moderation_Cog(bot))

### ADD OPTION TO CHANGE REASON/DURATION
## Send message to user, inviting them back after being unbanned
## send message to user, saying they have been warned, muted, kicked, banned
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