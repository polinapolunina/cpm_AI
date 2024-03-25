import asyncio

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

from states import States

from model.predictor import model

from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")


router = Router()

@router.message(CommandStart())
async def welcome(msg: Message, state: FSMContext):
    await state.set_state(States.work)
    await msg.reply(
        "Привет! Я бот кодиим). Напиши что-нибудь...",
        # reply_markup=ReplyKeyboardMarkup(
            # keyboard=[[KeyboardButton(text="Круто!")]])
    )


@router.message(States.work)
async def generate(msg: Message, state: FSMContext):
    await state.set_state(States.work)
    model_answer = model(msg.text)

    await msg.reply("Ответ:\n" + model_answer)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
