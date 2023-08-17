import os

import requests


def download_image(url, directory):
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(f'{directory}/{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch_by_id(url, directory):
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    photos = (response.json()['links']['flickr']['original'])

    for number, photo_url in enumerate(photos):
        response = requests.get(photo_url)
        response.raise_for_status()

        with open(f'{directory}/spacex{number}.jpg', 'wb') as file:
            file.write(response.content)    


if __name__ == '__main__':
    filename = 'hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    headers = {'User-Agent': 'AstronomyBot/0.1 (art.gilyazov@mail.ru)'}
    directory = 'images'
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'

    if not os.path.exists(directory):
        os.makedirs(directory)

    #download_image(url, directory)
    fetch_spacex_launch_by_id(spacex_url, directory)


