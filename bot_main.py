from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram.bot import Bot
from telegram.update import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputFile, InputMediaPhoto
from main import edsr, espcn, fsrcnn, lapSRN
import numpy as np
import cv2
import io
import tensorflow as tf

# Enable logging


TOKEN = "1850588140:AAF3UdOqvU8dTALuN9GUQsN7s15hFsIIafs"

bot = Bot(TOKEN)
updater = Updater(TOKEN)


def start(update: Update, callback):
    bot.send_message(chat_id=update.effective_chat.id,
                     text='Enter the photo you want to upscale')




# User message handler
def handle_text(update: Update, callback):
    keyboard = [
        [InlineKeyboardButton("EDSF", callback_data="EDSF")],
        [InlineKeyboardButton("ESPCN", callback_data="ESPCN")],
        [InlineKeyboardButton("FSRCNN", callback_data="FSRCNN")],
        [InlineKeyboardButton("LapSRN", callback_data="LapSRN")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose the model with which you want to upscale your photo:", reply_markup=reply_markup)


# Define an image handler
def image_handler(update: Update, callback):

    print(2)
    file = bot.getFile(update.message.document.file_id)
    print("file_id: " + str(update.message.photo.file_id))
    file.download('image.jpg')

dispatcher = updater.dispatcher



dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', start))

updater.start_polling()
updater.idle()
