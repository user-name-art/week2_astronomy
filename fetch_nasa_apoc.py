import os

import requests
from dotenv import load_dotenv

from processing_filename import get_and_save_image


def main(url, directory, request_paramerts):
    response = requests.get(url, params=request_paramerts)
    response.raise_for_status()

    apod = response.json()
    filename_template = 'nasa_apod_'

    for picture_number, picture in enumerate(apod):
        get_and_save_image(picture['url'], directory, picture_number, filename_template)


if __name__ == '__main__':
    load_dotenv()

    nasa_apod_request_paramerts = {
        'api_key': {os.environ["NASA_TOKEN"]},
        'count': 10,
    }

    directory = 'images'
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'

    os.makedirs(directory, exist_ok=True)
        
    main(nasa_apod_url, directory, nasa_apod_request_paramerts)  

