import os
import argparse

import telegram
import random
import time

from dotenv import load_dotenv
from processing_filename import get_filenames_in_folder


if __name__ == '__main__':
    load_dotenv()

    directory = 'images'

    image_names = get_filenames_in_folder()

    bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])
    chat = os.environ["TG_CHAT"]

    parser = argparse.ArgumentParser(
        description='Скрипт отправляет по одной фотографии из папки images в Telegram-канал с заданным интервалом.'
        )
    parser.add_argument('time', nargs='?', type=int, default=4, help='временной интервал в часах (по умолчанию 4 часа)')
    hours_to_seconds = 3600 * parser.parse_args().time

    while True:
        for image in image_names:
            with open(f'{directory}/{image}', 'rb') as file:
                bot.send_document(chat_id=chat, document=file)
            time.sleep(hours_to_seconds)

        random.shuffle(image_names)

