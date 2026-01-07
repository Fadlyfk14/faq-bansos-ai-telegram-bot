from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from faq_data import FAQ_DATA
from ai_engine import find_best_answer

BOT_TOKEN = "8560058556:AAHMxRDmJD1faYlwc2DzDqGi_0PbayA4--Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋\nSaya adalah Chatbot FAQ Bansos.\nSilakan ajukan pertanyaan Anda."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    answer = find_best_answer(user_text, FAQ_DATA)

    if answer:
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text(
            "Terima kasih atas pertanyaannya 🙏" \
            "Saat ini informasi tersebut belum tersedia di sistem kami." \
            "Pertanyaan Anda akan kami catat untuk ditindaklanjuti."
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
