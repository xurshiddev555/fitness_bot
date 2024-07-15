
#---------------------
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from button import main_button, start_button, woman_button, man_button, hafta_button
from dotenv import load_dotenv
from aiogram.fsm.state import StatesGroup, State

dp = Dispatcher()
load_dotenv()
TOKEN = getenv('TOKEN')

class StepState(StatesGroup): # noqa
    main_state = State()
    start_state = State()
    man_state = State()
    woman_state = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, ) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    caption = ("Assalomu alaykum !\n"
               "Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib\nberadi")
    await message.answer_photo(photo='https://telegra.ph/file/5727372f6074274f86a24.png',
                               caption=caption, reply_markup=main_button())


@dp.message(F.text == 'Filial 📍')
async def main_button_handler(message: Message, ) -> None:
    await message.answer_location(latitude=41.304476, longitude=69.253043)


@dp.message(F.text == 'Start ✅')
async def main_button_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Quydagilardan birontasini tanlang 👇🏿", reply_markup=start_button())
    await state.set_state(StepState.start_state)


@dp.message(F.text == 'Admin 👨🏻‍💻')
async def main_button_handler(message: Message) -> None:
    await message.answer('@Dilshod_Absaitov')


@dp.message(StepState.start_state)
async def start_button_handler(message: Message, state: FSMContext) -> None:
    if message.text == 'Woman 🧍‍♀️':
        caption = ('Quydagilarni birontasini tanlang 👇🏿')
        await message.answer_photo(photo='https://telegra.ph/file/269073f2fded85513a6cf.png',
                                   caption=caption, reply_markup=woman_button())
        await state.set_state(StepState.woman_state)

    elif message.text == 'Men 🧍‍♂️':
        caption = ('Quydagilarni birontasini tanlang 👇🏿')
        await message.answer_photo(photo='https://telegra.ph/file/112dbd10688e613d52320.png',
                                   caption=caption, reply_markup=man_button())
        await state.set_state(StepState.man_state)

    elif message.text == '🔙 back':
        await message.answer('back', reply_markup=main_button())
        await state.set_state(StepState.main_state)


@dp.message(StepState.woman_state)
async def woman_button_handler(message: Message, state: FSMContext) -> None:
    if message.text == '🔙 back':
        await message.answer('back', reply_markup=start_button())
        await state.set_state(StepState.start_state)

    elif message.text == '1-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())
    elif message.text == '2-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())
    elif message.text == '3-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())
    elif message.text == '4-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())


@dp.message(StepState.man_state)
async def woman_button_handler(message: Message, state: FSMContext) -> None:
    if message.text == '🔙 back':
        await message.answer('back', reply_markup=start_button())
        await state.set_state(StepState.start_state)

    elif message.text == '1-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())
    elif message.text == '2-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())
    elif message.text == '3-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())
    elif message.text == '4-oy':
        await message.answer('Hafta kunlaridan birontasini tanlang', reply_markup=hafta_button())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
