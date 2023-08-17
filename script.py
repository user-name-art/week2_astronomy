import os

import requests


def download_image(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.content


if __name__ == '__main__':
    filename = 'hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    headers = {'User-Agent': 'AstronomyBot/0.1 (art.gilyazov@mail.ru)'}
    directory = 'images'

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    os.chdir(directory)

    photo = download_image(url, headers)

    with open(filename, 'wb') as file:
        file.write(photo)
