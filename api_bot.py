
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
import requests
from datetime import datetime
import os
import pandas as pd
import functools


from secret import secrets

url1 = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={secrets['API1_TOKEN']}'
url2 = 'https://catfact.ninja/fact'
url3 = 'https://api.agify.io/?name=vadim'


def logging(func):
    if asyncio.iscoroutinefunction(func):
        # если функция асинхронная
        @functools.wraps(func)
        async def wrapper(message, *args, **kwargs):
            result = await func(message, *args, **kwargs)

            logs = 'log.csv'
            log_entry = {
                "id": 0,
                "id users": message.from_user.id,
                "button": message.text,
                "date": str(datetime.now().date()),
                "time": str(datetime.now().time()),
                "answer": result if isinstance(result, str) else ""
            }

            if os.path.isfile(logs):
                file_df = pd.read_csv(logs)
                log_entry["id"] = len(file_df)
                df = pd.DataFrame([log_entry])
                df.to_csv(logs, header=False, index=False, mode="a")
            else:
                df = pd.DataFrame([log_entry])
                df.to_csv(logs, index=False)

            return result
        return wrapper
    else:
        # синхронные функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper



def bit(url:str):
    response = requests.get(url)
    data = response.json()
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']

def cats(url:str):
    response = requests.get(url)
    return response.json()['fact']

def name(url:str):
    response = requests.get(url)
    data  = response.json()
    return f'{data['name']} approximate age: {data['age']}'


# ==== НАСТРОЙКИ ====
TELEGRAM_TOKEN = secrets['BOT_API_TOKEN']

# Создаём экземпляры бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

start_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Старт")]],resize_keyboard=True)
choice_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Биток"),KeyboardButton(text="Факт про котов"), KeyboardButton(text="Вадим")]],resize_keyboard=True)

@logging
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=start_kb)

@logging
@dp.message()
async def handle_messages(message: types.Message):
    if message.text == "Старт":
        await message.answer("Кого ты выберешь?", reply_markup=choice_kb)
    elif message.text == 'Биток':
        await message.answer(f'Bitcoin course {bit(url1)}')
    elif message.text == 'Факт про котов':
        await message.answer(f'Fan fact about cats{cats(url2)}')
    elif message.text == 'Вадим':
        await message.answer(name(url3))


# ==== ЗАПУСК ====
async def main():
    print('Бот запущен...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
