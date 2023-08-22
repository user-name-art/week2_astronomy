import os
import argparse

import requests

from processing_filename import get_image_by_url, get_image_extension, save_image


def main():
    headers = {'User-Agent': 'AstronomyBot/0.1 (art.gilyazov@mail.ru)'}
    directory = 'images'
    spacex_url = 'https://api.spacexdata.com/v5/launches/'

    parser = argparse.ArgumentParser(description='Скрипт скачивает фотографии с запусков ракет SpaceX.')
    parser.add_argument('id', nargs='?', default='latest', help='id запуска; если не указан - скрипт смотрит последний запуск.')
    launch_id = parser.parse_args().id

    os.makedirs(directory, exist_ok=True)
    launch_url = f'{spacex_url}{launch_id}'

    response = requests.get(launch_url, headers=headers)
    response.raise_for_status()

    photos = response.json()['links']['flickr']['original']
    filename_template = 'spacex_'

    for photo_number, photo_url in enumerate(photos):
        image = get_image_by_url(photo_url)
        image_extension = get_image_extension(picture['url'])

        if image_extension:
            save_image(image, directory, filename_template, photo_number, image_extension)


if __name__ == '__main__':
    main()
