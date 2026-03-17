import os
import logging
from logging.handlers import RotatingFileHandler

# ────────────────────────────────────────────────
#               ENVIRONMENT VARIABLES
# ────────────────────────────────────────────────

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# MongoDB connection (must be set in environment variables!)
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "wifeybot")   # change if you want different db name

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

# Auto-delete time in seconds (45 minutes = 2700)
FILE_AUTO_DELETE = int(os.environ.get("FILE_AUTO_DELETE", "2700"))

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Admins list
ADMINS = [OWNER_ID]
try:
    admin_str = os.environ.get("ADMINS", "")
    if admin_str:
        for x in admin_str.split():
            ADMINS.append(int(x))
except ValueError:
    raise Exception("ADMINS environment variable contains invalid integers.")

# Remove duplicates and sort (optional but cleaner)
ADMINS = sorted(set(ADMINS))

# ────────────────────────────────────────────────
#               BOT MESSAGES & SETTINGS
# ────────────────────────────────────────────────

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False").lower() == "true"

DISABLE_CHANNEL_BUTTON = os.environ.get('DISABLE_CHANNEL_BUTTON', "True").lower() == "true"

BOT_STATS_TEXT = "<b>Bot Uptime :</b>\n{uptime}"

USER_REPLY_TEXT = "❌ Don't send me messages directly!\nI'm only a file sharing bot."

START_MSG = os.environ.get(
    "START_MESSAGE",
    "🌸 Welcome to Wifey FanBase™ 🌸\n\n"
    "Your daily dose of exclusive content is here 💕\n"
    "Choose a category to explore 👇"
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {mention}\n\n"
    "<b>You need to join my channel/group to use me.</b>\n"
    "Kindly join the channel first → then come back ❤️"
)

# Logging setup
LOG_FILE_NAME = "filesharingbot.log"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50 * 1024 * 1024,   # 50 MB
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# ────────────────────────────────────────────────
#           DEVELOPER CREDITS (please keep)
# ────────────────────────────────────────────────
# Jishu Developer
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
