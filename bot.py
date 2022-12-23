from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import main
import detect
import matplotlib.pyplot as plt
import cv2
import os
import processing
import detect

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="Send a picture for prediction",
    )

def photo(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat_id
    photo_file = update.message.photo[-1].get_file()
    image = photo_file.download()
    image_np = cv2.imread(image)

    scale_percent = 80 # percent of original size
    width = int(image_np.shape[1] * scale_percent / 100)
    height = int(image_np.shape[0] * scale_percent / 100)
    image_np = processing.resize_image(image_np, width, height)

    data = detect.detection(image_np)

    image_np = processing.image_processing(image_np, data)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    cv2.imwrite('predict_image.jpg', image_np)
    #open image file
    predict_image = open('predict_image.jpg', 'rb')
    
    # send image to telegram
    bot.send_photo(chat_id=chat_id, photo=predict_image)
    os.remove('predict_image.jpg')
    os.remove(image)
    

updater = Updater('1925798170:AAEhdke3ALP-riQJ2diNyoQWkUSWLWeTm1o')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo))

updater.start_polling()
updater.idle()