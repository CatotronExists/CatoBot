skills = {
    0: {
        0.1: {
        "label": "Reaction Perms",
        "description": "Unlock Reactions in the server.",
        "cost": 1,
        "value": 0.1,
        "prerequisites": [],
        "emoji": "💬"
        },
        0.2: {
        "label": "Small XP Pack",
        "description": "Grants you 200xp.",
        "cost": 1,
        "value": 0.2,
        "prerequisites": [],
        "emoji": "🖼️"
        },
        0.3: {
        "label": "1.10xp Multi",
        "description": "Increase your xp gain by 10%. PERMANENTLY.",
        "cost": 1,
        "value": 0.3,
        "prerequisites": [],
        "emoji": "📈"
        },
        0.4: {
        "label": "Custom Color",
        "description": "Gain a custom color role.",
        "cost": 1,
        "value": 0.4,
        "prerequisites": [0.2],
        "emoji": "🎨"
        },
        0.5: {
        "label": "Embed Perms",
        "description": "Unlock Embeds in the server.",
        "cost": 1,
        "value": 0.5,
        "prerequisites": [0.2],
        "emoji": "📄"
        }
    },
    1: {
        1.1: {
        "label": "Media Perms",
        "description": "Unlock Media Perms in the server.",
        "cost": 1,
        "value": 1.1,
        "prerequisites": [0.2],
        "emoji": "🔒"
        },
        1.2: {
        "label": "External Emojis",
        "description": "Be able to use external emojis in the server.",
        "cost": 1,
        "value": 1.2,
        "prerequisites": [0.2],
        "emoji": "🔒"
        },
        1.3: {
        "label": "Small XP Pack",
        "description": "Grants you 200xp.",
        "cost": 1,
        "value": 1.3,
        "prerequisites": [0.2],
        "emoji": "🔒"
        },
        1.4: {
        "label": "/report Command",
        "description": "Unlock the /report command.",
        "cost": 1,
        "value": 1.4,
        "prerequisites": [1.1, 1.2, 1.3],
        "emoji": "🔒"
        },
        1.5: {
        "label": "External Stickers",
        "description": "Be able to use external stickers in the server.",
        "cost": 1,
        "value": 1.5,
        "prerequisites": [1.1, 1.2, 1.3],
        "emoji": "🔒"
        },
        1.6: {
        "label": "Talk in Threads",
        "description": "Be able to talk in threads.",
        "cost": 1,
        "value": 1.6,
        "prerequisites": [1.5],
        "emoji": "🔒"
        },    
    },
    2: {
        2.1: {
        "label": "placeholder",
        "description": "placeholder",
        "cost": 1,
        "value": 2.1,
        "prerequisites": [],
        "emoji": "🔒"
        },
        2.2: {
        "label": "placeholder",
        "description": "placeholder",
        "cost": 1,
        "value": 2.2,
        "prerequisites": [],
        "emoji": "🔒"
        },
        2.3: {
        "label": "placeholder",
        "description": "placeholder",
        "cost": 1,
        "value": 2.3,
        "prerequisites": [],
        "emoji": "🔒"
        },
        2.4: {
        "label": "placeholder",
        "description": "placeholder",
        "cost": 1,
        "value": 2.4,
        "prerequisites": [],
        "emoji": "🔒"
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