# Здесь хранятся хендлеры

from aiogram import Dispatcher
import view
from bot import bot
from aiogram import types
import parse

# возможные реакции на команды пользователя


def registred_handlers(dp: Dispatcher):

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await view.greetings(message)

    @dp.message_handler(commands=['quote'])
    async def exchange_command(message):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
        types.InlineKeyboardButton('USD', callback_data='get-USD'),
        types.InlineKeyboardButton('GBP', callback_data='get-GBP')
        )
        keyboard.row(
        types.InlineKeyboardButton('EUR', callback_data='get-EUR'),
        types.InlineKeyboardButton('JPY', callback_data='get-JPY')
        )

        await bot.send_message(
        message.chat.id,
        'Выбери вылюту:',
        reply_markup=keyboard
        )
    @dp.callback_query_handler(lambda call: True)
    async def vote_callback(callback: types.CallbackQuery):
        name_valute=callback.data[4:]
        print(name_valute)
        await bot.answer_callback_query(callback.id)
        await bot.send_message(callback.from_user.id, parse.parse_exchange(name_valute))
        
        
