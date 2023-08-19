import os

import requests
from dotenv import load_dotenv

from processing_filename import get_image_extension


def fetch_nasa_apod(url, directory, request_paramerts):
    response = requests.get(url, params=request_paramerts)

    apod = response.json()

    for number, day in enumerate(apod):
        response = requests.get(day['url'])
        response.raise_for_status()

        image_extention = get_image_extension(day['url'])

        if image_extention:
            with open(f'{directory}/nasa_apod_{number}{image_extention}', 'wb') as file:
                file.write(response.content)


if __name__ == '__main__':
    load_dotenv()

    nasa_apod_request_paramerts = {
        'api_key': {os.environ["NASA_TOKEN"]},
        'count': 10,
    }

    directory = 'images'
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'

    if not os.path.exists(directory):
        os.makedirs(directory)
        
    fetch_nasa_apod(nasa_apod_url, directory, nasa_apod_request_paramerts)  

