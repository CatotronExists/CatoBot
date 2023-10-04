### Skill Tree/Leveling Configs ###
level_xp_requirements = [0, 10, 40, 80, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750]
#                        0   1   2   3    4    5    6    7    8    9   10   11   12    13    14    15    16    17    18    19    20
lowerXP_gain = 1 # lowest amount of xp you can gain
upperXP_gain = 15 # highest amount of xp you can gain

skills = {
    0: {
        0.1: {
        "label": "Reaction Perms",
        "description": "Unlock Reactions in the server.",
        "cost": 1,
        "value": 0.1,
        "prerequisites": [],
        "emoji": "💬",
        "roleID": 1158924938951020564
        },
        0.2: {
        "label": "Small XP Pack",
        "description": "Grants you 200xp.",
        "cost": 1,
        "value": 0.2,
        "prerequisites": [],
        "emoji": "📦",
        "roleID": "n/a"
        },
        0.3: {
        "label": "1.10xp Multi",
        "description": "Increase your xp gain by 10%. PERMANENTLY. (Stacks with other bonuses)",
        "cost": 1,
        "value": 0.3,
        "prerequisites": [],
        "emoji": "📈",
        "roleID": "n/a"
        },
        0.4: {
        "label": "Custom Color",
        "description": "Gain a custom color role.",
        "cost": 1,
        "value": 0.4,
        "prerequisites": [0.2],
        "emoji": "🎨",
        "roleID": 1158926421591347201 # just the placeholder role, [defaultID, color1ID, color2ID, color3ID]
        },
        0.5: {
        "label": "Embed Perms",
        "description": "Unlock Embeds in the server.",
        "cost": 1,
        "value": 0.5,
        "prerequisites": [0.2],
        "emoji": "📄",
        "roleID": 1158926663262941295
        }
    },
    1: {
        1.1: {
        "label": "Media Perms",
        "description": "Unlock Media Perms in the server.",
        "cost": 1,
        "value": 1.1,
        "prerequisites": [0.2],
        "emoji": "📨",
        "roleID": 1158927442908553360
        },
        1.2: {
        "label": "External Emojis",
        "description": "Be able to use external emojis in the server.",
        "cost": 1,
        "value": 1.2,
        "prerequisites": [0.2],
        "emoji": "😀",
        "roleID": 1158927844102131771
        },
        1.3: {
        "label": "Small XP Pack",
        "description": "Grants you 200xp.",
        "cost": 1,
        "value": 1.3,
        "prerequisites": [0.2],
        "emoji": "📦",
        "roleID": "n/a"
        },
        1.4: {
        "label": "/report Command",
        "description": "Unlock the /report command. (Comming Soon)",
        "cost": 1,
        "value": 1.4,
        "prerequisites": [1.1, 1.2, 1.3],
        "emoji": "👮‍♂️",
        "roleID": 1158928155957002241
        },
        1.5: {
        "label": "External Stickers",
        "description": "Be able to use external stickers in the server.",
        "cost": 1,
        "value": 1.5,
        "prerequisites": [1.1, 1.2, 1.3],
        "emoji": "🤩",
        "roleID": 1158928412665188444
        },
        1.6: {
        "label": "Talk in Threads",
        "description": "Be able to talk in threads.",
        "cost": 1,
        "value": 1.6,
        "prerequisites": [1.5],
        "emoji": "🧵",
        "roleID": 1158928609159950437
        },    
    },
    2: {
        2.1: {
        "label": "Nickname Perms",
        "description": "Be able to change your nickname in the server.",
        "cost": 1,
        "value": 2.1,
        "prerequisites": [],
        "emoji": "🗨",
        "roleID": 0
        },
        2.2: {
        "label": "Medium XP Pack",
        "description": "Grants you 500xp.",
        "cost": 1,
        "value": 2.2,
        "prerequisites": [],
        "emoji": "🎁",
        "roleID": 0
        },
        2.3: {
        "label": "Tester Role",
        "description": "Help test the bot, when needed.",
        "cost": 1,
        "value": 2.3,
        "prerequisites": [],
        "emoji": "🛠",
        "roleID": 0
        },
        2.4: {
        "label": "1.25xp Multi",
        "description": "Increase your xp gain by 25%. PERMANENTLY. (Stacks with other bonuses)",
        "cost": 1,
        "value": 2.4,
        "prerequisites": [],
        "emoji": "📈",
        "roleID": 0
        }
    }
}

## Find Number of skills
def number():
    skill_number = 0
    for i in skills:
        for j in skills[i]:
            skill_number += 1
    return skill_number

skill_number = number()