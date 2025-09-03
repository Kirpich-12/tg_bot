import telebot

from secret import secrets


# ==== НАСТРОЙКИ ====
TELEGRAM_TOKEN = secrets['BOT_API_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот на telebot")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

# ==== ЗАПУСК ====
def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
