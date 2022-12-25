"""
âœ˜ Commands Available

To Find This Repo's CreatorðŸ¥³


> CMD: `{i}creator`
"""


from telethon import events
import random, re
from . import ultroid_cmd

RUNSREACTS = [
    "Creator's ID : [Click Here](https://t.me/The_Pr3mium_Boy)",
]

@ultroid_cmd(pattern="creator")
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)
