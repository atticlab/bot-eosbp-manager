#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
requ - pip install python-telegram-bot
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import subprocess

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
users = open('/opt/BP-manager/scripts/schedule.conf').readline()
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    #Check if user in users list
    if str(update.message.from_user.id) not in users:
        update.message.reply_text('Access Denied!\n')
        return
    #Only run command
    #command_result = subprocess.call("ls -la", shell=True)
    #command with send output result
    message = str()
    #message = "{'delete_chat_photo': False, 'new_chat_photo': [], 'from': {'username': u'edroot', 'first_name': u'Ed', 'last_name': u'Kab', 'is_bot': False, 'language_code': u'ru', 'id': 282627546}, 'text': u'/start', 'caption_entities': [], 'entities': [{'length': 6, 'type': u'bot_command', 'offset': 0}], 'channel_chat_created': False, 'new_chat_members': [], 'supergroup_chat_created': False, 'chat': {'username': u'edroot', 'first_name': u'Ed', 'last_name': u'Kab', 'type': u'private', 'id': 282627546}, 'photo': [], 'date': 1538132869, 'group_chat_created': False, 'message_id': 378}"
    print(message)

    proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    output = proc.stdout.read()
    update.message.reply_text('Result:\n'+ str(output))

def get_schedule(bot, update):
    if str(update.message.from_user.id) not in users:
        update.message.reply_text('Access Denied!\n')
        return
    message = str()
    print(message)
    #cmd = '/opt/EOSmainNet/cleos.sh get schedule | grep atticlab'
    proc = subprocess.Popen('/opt/BP-manager/scripts/schedule.sh', stdout=subprocess.PIPE)
    output = proc.stdout.read()
    update.message.reply_text('Result:\n'+ str(output))

def help(bot, update):
    """Send a message when the command /help is issued."""
    print(update.message.from_user.id)
    update.message.reply_text('Help!')


def messages(bot, update):
    """This the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("691795908:AAHRvJLj_YekHnFX4QijYrO4RV1a0-dK910")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get_schedule", get_schedule))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, messages))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
