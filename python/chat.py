from asyncore import dispatcher
import imp
from turtle import update
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_html('salom   siz hozir oddiy sinov botidasiz')
    
def a(update, context):
    update.message.reply_html('bu bot oddiygina sinov boti')

def main():
    updater =Updater('5350196224:AAHk9rxn3ePUfSAglkLHF8QVXDPbVUX5IMc',use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start',start))

    dispatcher.add_handler(CommandHandler('kimsan',a))





    updater.start_polling()
    updater.idle()
main()