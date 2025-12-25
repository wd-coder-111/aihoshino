# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8419198725:AAGhxLIVGZ2y4lPm8SSn0ieIn-dFRxXpLpU")
APP_ID = int(os.environ.get("APP_ID", "28682747")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "067e7c3e7d263586954424616284896c") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003459220099")) #Your db channel Id
OWNER = os.environ.get("OWNER", "DEMON_LORD_111") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7159454821")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Aihonshino131:jSf1f4gp1dej3Rje@cluster0.6gabptr.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AI")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/X_Contact_Bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/484cd8e280bb072476617-2ae7a000ff7e77166b.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/8fbb98eaa2b260613f292-44f79979fac10228ed.jpg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "linkshortify.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "08fba4aa633f00a1569a3c5ca88bdad1db1e531a")
TUT_VID = os.environ.get("TUT_VID","https://t.me/tutorialwallah/37")
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://graph.org/file/83a8422797b7321589fda-0fafb68695a111f569.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>ᴛʜɪs ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ <a href=https://t.me/cultured_X>ᴄᴜʟᴛᴜʀᴇᴅ x</a>\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ᴡɪᴛʜ ʟᴏᴠᴇ</blockquote></b>"
ABOUT_TXT = "<b><blockquote>\n\n♡\n\n</blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> ɪ ᴀᴍ ᴀɪ ʜᴏsʜɪɴᴏ, ɪ ᴡᴏʀᴋ ғᴏʀ <a href=https://t.me/cultured_X>ᴄᴜʟᴛᴜʀᴇᴅ x</a>\n\nɢᴇᴛ sᴘᴇᴄɪғɪᴄ ʟɪɴᴋ ғʀᴏᴍ ᴛʜᴇʀᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜʀ ᴅᴇsɪʀᴇᴅ ᴄᴏɴᴛᴇɴᴛ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b></blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /premium_users :</b> ʟɪsᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀs
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
<b>›› /count :</b> ᴄᴏᴜɴᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴs
<b>›› /delreq :</b> Rᴇᴍᴏᴠᴇᴅ ʟᴇғᴛᴏᴠᴇʀ ɴᴏɴ-ʀᴇǫᴜᴇsᴛ ᴜsᴇʀs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ <a href=https://t.me/cultured_X>ᴄᴜʟᴛᴜʀᴇᴅ x</a></b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "Demon_Lord_111")
UPI_ID = os.environ.get("UPI_ID", ".")
QR_PIC = os.environ.get("QR_PIC", "https://graph.org/file/484cd8e280bb072476617-2ae7a000ff7e77166b.jpgg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/X_Contact_Bot")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "15 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "49 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "99 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "199 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "499 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
