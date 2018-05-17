# -*- coding: utf-8 -*-
import argparse
import logging

import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater


def run(token: str):
    # Load secret token
    bot = telegram.Bot(token=token)
    print(bot.get_me())

    # Configure an updater to receive updates
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Configure a logging tool
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    # Define commands
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="I'm the DiceBot, please ask me to do a roll!")

    # Add command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Connect bot
    updater.start_polling()


def main():
    # Parse arguments as parameters
    parser = argparse.ArgumentParser(description='Dataset generator')
    parser.add_argument('token', type=str, help="Bot's API token")
    arguments = parser.parse_args()

    # Run bot
    run(arguments.token)


if __name__ == '__main__':
    main()
