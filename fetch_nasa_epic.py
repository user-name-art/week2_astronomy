import os
import datetime

import requests
from dotenv import load_dotenv


def fetch_nasa_epic(url, directory, request_parametrs):
    response = requests.get(url, params=request_parametrs)
    response.raise_for_status()

    epic = response.json()

    for number, photo in enumerate(epic):
        photo_id = epic[number]['identifier']
        photo_date = datetime.datetime.strptime(epic[number]['date'].split()[0], '%Y-%m-%d').strftime('%Y/%m/%d')

        epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/epic_1b_{photo_id}.png'
        
        response = requests.get(epic_photo_url, params=request_parametrs)
        response.raise_for_status()

        with open(f'{directory}/nasa_epic_{number}.png', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    load_dotenv()

    nasa_epic_request_paramerts = {
        'api_key': {os.environ["NASA_TOKEN"]},
    }

    directory = 'images'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'

    if not os.path.exists(directory):
        os.makedirs(directory)

    fetch_nasa_epic(nasa_epic_url, directory, nasa_epic_request_paramerts)
