from pyrogram.types import Message
from bot.auto_name import auto_detect_name
from bot.ai_watermark import add_watermark
from bot.utils.db import save_file

async def start_handler(client, message: Message):
    await message.reply_text("🤖 Welcome to Advanced AutoRenameBOT!\nSend any file to rename & watermark automatically.")

async def rename_handler(client, message: Message):
    file = await message.download()
    new_name = auto_detect_name(file)
    watermarked_file = add_watermark(file)
    save_file(message.from_user.id, new_name)
    await message.reply_document(watermarked_file, caption=f"✅ Renamed to {new_name}")
