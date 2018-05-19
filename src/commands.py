# -*- coding: utf-8 -*-
""" Define BOT's commands """
import logging
from random import randrange

from telegram.ext import CommandHandler

# Configure a logging tool
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def _start(bot, update):
    logging.info('[CMD] start')
    bot.send_message(chat_id=update.message.chat_id,
                     text="I'm the DiceBot, please ask me to do a roll!")


START_HANDLER = CommandHandler('start', _start)


def get_all_handlers():
    return [START_HANDLER]
