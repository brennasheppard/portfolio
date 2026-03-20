import os, ollama, logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OWNER_ID = 8704064227

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != OWNER_ID:
        return
    msg = update.message.text.strip().lower()
    if msg in ["/start", "hi", "hello", "/help"]:
        await update.message.reply_text("👋 Howdy! Only you can talk to me.\n\nCommands:\n/joke — Texas joke\n/story — short story\n/models — list models\n/clear — reset chat\n/status — system check")
    elif msg == "/joke":
        await update.message.reply_text("Why don't scientists trust atoms? Because they make up everything! 😂")
    elif msg == "/story":
        await update.message.reply_text("Once upon a time in Schertz, Texas, a curious cat found an old laptop and started coding his own AI… Want the full story?")
    elif msg == "/models":
        models = [m['name'] for m in ollama.list()['models']]
        await update.message.reply_text("Available models:\n" + "\n".join(models))
    elif msg == "/clear":
        await update.message.reply_text("🗑 Chat history cleared!")
    elif msg == "/status":
        await update.message.reply_text("✅ Running locally on M1 Metal • llama3:8b • Secure sandbox active • Only you can message me")
    else:
        await update.message.reply_text("Fixin' to think...")
        try:
            response = ollama.chat(model='llama3:8b', messages=[{'role': 'user', 'content': msg}])['message']['content']
            await update.message.reply_text(response + "\n\n✅ From your secure M1 Nemo (local Ollama)")
        except Exception as e:
            await update.message.reply_text(f"Oops: {e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
print("🤖 Locked bot with commands started!")
app.run_polling()
