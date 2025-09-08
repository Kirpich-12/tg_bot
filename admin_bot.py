import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile 
import schedule

from secret import secrets

# ==== НАСТРОЙКИ ====
TELEGRAM_TOKEN = secrets['BOT_API_TOKEN']
CHAT_ID = secrets['CHAT_ID']   # добавлено


# Создаём экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

def daily_message():
    bot.send_message(chat_id=CHAT_ID,text='КУку')
    
# ==== ЗАПУСК ====
schedule.every().day.at('11:33').do(daily_message())
async def main():
    print('Бот запущен...') 
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())