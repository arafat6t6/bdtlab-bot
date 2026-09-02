import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📋 Available Tasks", callback_data="tasks"),
            InlineKeyboardButton("💰 My Balance", callback_data="balance"),
        ],
        [
            InlineKeyboardButton("📤 Submit Proof", callback_data="proof"),
            InlineKeyboardButton("💳 Withdraw", callback_data="withdraw"),
        ],
        [
            InlineKeyboardButton("👤 My Profile", callback_data="profile"),
            InlineKeyboardButton("📢 Official Channel", url="https://t.me/YOUR_CHANNEL"),
        ],
        [
            InlineKeyboardButton("ℹ️ Help & Support", callback_data="help"),
        ],
    ]

    message = """╔══════════════════════════╗
║      ⚡ BDTLAB ⚡         ║
║    MICRO TASK PLATFORM   ║
╚══════════════════════════╝

🔥 Welcome to BDTLAB!

💎 Complete tasks and earn rewards.
👇 Choose an option below:"""

    await update.message.reply_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "tasks": "📋 Available Tasks\n\nএখনো কোনো Task যোগ করা হয়নি।",
        "balance": "💰 My Balance\n\nBalance: ৳0.00",
        "proof": "📤 Submit Proof\n\nকাজ সম্পন্ন করার পর এখানে Proof জমা দিতে পারবেন।",
        "withdraw": "💳 Withdraw\n\nMinimum withdrawal পরে সেট করা হবে।",
        "profile": f"👤 My Profile\n\nTelegram ID: {query.from_user.id}",
        "help": "ℹ️ Help & Support\n\nBDTLAB Support-এর সাথে যোগাযোগ করুন।",
    }

    await query.edit_message_text(
        responses.get(query.data, "⚡ BDTLAB"),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Main Menu", callback_data="home")]
        ])
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start_from_button(query)


async def start_from_button(query):
    keyboard = [
        [
            InlineKeyboardButton("📋 Available Tasks", callback_data="tasks"),
            InlineKeyboardButton("💰 My Balance", callback_data="balance"),
        ],
        [
            InlineKeyboardButton("📤 Submit Proof", callback_data="proof"),
            InlineKeyboardButton("💳 Withdraw", callback_data="withdraw"),
        ],
        [
            InlineKeyboardButton("👤 My Profile", callback_data="profile"),
            InlineKeyboardButton("📢 Official Channel", url="https://t.me/YOUR_CHANNEL"),
        ],
        [
            InlineKeyboardButton("ℹ️ Help & Support", callback_data="help"),
        ],
    ]

    message = """╔══════════════════════════╗
║      ⚡ BDTLAB ⚡         ║
║    MICRO TASK PLATFORM   ║
╚══════════════════════════╝

🔥 Welcome to BDTLAB!

💎 Complete tasks and earn rewards.
👇 Choose an option below:"""

    await query.edit_message_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(home, pattern="^home$"))
    app.add_handler(CallbackQueryHandler(buttons))

    print("BDTLAB Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
