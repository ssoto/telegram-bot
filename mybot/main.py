#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import os

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

START = 'start'
HELP = 'help'
AYUDA = 'ayuda'


def get_token() -> str:
    """Retrieve token form environment variable"""
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise Exception(f"BOT_TOKEN environment variable not found.")
    logging.debug(f"Retrieved token '{token}'")
    return token


def start_handler(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soy un bot, háblame por favor!")


def help_handler(updater: object, context: object):
    context.bot.send_message(
        chat_id=updater.effective_chat.id,
        text="Para usarme prueba a citarme al principio de un mensaje")


def echo_handler(updater: object, context: object):
    context.bot.send_message(
        chat_id=updater.effective_chat.id,
        text=updater.message.text
    )


def connect_handlers(dispatcher: object):
    dispatcher.add_handler(
        CommandHandler(START, start_handler))

    dispatcher.add_handler(
        CommandHandler(HELP, help_handler))

    echohandler = MessageHandler(Filters.text & (~Filters.command), echo_handler)
    dispatcher.add_handler(echohandler)


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info("Starting up telegram bot...")

    # Create updater object
    updater = Updater(token=get_token(), use_context=True)

    # connect handlers
    connect_handlers(updater.dispatcher)

    # main loop
    updater.start_polling()


if __name__ == "__main__":
    main()
