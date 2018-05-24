# -*- coding: utf-8 -*-
""" Define BOT's commands """
import logging
from random import randrange
# Configure a logging tool
from typing import Iterable

from telegram.ext import CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def _start(bot, update):
    logging.info('[CMD] start')
    bot.send_message(chat_id=update.message.chat_id,
                     text="I'm the DiceBot, please ask me to do a roll!")


def roll_parser(expression: str) -> Iterable[int]:
    """ Parse and expression into number of dice and die type

    Args:
        expression: follows the prototype `5d10`

    Returns:
        a list of results, one per each die
    """
    try:
        n_dice, die_type = expression.split('d')
        n_dice = int(n_dice)
        die_type = int(die_type)
    except ValueError:
        #return "That's not a dice, try again"
        return []

    return [die_roller(die_type) for _ in range(n_dice)]


def die_roller(die_type: int) -> int:
    """ Rolls a die with

    Args:
        die_type: number of faces of the die

    Returns:
        the result of the die rolling

    Notes:
         counts from 1 to ``type``
    """
    return randrange(1, die_type+1)


def _roll(bot, update, args):
    logging.info(f'[CMD] roll with {args}')
    if not args:
        args = ['1d10']
    result = list(roll_parser(args[0]))
    if result:
        bot.send_message(chat_id=update.message.chat_id,
                     text=f'You roll [{args[0]}]: {result}')
    else: 
        bot.send_message(chat_id=update.message.chat_id,
                     text=f'This is not a valid roll. Try again')

START_HANDLER = CommandHandler('start', _start)
ROLL_HANDLER = CommandHandler('roll', 
_roll, pass_args=True)


def get_all_handlers():
    return [START_HANDLER, ROLL_HANDLER]
