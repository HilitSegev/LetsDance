import os
import telebot
import shutil
from dotenv import dotenv_values
from main_processor import process_video
from cloud_storage import cloud_manager

from pose_estimator.color_configs import COLORS

from consts import *

config = dotenv_values(".env")
bot = telebot.TeleBot(config['API_KEY'])

print("Starting bot...")

# Save user settings (bg, emoji, color)
users_configs = dict()


@bot.message_handler(commands=['start'])
def hello(message):
    welcome_message = """
    Hello, I am a bot that can help you to make your own video with your own background and emoji.\n\
    Please provide an emoji to use :)\n\
    Options: [Elsa, Crazy]
    """
    bot.send_message(message.chat.id, welcome_message)


def is_valid_emoji(message):
    try:
        if message.text in ['Crazy', 'Elsa']:
            return True
        return False
    except:
        return False


def is_valid_bg(message):
    try:
        if message.text in ['1.jpg', '2.jpg'] or int(message.text) in range(1, 52):
            return True
        return False
    except:
        return False


def is_valid_colors(message):
    try:
        if message.text in COLORS.keys():
            return True
        return False
    except:
        return False


def is_valid_url(message):
    try:
        if message.text.endswith('.mp4'):
            return True
        return False
    except:
        return False


@bot.message_handler(func=is_valid_emoji)
def update_emoji(message):
    if message.chat.id not in users_configs:
        users_configs[message.chat.id] = dict()
    users_configs[message.chat.id]['emoji'] = message.text
    bot.send_message(message.chat.id, 'Emoji updated! \nPlease select a background image [1-51]')
    print(users_configs[message.chat.id])


@bot.message_handler(func=is_valid_bg)
def update_bg(message):
    if message.chat.id not in users_configs:
        users_configs[message.chat.id] = dict()
    users_configs[message.chat.id]['bg'] = message.text if message.text.endswith('.jpg') else (
            str(message.text) + '.jpg')
    bot.send_message(message.chat.id, 'Background Image updated! \nPlease select a color palette to use!')
    print(users_configs[message.chat.id])


@bot.message_handler(func=is_valid_colors)
def update_colors(message):
    if message.chat.id not in users_configs:
        users_configs[message.chat.id] = dict()
    users_configs[message.chat.id]['colors'] = message.text
    bot.send_message(message.chat.id, 'Color Palette updated! \nPlease send your video!')
    print(users_configs[message.chat.id])


@bot.message_handler(func=is_valid_url)
def bot_process_video(message):
    try:
        if message.chat.id not in users_configs:
            users_configs[message.chat.id] = dict(emoji=None, bg=None, colors=None)
        print(users_configs[message.chat.id])

        video_path = message.text
        final_video_path = process_video(video_path,
                                         RESOURCES_DIR + BACKGROUND_IMAGES_DIR + users_configs[message.chat.id]['bg'] if
                                         users_configs[message.chat.id]['bg'] else None,
                                         users_configs[message.chat.id]['emoji'],
                                         users_configs[message.chat.id]['colors'])
        file_name = OUTPUTS_DIR + final_video_path.split("/")[-1]
        bot.send_video(chat_id=message.chat.id, video=open(file_name, 'rb'), supports_streaming=True)
    except:
        bot.reply_to(message, 'Processing video failed :sad:')


@bot.message_handler(content_types=['video'])  # list relevant content types
def addfile(message):
    file_name = RESOURCES_DIR + VIDEOS_DIR + message.video.file_id + ".mp4"
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, f'File saved! Processing...')
    message.text = file_name
    message.video = None
    bot_process_video(message)


bot.polling()
