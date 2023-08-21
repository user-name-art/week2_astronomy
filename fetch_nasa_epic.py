import os
import datetime

import requests
from dotenv import load_dotenv

from processing_filename import get_and_save_image


def main(url, directory, request_parametrs):
    response = requests.get(url, params=request_parametrs)
    response.raise_for_status()

    epic = response.json()
    filename_template = 'nasa_epic_'

    for picture_number, picture in enumerate(epic):
        photo_id = epic[picture_number]['identifier']
        photo_date = datetime.datetime.strptime(epic[picture_number]['date'].split()[0], '%Y-%m-%d').strftime('%Y/%m/%d')

        epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/epic_1b_{photo_id}.png'
        
        get_and_save_image(epic_photo_url, directory, picture_number, filename_template, request_parametrs)


if __name__ == '__main__':
    load_dotenv()

    nasa_epic_request_paramerts = {
        'api_key': {os.environ["NASA_TOKEN"]},
    }

    directory = 'images'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    
    os.makedirs(directory, exist_ok=True)

    main(nasa_epic_url, directory, nasa_epic_request_paramerts)
