import controller as con
from os import system

import user_interface as ui
import loger as log
import breaking_data as bd
import rational_math as rm
import complex_math as cm
from controller import cancel, number, rac, komp, repeat_or_end_calc, give_word, start, unknown

import logging

from config import TOKEN

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    Handler
)

system('cls')

# Определяем константы этапов разговора
NUMBER, RATI, COMP, REPEAT_OR_END_CALC = range(4)

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            NUMBER: [MessageHandler(Filters.regex('^(Рациональные|Комплексные)$'), number)],
            RATI: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, rac)],
            COMP:
                [CommandHandler('cancel', cancel), MessageHandler(Filters.text, komp)],
            REPEAT_OR_END_CALC:
                [MessageHandler(Filters.regex('^(Выход|Продолжить)$'), repeat_or_end_calc)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    message_handler = MessageHandler(Filters.text, give_word)
    unknown_handler = MessageHandler(Filters.command, unknown)

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(unknown_handler)
    dispatcher.add_handler(message_handler)

    # Запуск бота
    log.log_data('|' + '-' * 10 + "Сервер старт" + '-' * 10 + '|')
    updater.start_polling()
    updater.idle()
    log.log_data('|' + '-' * 10 + "Сервер стоп" + '-' * 10 + '|' + '\n\n')
