import os
import argparse

import requests

from image_extention import get_image_extension


def fetch_spacex_launch(url, directory, headers, launch_id):
    launch_url = f'{url}{launch_id}'

    response = requests.get(launch_url, headers=headers)
    response.raise_for_status()

    photos = (response.json()['links']['flickr']['original'])

    for number, photo_url in enumerate(photos):
        response = requests.get(photo_url)
        response.raise_for_status()

        image_extention = get_image_extension(photo_url)

        with open(f'{directory}/spacex{number}{image_extention}', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    headers = {'User-Agent': 'AstronomyBot/0.1 (art.gilyazov@mail.ru)'}
    directory = 'images'
    spacex_url = 'https://api.spacexdata.com/v5/launches/'

    parser = argparse.ArgumentParser()
    parser.add_argument('id', nargs='?', default='latest')
    launch_id = parser.parse_args().id

    if not os.path.exists(directory):
        os.makedirs(directory)

    fetch_spacex_launch(spacex_url, directory, headers, launch_id)
