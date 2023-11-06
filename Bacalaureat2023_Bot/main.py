# main.py
import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from config import TOKEN, PAYMENT_API

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

subjects = ["L Romana", "Matematica", "L Engleza", "Fizica", "Informatica", "Biologia", "Chimia", "Geografia", "Istoria"]
years = ["Anul 2017", "Anul 2018", "Anul 2019", "Anul 2020", "Anul 2021", "Anul 2022", "Anul 2023"]
sessions = ["Sesiunea de baza", "Sesiunea repetata", "Pretestare", "Teste pentru exersare"]

help_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#Buttons
button_main_menu = types.KeyboardButton("Main Menu", callback_data="main_menu")
button_support = types.KeyboardButton("Support @", callback_data="support")
button_support_bac = types.KeyboardButton("Support @bac_support", callback_data="support_bac")

help_markup.add(button_main_menu, button_support, button_support_bac)

@dp.message_handler(lambda message: message.text == 'Main Menu')
async def handle_support_message(message: types.Message):
        # handle main menu button press
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        buttons = [InlineKeyboardButton(text=subject, callback_data=f'subject:{subject}') for subject in subjects]
        keyboard_markup.add(*buttons)
        await message.answer("Alegeți discplina:", reply_markup=keyboard_markup)

@dp.message_handler(lambda message: message.text == 'Support @')
async def handle_support_message(message: types.Message):
        # handle support @ button press
        support = (
        "<b>Support @bac_support!</b>\n"
        "<i>Ați întămpinat greutăți în utilizara botului?</i>\n\n"
        "<u>Cum să obțineti ajuor:</u>\n"
        "Vă rog transmiteți un mesaj privat la "
        "<a href='https://t.me/bac_support'>@bac_support</a> "
        "pentru a primi o soluție cât mai curând."
    )
        await message.answer(support, parse_mode="HTML", reply_markup=help_markup)

@dp.message_handler(lambda message: message.text == 'Support @bac_support')
async def handle_support_message(message: types.Message):
        support_bac = (
        "<b>Support @bac_support!</b>\n"
        "<i>Ați întămpinat greutăți în utilizara botului?</i>\n\n"
        "<u>Cum să obțineti ajuor:</u>\n"
        "Vă rog transmiteți un mesaj privat la "
        "<a href='https://t.me/bac_support'>@bac_support</a> "
        "sau pe poșta electronică "
        "<a href='mailto:support@aee.edu.md'>support@aee.edu.md</a> "
        "pentru a primi o soluție cât mai curând."
    )
        await message.answer(support_bac, parse_mode="HTML", reply_markup=help_markup)

async def send_access_denied_message(chat_id):
    access_denied_message = (
        "<b>Acces Interzis!</b>\n"
        "<i>Ați încercat să accesați o zonă restricționată.</i>\n\n"
        "<u>Cum să obțineti acces:</u>\n"
        "Prin sistema de plată integrată, utilizând: /payment.\n"
        "Ori vă rog transmiteți un mesaj privat la "
        "<a href='https://t.me/bac_support'>@bac_support</a> "
        "pentru a primi acces la versiunile private ale examenelor."
    )
    await bot.send_message(chat_id, access_denied_message, parse_mode="HTML")


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

@dp.message_handler(commands=['menu'])
async def send_welcome(message: types.Message):
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(text=subject, callback_data=f'subject:{subject}') for subject in subjects]
    keyboard_markup.add(*buttons)
    await message.answer("Alegeți discplina:", reply_markup=keyboard_markup)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    help_message = (
        "<b>Ajutor!</b>\n"
        "<i>Lista de comenzi:</i>\n\n"
        "Pentru a utiliza bot-ul, utilizați /menu.\n"
        "Pentru ajutor, utilizați /help.\n"
        "Pentru a restarta botul, utilizați /start.\n"
        "<b>Support: @bac_support</b>"
    )
    help_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    await message.answer(help_message, parse_mode="HTML", reply_markup=help_markup)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    help_message = (
        "<b>Ajutor!</b>\n"
        "<i>Ați întămpinat greutăți în utilizara botului?</i>\n\n"
        "<u>Cum să obțineti ajuor:</u>\n"
        "Vă rog transmiteți un mesaj privat la "
        "<a href='https://t.me/bac_support'>@bac_support</a> "
        "pentru a primi o soluție cât mai curând."
    )

    await message.answer(help_message, parse_mode="HTML", reply_markup=help_markup)

@dp.message_handler(commands=['payment'])
async def handlePayment(message: types.Message):
    await bot.send_invoice(message.chat.id, 
                           'Achiziționarea accesului la material privat.', 
                           'Sesiunea de bază la toate disciplinele ale anului de examinare 2023. După achitare, veți primi acces la secțiunea Anul 2023, sesiunea de bază și pe viitor sesiunea repetată.', 
                           'invoice', 
                           PAYMENT_API, 
                           'EUR', 
                           [types.LabeledPrice('Achiziționarea cursului', 350 * 100)],
                           photo_url="https://phonline.ro/wp-content/uploads/2023/04/Screenshot_20230420_162818.jpg",
                           need_shipping_address=False)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def succes(message: types.Message):
     await message.answer(f'Succes: {message.successful_payment.order_info}')

@dp.message_handler()
async def handle_message(message: types.Message):
    # Handle any other message after starting point
    await message.answer("Vă rog utilizați comanda /menu pentru a restarta botul sau /help pentru ajutor.")    

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
    sesiunea_msg = await bot.send_message(callback_query.from_user.id, f'Anul selectat: {year}\nSelectați sesiunea:', reply_markup=keyboard_markup)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('session'))
async def process_callback_session(callback_query: types.CallbackQuery):
    _, subject, year, session = callback_query.data.split(':')
    await bot.answer_callback_query(callback_query.id)

    if (year == "Anul 2023"):
        # Throw acces error
        await send_access_denied_message(callback_query.from_user.id)
    else:
        # Send PDF
        await bot.send_message(callback_query.from_user.id, f'<b><code>{subject} - {year} - {session}</code></b>', parse_mode='HTML')
        try:    
            await send_pdf(callback_query.from_user.id, subject, year, session)
        except:
            await send_access_denied_message(callback_query.from_user.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
