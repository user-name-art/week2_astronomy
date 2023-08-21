import os
import argparse

import telegram
import random

from dotenv import load_dotenv
from processing_filename import get_filenames_in_folder


if __name__ == '__main__':
    load_dotenv()

    directory = 'images'

    image_names = get_filenames_in_folder()

    bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])
    chat = os.environ["TG_CHAT"]

    parser = argparse.ArgumentParser(description='Скрипт отправляет фотографию из папки images в Telegram-канал.')
    parser.add_argument('name', nargs='?', default=random.choice(image_names), help='имя файла (опционально)')
    filename = parser.parse_args().name

    with open(f'{directory}/{filename}', 'rb') as file:
        bot.send_document(chat_id=chat, document=file)
