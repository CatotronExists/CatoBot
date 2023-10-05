### Skill Tree/Leveling Configs ###
level_xp_requirements = [0, 10, 40, 80, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750]
#                        0   1   2   3    4    5    6    7    8    9   10   11   12    13    14    15    16    17    18    19    20

lowerXP_gain = 1 # lowest amount of xp you can gain
upperXP_gain = 1500 # highest amount of xp you can gain
# xp pack amounts
XP_pack_tiny = 100
XP_pack_small = 300
XP_pack_medium = 1000
XP_pack_massive = 3000
max_level = 20

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
        "label": "Tiny XP Pack",
        "description": "Grants you "+str(XP_pack_tiny)+"xp.",
        "cost": 1,
        "value": 0.2,
        "prerequisites": [],
        "emoji": "📦",
        "roleID": "n/a"
        },
        0.3: {
        "label": "1.10xp Multi",
        "description": "XP gain upped by 10%. PERMANENTLY. (Stacks)",
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
        "description": "Grants you "+str(XP_pack_small)+"xp.",
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
        "prerequisites": [1.4],
        "emoji": "🗨",
        "roleID": 1159268603531624528
        },
        2.2: {
        "label": "Medium XP Pack",
        "description": "Grants you "+str(XP_pack_medium)+"xp.",
        "cost": 2,
        "value": 2.2,
        "prerequisites": [1.4],
        "emoji": "🎁",
        "roleID": "n/a"
        },
        2.3: {
        "label": "Tester Role",
        "description": "Help test the bot, when needed.",
        "cost": 1,
        "value": 2.3,
        "prerequisites": [2.1],
        "emoji": "🛠",
        "roleID": 1159268716756860938
        },
        2.4: {
        "label": "1.25xp Multi",
        "description": "XP gain upped by 25%. PERMANENTLY. (Stacks)",
        "cost": 2,
        "value": 2.4,
        "prerequisites": [2.2],
        "emoji": "📈",
        "roleID": "n/a"
        }
    },
    3: {
        3.1: {
        "label": "Create Invites",
        "description": "Now you can create invites, cool I guess.",
        "cost": 1,
        "value": 3.1,
        "prerequisites": [2.3, 2.4],
        "emoji": "📨",
        "roleID": 1159268789494485033
        },
        3.2: {
        "label": "VC Status",
        "description": "Set the status of your VC",
        "cost": 1,
        "value": 3.2,
        "prerequisites": [2.3, 2.4],
        "emoji": "🎙",
        "roleID": 1159268885850243133
        },
        3.3: {
        "label": "MASSIVE XP PACK",
        "description": "Grants you "+str(XP_pack_massive)+"xp.",
        "cost": 3,
        "value": 3.3,
        "prerequisites": [2.3,2.4],
        "emoji": "📈",
        "roleID": "n/a"
        },
        3.4: {
        "label": "Completionist",
        "description": "Gain the ultimate role, Completionist.",
        "cost": 1,
        "value": 3.4,
        "prerequisites": [0.1, 0.2, 0.3, 0.4, 0.5, 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3], # every skill
        "emoji": "🏆",
        "roleID": 1159269069921452192
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