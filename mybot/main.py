#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import os

from telegram.ext import Updater, CommandHandler

START = 'start'


def get_token() -> str:
    """Retrieve token form environment variable"""
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise Exception(f"BOT_TOKEN environment variable not found.")
    logging.debug(f"Retrieved token '{token}'")
    return token


def bot_start_handler(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soy un bot, háblame por favor!")


def connect_handlers(updater: object):
    updater.dispatcher.add_handler(CommandHandler(START, bot_start_handler))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info("Starting up telegram bot...")

    # Create updater object
    updater = Updater(token=get_token(), use_context=True)

    # connect handlers
    connect_handlers(updater)

    # main loop
    updater.start_polling()

