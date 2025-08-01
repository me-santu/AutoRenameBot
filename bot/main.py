import logging
from pyrogram import Client, filters
from bot.handlers import start_handler, file_receive_handler, button_callback_handler
from bot.vars import API_ID, API_HASH, BOT_TOKEN   # 🔥 vars.py import

logging.basicConfig(level=logging.INFO)

# ✅ Client Initialize
app = Client(
    "AutoRenameBOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ✅ /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await start_handler(client, message)

# ✅ File receive handler
@app.on_message(filters.document | filters.video | filters.audio)
async def file_receive(client, message):
    await file_receive_handler(client, message)

# ✅ Inline button callback
@app.on_callback_query()
async def callback_handler(client, callback_query):
    await button_callback_handler(client, callback_query)

print("✅ AutoRenameBOT is running...")
app.run()
