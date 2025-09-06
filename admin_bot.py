import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile 

from secret import secrets


# ==== НАСТРОЙКИ ====
TELEGRAM_TOKEN = secrets['BOT_API_TOKEN']

# Создаём экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

async def daily_message():
    while True:
        now = datetime.now()
        target = datetime.combine(now.date(), datetime.strptime("21:50", "%H:%M").time())

        if target < now:
            target += timedelta(days=1)

        delay = (target - now).total_seconds()
        await asyncio.sleep(delay)

        await bot.send_message(CHAT_ID, "Выходим на поверку")


# ==== ЗАПУСК ====
async def main():
    print('Бот запущен...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
