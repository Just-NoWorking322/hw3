import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token


bot = Bot(token=token)
dp = Dispatcher()

start_buttons = [
    [KeyboardButton(text="Geeks направления"), KeyboardButton(text="Contacts")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

start_buttons_icg = [
    [KeyboardButton(text="BACK_END"), KeyboardButton(text="FRONT_END")],
    [KeyboardButton(text="UI_UX"), KeyboardButton(text="ANDROID")],
]
start_keyboard_inboard = ReplyKeyboardMarkup(keyboard=start_buttons_icg, resize_keyboard=True)

start_buttons_1 = [
    [KeyboardButton(text="Geeks направления"), KeyboardButton(text="Contacts")],
    [KeyboardButton(text="TELEGRAMM"), KeyboardButton(text="INSTAGRAM")]
]
start_keyboard_contacts = ReplyKeyboardMarkup(keyboard=start_buttons_1, resize_keyboard=True)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, ВЫБЕРИТЕ ДЕЙТСВИЕ", reply_markup=start_keyboard)

@dp.message(F.text == "Geeks направления")
async def napravlenia(message: types.Message):
    await message.answer("Вот наши напрваления:",reply_markup=start_keyboard_inboard)
    
@dp.message(F.text == "Contacts")
async def napravlenia(message: types.Message):
    await message.answer("Связаться с нами можно через:+996 (557) 05 2018, +996 (507) 05 2018, +996 (777) 05 2018", reply_markup=start_keyboard_contacts)
    


@dp.message(F.text == "BACK_END")
async def napravlenia(message: types.Message):
    await message.answer("Backend — это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей.Она включает в себя работу над архитектурой сайта, управление базами данных, обработку запросов от клиентской части, подгрузку и обновление контента, работу с API и многое другое.")

@dp.message(F.text == "FRONT_END")
async def napravlenia(message: types.Message):
    await message.answer("Frontend разработка пользовательского интерфейса, то есть той части сайта или приложения, которую видят посетители страницы. Главная задача фронтенд разработчика — перевести готовый дизайн-макет в код так, чтобы все работало правильно.")
       
@dp.message(F.text == "UI_UX")
async def napravlenia(message: types.Message):
    await message.answer("UX-дизайн (User Experience — «пользовательский опыт») отвечает за то, как интерфейс работает. UI-дизайн (User Interface — «пользовательский интерфейс») отвечает за то, как интерфейс выглядит. Одна часть не может существовать без другой.")
@dp.message(F.text == "ANDROID")
async def napravlenia(message: types.Message):
           await message.answer("Android – операционная система, которая открыта для всех: разработчиков, дизайнеров и производителей устройств. Это означает, что возможность экспериментировать, предлагать революционные идеи и воплощать их в жизнь доступна большому количеству людей.")
           

@dp.message(F.text == "TELEGRAMM")
async def napravlenia(message: types.Message):
    await message.answer("@geeks_osh")

@dp.message(F.text == "INSTAGRAM")
async def napravlenia(message: types.Message):
    await message.answer("@geeks_osh ")
                  
           
async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
