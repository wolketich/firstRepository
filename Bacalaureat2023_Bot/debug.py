# main.py
import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

subjects = ["L Romana", "Matematica", "Limba Engleza", "Fizica", "Informatica", "Biologia", "Chimia", "Geografia", "Istoria"]
years = ["Anul 2017", "Anul 2018", "Anul 2019", "Anul 2020", "Anul 2021", "Anul 2022", "Anul 2023"]
sessions = ["Sesiunea de baza", "Sesiunea repetata", "Pretestare", "Teste pentru exersare"]

def get_pdf_file(category, year, session):
    # Convert category and session to a format suitable for the file path
    year_path = year.lower().replace(' ', '_')
    category_path = category.lower().replace(' ', '_')
    session_path = session.lower().replace(' ', '_')
    
    # Build the file path
    file_path = os.path.join('pdfs', year_path, category_path, session_path + '.pdf')

    return file_path

async def send_pdf(chat_id, category, year, session):
    pdf_file = get_pdf_file(category, year, session)
    with open(pdf_file, 'rb') as f:
        await bot.send_document(chat_id, f, caption=f' ')

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(text=subject, callback_data=f'subject:{subject}') for subject in subjects]
    keyboard_markup.add(*buttons)
    await message.answer("Alegeți discplina:", reply_markup=keyboard_markup)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('subject'))
async def process_callback_subject(callback_query: types.CallbackQuery):
    _, subject = callback_query.data.split(':')
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(text=year, callback_data=f'year:{subject}:{year}') for year in years]
    keyboard_markup.add(*buttons)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Disciplina selectată: {subject}\nSelectați anul:', reply_markup=keyboard_markup)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('year'))
async def process_callback_year(callback_query: types.CallbackQuery):
    _, subject, year = callback_query.data.split(':')
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=session, callback_data=f'session:{subject}:{year}:{session}') for session in sessions]
    keyboard_markup.add(*buttons)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Anul selectat: {year}\nSelectați sesiunea:', reply_markup=keyboard_markup)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('session'))
async def process_callback_session(callback_query: types.CallbackQuery):
    _, subject, year, session = callback_query.data.split(':')
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'<b><code>{subject} - {year} - {session}</code></b>', parse_mode='HTML')
    
    # Send PDF
    await send_pdf(callback_query.from_user.id, subject, year, session)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
