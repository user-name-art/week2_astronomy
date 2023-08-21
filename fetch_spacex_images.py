import os
import argparse

import requests

from processing_filename import get_and_save_image


def main(url, directory, headers, launch_id):
    launch_url = f'{url}{launch_id}'

    response = requests.get(launch_url, headers=headers)
    response.raise_for_status()

    photos = response.json()['links']['flickr']['original']
    filename_template = 'spacex_'

    for photo_number, photo_url in enumerate(photos):
        get_and_save_image(photo_url, directory, photo_number, filename_template)


if __name__ == '__main__':
    headers = {'User-Agent': 'AstronomyBot/0.1 (art.gilyazov@mail.ru)'}
    directory = 'images'
    spacex_url = 'https://api.spacexdata.com/v5/launches/'

    parser = argparse.ArgumentParser(description='Скрипт скачивает фотографии с запусков ракет SpaceX.')
    parser.add_argument('id', nargs='?', default='latest', help='id запуска; если не указан - скрипт смотрит последний запуск.')
    launch_id = parser.parse_args().id

    os.makedirs(directory, exist_ok=True)

    main(spacex_url, directory, headers, launch_id)
