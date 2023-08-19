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

    parser = argparse.ArgumentParser()
    parser.add_argument('time', nargs='?', default=4)
    hours_to_seconds = 3600 * parser.parse_args().time

    while True:
        for image in image_names:
            bot.send_document(chat_id='@astronomy_tatarstan', document=open(f'{directory}/{image}', 'rb'))
            time.sleep(hours_to_seconds)

        random.shuffle(image_names)

