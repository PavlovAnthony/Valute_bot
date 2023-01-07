# Cюда все функции отправляющие сообщения

from aiogram import types
from bot import bot
async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Посмотреть котировки /quote\n'
                           f'закончить /finish')
    
async def show_quote(quote, message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{quote}\n')

async def end (message: types.Message):
     await bot.send_message(message.from_user.id,
                            f' До свидания, {message.from_user.first_name}!')
    
