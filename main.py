import asyncio
import datetime
import logging
import os

import pytz
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.types import InputMediaPhoto

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.parser.html").setLevel(logging.ERROR)
logging.getLogger("pyrogram.session.session").setLevel(logging.ERROR)

TIME_ZONE = "Asia/Kolkata"
BOT_LIST = ["Spl_Levi_Ackerman_Bot", "Spl_Afk_Bot", "Spl_Sticker_Bot", "Spl_String_Session_Bot", "Spl_Post_Bot", "Spl_Mention_Bot"]
CHANNEL_OR_GROUP_ID = -1001401571895
MESSAGE_ID = 3
BOT_ADMIN_IDS = [5868832590, 5232837149]

API_HASH = "2a31b117896c5c7da27c74025aa602b8"
API_ID = 13691707
SESSION_NAME = "BQBiMZkAP_e7w6Jz1zoPb-GJ7rdeRBa1VZVNCLDDmxf5ZKU47ZHkcVERRZnO4DT5ZWIbhVitfWxRkqsOMPLw67SsWG3wfntw9S8B89ZakmsSF_dpZkD_gqs9vLHUuK132rSABUJ63D8h7fjIbymFQ9SO2xwbowelTCOtbSTSUbN8dR4DLAyAqOCuQhFPWAsvuA2hcGB6L_LgLfMtPmd86UkumP_OzP-CBX1bWv49A015T3m4m4Pf2a820Oq0Sd5G1KPXSX_vh7M6nbXNcy_LYQ605VsnX3pJEgmrWx8Ixe5XZWEF4oXlqu4LPqHBrE0xksrQBBupw_3-IAjMtG-25j2WI2TxQQAAAAE35sIdAA"


app = Client("hehe", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_NAME)

logging.warning("Starting ➿➿➿....")


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def main():
    async with app:
        logging.warning("Starting Bot Check Loop ➿....")
        while True:
            logging.warning("Checking...")
            yax = 600
            bg = Image.open("images/bg.jpg")
            bg = changeImageSize(1300, 2000, bg)
            # font = ImageFont.load_default()
            font = ImageFont.truetype("stuff/fonts/arial.ttf", 60)
            xxx_tg = f"📈 | ** Sᴘʟ Nᴇᴛᴡᴏʀᴋ™ Bot Status**"
            for bot in BOT_LIST:
                try:
                    yyy_tg = await app.send_message(bot, "/start")
                    aaa = yyy_tg.message_id
                    await asyncio.sleep(10)
                    zzz_tg = await app.get_history(bot, limit=1)
                    for ccc in zzz_tg:
                        bbb = ccc.message_id
                    if aaa == bbb:
                        logo = Image.open("images/down.jpg")
                        # imgffff = Image.open("temp.png")
                        bg = bg.copy()
                        yax = yax + 175
                        bg.paste(logo, (1000, yax))
                        draw = ImageDraw.Draw(bg)
                        draw.text((200, yax), f"{bot}", (26, 84, 174), font=font)
                        for bot_admin_id in BOT_ADMIN_IDS:
                            try:
                                await app.send_message(
                                    int(bot_admin_id),
                                    f"🚨 **Beep! Beep!! {bot} is down** ❌",
                                )
                            except Exception:
                                pass
                        await app.read_history(bot)
                    else:
                        logo = Image.open("images/up.jpg")
                        # imgffff = Image.open("temp.png")
                        bg = bg.copy()
                        yax = yax + 190
                        bg.paste(logo, (1000, yax))
                        draw = ImageDraw.Draw(bg)
                        # font = ImageFont.truetype("font.ttf", 80)
                        draw.text((200, yax), f"{bot}", (26, 84, 174), font=font)
                        await app.read_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))

            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            xxx_tg += f"\n\n✔️ Last updated on: {last_update} ({TIME_ZONE})\n\n<i>⇋ Updates every 10min - Powered by @SpLBots</i>"
            bg.save("md.jpg")
            await app.edit_message_media(
                CHANNEL_OR_GROUP_ID,
                MESSAGE_ID,
                InputMediaPhoto(media="md.jpg", caption=xxx_tg),
            )
            logging.warning(f"Last checked on: {last_update}")
            await asyncio.sleep(600)
            # await asyncio.sleep(60)


app.run(main())
