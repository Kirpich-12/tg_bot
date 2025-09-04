cd = 'pip install python-telegram-bot, pyTelegramBotAPI,aiogram'

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from secret import secrets


# ==== НАСТРОЙКИ ====
TELEGRAM_TOKEN = secrets['BOT_API_TOKEN']

# Создаём экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()



# Обработчик команды /start

start_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Старт")]],resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=start_kb)

# Обработчик любого текстового сообщения
'''@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")'''

# ==== ЗАПУСК ====
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
