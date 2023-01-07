#Здесь создается бот и хранится его токен

from aiogram import Bot
import logging

from aiogram.dispatcher import Dispatcher

#объект бота
bot = Bot(token='YOUR TOKEN')
#диспетчер
dp = Dispatcher(bot)
#Логирование бота
logging.basicConfig(level=logging.INFO)