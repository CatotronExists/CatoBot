username = "catotron"
username = username.capitalize()
level = 1
skill_tree_progress = 0
max_skill_tree_progress = 100
xp = 0
next_level = level + 1
skill_points = 0

skill_tree_page_1 = f"{username}, Level {level} | {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked\n|_ Reaction Perms     _ Custom Color            __\n|_ Image Perms       /                         |\n|  |________________|     _ Embed Perms        |\n|_ 1.25xp Multi      \\___|_____________________|__\n==================================================\n[ 0 ]~~~~[ 1 ]~~~~[ 2 ]~~~~[ 3 ]~~~~[ 4 ]~~--[ 5 ]\n==================================================\n{xp} xp until level {next_level}, You have {skill_points} SP to spend."

# {username}, Level {level}, {skill_tree_progress}/{max_skill_tree_progress} Skills Unlocked
# |_ Reaction Perms     _ Custom Color            __
# |_ Image Perms       /                         |
# |  |________________|     _ Embed Perms        |
# |_ 1.25xp Multi      \___|_____________________|__
# ==================================================
# [ 0 ]~~~~[ 1 ]~~~~[ 2 ]~~~~[ 3 ]~~~~[ 4 ]~~--[ 5 ]
# ==================================================
# {xp} xp until level {next_level}, You have {skill_points} skill points to spend.

print(skill_tree_page_1)

# [ 1 ]
# [1 0]
# [100]