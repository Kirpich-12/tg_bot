cd = 'pip install python-telegram-bot, pyTelegramBotAPI,aiogram'

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from secret import secrets


# ==== НАСТРОЙКИ ====
TELEGRAM_TOKEN = secrets['BOT_API_TOKEN']

# Создаём экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я простой бот на aiogram 🤖")

# Обработчик любого текстового сообщения
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

# ==== ЗАПУСК ====
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
