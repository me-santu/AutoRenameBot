import os
from os import environ

# 🔥 Telegram API Credentials
API_ID = int(environ.get("API_ID", "123456"))        # (Your Telegram API ID)
API_HASH = environ.get("API_HASH", "your_api_hash")  # (Your Telegram API Hash)
BOT_TOKEN = environ.get("BOT_TOKEN", "")             # (BotFather Token)

# 🔥 Owner & Access
OWNER_ID = int(environ.get("OWNER_ID", "123456789")) # (Bot Owner Telegram ID)

# 🔥 Optional Configs
MONGO_URI = environ.get("MONGO_URI", "")             # (MongoDB URI - Optional)
OPENAI_API_KEY = environ.get("OPENAI_API_KEY", "")   # (OpenAI API Key - Optional)

# 🔥 Allowed Users List
TOTAL_USER = os.environ.get('TOTAL_USERS', str(OWNER_ID)).split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

# 🔥 Auth Users List
AUTH_USER = os.environ.get('AUTH_USERS', str(OWNER_ID)).split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]

# 🔥 Ensure Owner is in Auth List
if int(OWNER_ID) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER_ID))
