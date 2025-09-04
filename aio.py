

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
choice_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Их"), KeyboardButton(text="Нас"),KeyboardButton(text="САС"), KeyboardButton(text="АУДИО"), KeyboardButton(text="Пробив", request_location=True)]],resize_keyboard=True)



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=start_kb)

@dp.message()
async def handle_messages(message: types.Message):
    if message.text == "Старт":
        await message.answer("Кого ты выберешь?", reply_markup=choice_kb)

    elif message.text == "Их":
        photo_url = "https://www.meme-arsenal.com/memes/8a7b3d9be549530aab5a3a14b6bff56e.jpg"
        await message.answer_photo(photo_url, caption="Ты выбрал: Их")

    elif message.text == "Нас":
        photo_url = "https://memchik.ru//images/memes/596409a4b1c7e3235d140ce1.jpg"
        await message.answer_photo(photo_url, caption="Ты выбрал: Нас")
    
    elif message.text == "САС":
        video_url = "http://cache-rmg.servicecdn.ru/rmg/streaming_rutv/video/Hanna_Artik__KakVPervyiRaz_9.mp4"
        await message.reply_video(video=video_url, caption="СААААС")

    elif message.text == "АУДИО":
        audio_file = FSInputFile("rick.mp3", "rick.mp3")
        await bot.send_audio(chat_id=message.chat.id, audio=audio_file, title="Название трека", performer="Исполнитель", caption="+")
    
    elif message.text == "Пробив":
            await message.answer("Дай данные")

    
    

    else:
        await message.answer(f"Ты написал: {message.text}")


# ==== ЗАПУСК ====
async def main():
    print('Бот запущен...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

