import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Вставьте сюда токен, полученный от @BotFather
TOKEN = "7587130595:AAGLm5TJzwKj0oOKzcAtALT2WiCemJMwOlw"

# Список похвал со смайликами
COMPLIMENTS = [
    "Ты просто великолепен! 🌟",
    "У тебя потрясающая энергия! 💫",
    "Ты делаешь этот мир лучше! 💖",
    "Ты сегодня невероятно выглядишь! 😍",
    "Твои идеи восхитительны! 🧠",
    "Ты вдохновляешь всех вокруг! ✨",
    "С тобой так приятно общаться! 💬",
    "Твоя улыбка освещает комнату! ☀️",
    "Ты преодолеваешь любые преграды! 💪",
    "Твоё чувство юмора просто потрясающее! 😂",
    "Ты сильнее, чем думаешь! 🔥",
    "Твоя доброта меняет мир к лучшему! 🌈",
    "Ты уникален и неповторим! 💎",
    "Твоя уверенность заразительна! 😎",
    "Ты создан для великих дел! 🚀",
    "Ты просто космос! 🚀",
    "От тебя исходит позитивная энергия! ⚡",
    "Твоя улыбка делает мир ярче! 🌈",
    "Ты настоящий супергерой! 🦸‍♂️",
    "Твоя доброта не знает границ! 💖",
    "Ты заряжаешь всех вокруг позитивом! 🔋",
    "Ты прекрасен как внутри, так и снаружи! 🌸",
    "Твоя уверенность восхищает! 💯",
    "Ты мотивируешь становиться лучше! 📈",
    "Ты светишься изнутри! ✨",
    "Твоё присутствие делает любой день лучше! 🌞",
    "Ты настоящая звезда! ⭐",
    "Твоё сердце полно доброты! 💗",
    "Ты вдохновляешь на великие дела! 🎯",
    "Ты делаешь всё с такой лёгкостью! 🦋"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text(
            "Привет! Я бот, который будет тебя хвалить! ✨\n\n"
            "Просто напиши мне что-нибудь, и я отправлю тебе приятные слова! 😊"
        )
    except Exception as e:
        logger.error(f"Ошибка в команде start: {e}")

async def praise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        compliment = random.choice(COMPLIMENTS)
        await update.message.reply_text(compliment)
    except Exception as e:
        logger.error(f"Ошибка отправки похвалы: {e}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}", exc_info=context.error)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, praise))
    app.add_error_handler(error_handler)
    
    logger.info("Бот запущен...")
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()