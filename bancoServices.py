# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, ConversationHandler, RegexHandler, MessageHandler
import os
from bancoDB import DBHelper
from telegram import ReplyKeyboardMarkup
import bancoFilter

OPERATIONS = 0
ADD_BALANCE = 1
def services(bot, update):
    reply_keyboard = [["Tansferencias"], ["Add fondos"]]
    update.message.reply_text("¿Que deseas hacer?", reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return OPERATIONS

def transfer(bot, update):
    pass

def cancel(bot, update):
    pass

def add_balance(bot, update):
    update.message.reply_text("¿Cuanto vas a añadir?")
    return ADD_BALANCE

def add_balance_logic(bot, update):
    update.message.reply_text("Hi")

service_handler = ConversationHandler(
    entry_points=[MessageHandler(bancoFilter.filter_service, services)],

    states={
        OPERATIONS:[MessageHandler(bancoFilter.filter_transfer, transfer), MessageHandler(bancoFilter.filter_add_balance, add_balance)],
        ADD_BALANCE:[MessageHandler(bancoFilter.filter_number, add_balance_logic)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)