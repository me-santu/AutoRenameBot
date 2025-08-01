import logging, os
from pyrogram import Client, filters
from bot.handlers import start_handler, rename_handler

logging.basicConfig(level=logging.INFO)

app = Client(
    "AutoRenameBOT",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await start_handler(client, message)

@app.on_message(filters.document | filters.video | filters.audio)
async def rename_file(client, message):
    await rename_handler(client, message)

print("✅ AutoRenameBOT is running...")
app.run()
