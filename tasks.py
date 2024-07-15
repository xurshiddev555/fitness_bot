
import asyncio
import logging
import smtplib
import ssl
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from sqlalchemy import create_engine, Column, Integer, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import certifi

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = getenv('TELEGRAM_BOT_TOKEN')
SENDER_EMAIL = getenv('SENDER_EMAIL')
EMAIL_PASSWORD = getenv('EMAIL_PASSWORD')
DATABASE_URL = getenv('DATABASE_URL')

bot = Bot(token=TOKEN)
dp = Dispatcher()

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'  # noqa

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)


Base.metadata.create_all(engine, checkfirst=True)

receiver_email = ""
message_content = ""


def send_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Send message", callback_data="send_message")]
    ])


@dp.message(CommandStart())
async def start(message: Message):
    user_data = {
        "tg_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
    }

    existing_user = session.query(User).where(User.tg_id == user_data["tg_id"]).scalar()

    if not existing_user:
        try:
            user = User(**user_data)
            session.merge(user)
            session.commit()
            await message.answer(f'Hello {message.from_user.first_name}, please enter the email address.')
        except Exception as e:
            logging.error(f"Failed to save user: {e}")
            await message.answer('Failed to save user data. Please try again later.')
    else:
        await message.answer(f'Hello {message.from_user.first_name}, please enter the email address.')


@dp.message(F.text.endswith(".com"))
async def get_email(message: Message):
    global receiver_email
    receiver_email = message.text
    await message.answer('Please enter the message content.')


@dp.message(lambda message: message.text and not message.text.endswith(".com"))
async def get_message_content(message: Message):
    global message_content
    message_content = message.text
    await message.answer('Confirm sending email by clicking the button below.', reply_markup=send_button())


@dp.callback_query(lambda callback_query: callback_query.data == 'send_message')
async def on_send_button(callback: CallbackQuery):
    await send_email(callback.message)
    await callback.answer()


async def send_email(message: Message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, f"sunatillo: Hi there\n\n{message_content}")  # noqa
        await message.answer('Email sent successfully.')
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        await message.answer('Failed to send email. Please try again.')


async def main() -> None:
    while True:
        try:
            await dp.start_polling(bot)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            await asyncio.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
