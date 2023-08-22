import os
import datetime

import requests
from dotenv import load_dotenv

from processing_filename import get_image_by_url, get_image_extension, save_image


def main():
    load_dotenv()

    directory = 'images'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    filename_template = 'nasa_epic_'
    nasa_epic_request_parametrs = {
        'api_key': {os.environ["NASA_TOKEN"]},
    }
    
    os.makedirs(directory, exist_ok=True)

    response = requests.get(nasa_epic_url, params=nasa_epic_request_parametrs)
    response.raise_for_status()

    epic = response.json()
    
    for picture_number, picture in enumerate(epic):
        photo_id = epic[picture_number]['identifier']
        photo_date = datetime.datetime.strptime(epic[picture_number]['date'].split()[0], '%Y-%m-%d').strftime('%Y/%m/%d')

        epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/epic_1b_{photo_id}.png'
        
        image = get_image_by_url(epic_photo_url, nasa_epic_request_parametrs)
        image_extension = '.png'

        save_image(image, directory, filename_template, picture_number, image_extension)


if __name__ == '__main__':
    main()
