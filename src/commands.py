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


def roll_parser(args: str = '1d10') -> int:
    return randrange(1, 10)


def _roll(bot, update):
    logging.info('[CMD] roll')
    args = '1d10'
    result = roll_parser(args)
    bot.send_message(chat_id=update.message.chat_id,
                     text=f'You roll [{args}]: {result}')


START_HANDLER = CommandHandler('start', _start)
ROLL_HANDLER = CommandHandler('roll', _roll)


def get_all_handlers():
    return [START_HANDLER, ROLL_HANDLER]
