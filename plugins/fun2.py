""" Modded For Ultroid , Take IT from Hell BOT  by @moon_knight69"""

import asyncio
import random
from os import remove
from urllib import parse

import nekos
import requests
from telethon.tl.types import ChannelParticipantsAdmins

from . import *

BASE_URL = "https://headp.at/pats/{}"
PAT_IMAGE = "pat.jpg"


@ultroid_cmd(pattern="pat ([\s\S]*)")
async def _(event):
    username = event.pattern_match.group(1)
    if not username and not event.reply_to_msg_id:
        await eod(event, "`Reply to a message or provide username`")
        return

    resp = requests.get("http://headp.at/js/pats.json")
    pats = resp.json()
    pat = BASE_URL.format(parse.quote(random.choice(pats)))
    await event.delete()
    with open(PAT_IMAGE, "wb") as f:
        f.write(requests.get(pat).content)
    if username:
        await event.client.send_file(
            event.chat_id, PAT_IMAGE, caption=username, reply_to=event.reply_to_msg_id
        )
    else:
        await event.client.send_file(
            event.chat_id, PAT_IMAGE, reply_to=event.reply_to_msg_id
        )
    remove(PAT_IMAGE)


@ultroid_cmd(pattern="join$")
async def _(event):
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="pay$")
async def _(event):
    mentions = "`█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="climb$")
async def _(event):
    mentions = "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="aag$")
async def _(event):
    mentions = "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="push$")
async def _(event):
    mentions = "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="work$")
async def _(event):
    mentions = "`📔📚           📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="suckit$")
async def _(event):
    mentions = "`......................................... \n \n𝕔𝕠𝕞𝕖 𝕥𝕠 𝕞𝕖, 𝕞𝕪 𝕔𝕙𝕚𝕝𝕕𝕣𝕖𝕟 \n`` \n. . /. ))) . . . . . . . . . (((ヽ \n/. .ノ￣. . . ___. . .￣ Y .\ \n| . (.\, . . . ( ͡° ͜ʖ ͡°). . . ./.) . ) \nヽ.ヽ..ᯢ._.|﹀|._._ノ₄₂₀ // \n. . .\|. 𓀐𓂸Ｙ. . ࿕. . . / \n. . . .|. \. . ᯪ. . .|. . ᯪ. . ﾉ \n. . . . . \ .トー仝ーイ \n. . . . . . . |. ミ土彡 / \n. . . . . . . )\. . .° . ./( \n. . . . . . /. . .\͎̦ ̷̫ ̴́ ̴̢/̴͖. . \ \n. . . . . /. ⁶⁹ . /̴͝Ѽ̔̕☰̴̈́☰☰☰☰D,̰̱ \n. . . . /. / . . / . . .\. \. . \ \n. . . .((. . . .(. . . . .). . . .)) \n. . . .| . . . .). . . . .(|. . . / \n. . . . |. . . /. . . . /. . . ./ \n. . . . |. . ..| . . . ./. . ./. . ... . . 𓁉𓀏𓀃𓁏`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="ohh$")
async def _(event):
    mentions = "`´´´´´████████´´\n´´`´███▒▒▒▒███´´´´´\n´´´███▒●▒▒●▒██´´´\n´´´███▒▒👄▒▒██´´\n´´█████▒▒████´´´´´\n´█████▒▒▒▒███´´\n█████▒▒▒▒▒▒███´´´´\n´´▓▓▓▓▓▓▓▓▓▓▓▓▓▒´´\n´´▒▒▒▒▓▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒▒´´▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒´´´´▓▓▓▓▓▓▓▒\n..▒▒.´´´´▓▓▓▓▓▓▓▒\n´▒▒▒▒▒▒▒▒▒▒▒▒\n´´´´´´´´´███████´´´´\n´´´´´´´´████████´´´´´´\n´´´´´´´█████████´´´´´\n´´´´´´██████████´´´\n´´´´´´██████████´´\n´´´´´´´█████████´\n´´´´´´´█████████´\n´´´´´´´´████████´´´\n´´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒´▒▒´´´\n´´´´´´´´´▒▒´´▒▒´´´\n´´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´▒▒´´´´´▒▒´´´\n´´´´´´´´▒▒´´´´´´▒▒´´´\n´´´´´´´´███´´´´███´´´\n´´´´´´´´████´´███´´´\n´´´´´´´´█´´███´´████´´´`"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await eor(event, mentions)


@ultroid_cmd(pattern="lovestory$")
async def _(event):
    animation_interval = 3
    animation_ttl = range(0, 20)
    await eor(event, "Starting asf")
    animation_chars = [
        "1 ❤️ love story",
        "  😐             😕 \n/👕\         <👗\ \n 👖               /|",
        "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
        "  😚            😒 \n/👕\         <👗> \n  👖             /|",
        "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
        "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
        "  😘   😊 \n /👕\/👗\ \n   👖   /|",
        " 😳  😁 \n /|\ /👙\ \n /     / |",
        "😈    /😰\ \n<|\      👙 \n /🍆    / |",
        "😅 \n/(),✊😮 \n /\         _/\\/|",
        "😎 \n/\\_,__😫 \n  //    //       \\",
        "😖 \n/\\_,💦_😋  \n  //         //        \\",
        "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
        "The End 😂...",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])


@ultroid_cmd(pattern="bf$")
async def pressf(f):
    args = f.text.split()
    arg = (f.text.split(" ", 1))[1] if len(args) > 1 else None
    if len(args) == 1:
        r = random.randint(0, 3)
        LOGS.info(r)
        if r == 0:
            await eor(f, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await eor(f, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        else:
            arg = "F"
    if arg is not None:
        out = ""
        F_LENGTHS = [5, 1, 1, 4, 1, 1, 1]
        for line in F_LENGTHS:
            c = max(round(line / len(arg)), 1)
            out += (arg * c) + "\n"
        await eor(f"`" + out + "`")


@ultroid_cmd(pattern="session$")
async def _(event):
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await eor(event, mentions)


@ultroid_cmd(pattern="ftext ([\s\S]*)")
async def payf(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        paytext = input_str
        pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            paytext * 8,
            paytext * 8,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 6,
            paytext * 6,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 2,
        )
    else:
        pay = "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n"

    await eor(event, pay)


@ultroid_cmd(pattern="cat$")
async def hmm(hell):
    reactcat = nekos.textcat()
    await eor(hell, reactcat)


@ultroid_cmd(pattern="why$")
async def hmm(hell):
    whyhell = nekos.why()
    await eor(hell, whyhell)


@ultroid_cmd(pattern="fact$")
async def hmm(hell):
    facthell = nekos.fact()
    await eor(hell, facthell)


