import os, shutil
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot.auto_name import auto_detect_name
from bot.ai_watermark import add_watermark
from bot.utils.db import save_file

# ✅ Start message
async def start_handler(client, message: Message):
    await message.reply_text("🤖 Welcome to Advanced AutoRenameBOT!\n\nSend any file to rename with AI.")

# ✅ File receive and show buttons
async def file_receive_handler(client, message: Message):
    file_path = await message.download()
    await message.reply_text(
        "📂 File received!\nChoose an option:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🤖 Auto Rename", callback_data=f"auto|{file_path}")],
            [InlineKeyboardButton("✍️ New Rename", callback_data=f"custom|{file_path}")]
        ])
    )

# ✅ Callback handler for buttons
async def button_callback_handler(client, query: CallbackQuery):
    action, file_path = query.data.split("|", 1)

    if action == "auto":
        new_name = auto_detect_name(file_path)
        await process_rename(query, file_path, new_name)

    elif action == "custom":
        await query.message.reply_text("✍️ Send me the new name for the file:")

        @client.on_message()
        async def get_new_name(c, msg: Message):
            if msg.reply_to_message and msg.reply_to_message.message_id == query.message.message_id:
                new_name = msg.text
                await process_rename(query, file_path, new_name)

# ✅ Rename + Watermark + Send Back
async def process_rename(query, file_path, new_name):
    ext = os.path.splitext(file_path)[1]
    final_name = f"{new_name}{ext}"
    new_path = os.path.join(os.getcwd(), final_name)
    shutil.move(file_path, new_path)

    wm_file = add_watermark(new_path)
    save_file(query.from_user.id, final_name)

    await query.message.reply_document(wm_file, caption=f"✅ Renamed to {final_name}")
