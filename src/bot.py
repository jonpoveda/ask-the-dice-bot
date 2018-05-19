# -*- coding: utf-8 -*-
""" Bot module """

import argparse
import commands
import logging

import telegram
from telegram.ext import Updater


def run(updater: Updater):
    """ Connects bot """
    updater.start_polling()


def configure(token: str):
    """ Configures the bot """
    # Configure a logging tool
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    # Load secret token
    bot = telegram.Bot(token=token)
    info = bot.get_me()

    # Configure an updater to receive updates
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Add command handlers
    for handler in commands.get_all_handlers():
        dispatcher.add_handler(handler)

    return updater, info


def main():
    # Parse arguments as parameters
    parser = argparse.ArgumentParser(description='Dataset generator')
    parser.add_argument('token', type=str, help="Bot's API token")
    parser.add_argument('-i', '--info',
                        action='store_true',
                        help='Do not actually run the bot, just configure and '
                             'retrieve information')
    arguments = parser.parse_args()

    # Run bot

    updater, info = configure(arguments.token)

    if arguments.info:
        logging.info(info)
    else:
        logging.debug(info)
        logging.info('[Run] Connecting bot')
        run(updater)


if __name__ == '__main__':
    main()
