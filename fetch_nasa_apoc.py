import os

import requests
from dotenv import load_dotenv

from processing_filename import get_image_by_url, get_image_extension, save_image


def main():
    load_dotenv()

    directory = 'images'
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    filename_template = 'nasa_apod_'
    nasa_apod_request_parametrs = {
        'api_key': {os.environ["NASA_TOKEN"]},
        'count': 10,
    }

    os.makedirs(directory, exist_ok=True)

    response = requests.get(nasa_apod_url, params=nasa_apod_request_parametrs)
    response.raise_for_status()

    apod = response.json()

    for picture_number, picture in enumerate(apod):
        image = get_image_by_url(picture['url'], nasa_apod_request_parametrs)
        image_extension = get_image_extension(picture['url'])

        if image_extension:
            save_image(image, directory, filename_template, picture_number, image_extension)


if __name__ == '__main__':
    main()  

