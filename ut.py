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

start_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Старт")]],resize_keyboard=True)
choice_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Видик")]],resize_keyboard=True)



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=start_kb)

@dp.message()
async def handle_messages(message: types.Message):
    if message.text == "Старт":
        await message.answer("Старт", reply_markup=choice_kb)

    elif message.text == "Видик":
        await message.answer('https://www.youtube.com/watch?v=Pt0DktW4rGQ')

# ==== ЗАПУСК ====
async def main():
    print('Бот запущен...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
