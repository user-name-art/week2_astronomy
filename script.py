import os

import requests
from dotenv import load_dotenv
from urllib import parse


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


def get_image_extension(url):
    path = parse.urlsplit(url)
    return os.path.splitext(parse.unquote(path.path))[1]


def fetch_nasa_apod(url, directory, request_paramerts):
    response = requests.get(url, params=request_paramerts, headers=headers)
    response.raise_for_status()

    apod = response.json()

    for number, day in enumerate(apod):
        response = requests.get(day['url'])
        response.raise_for_status()

        image_extention = get_image_extension(day['url'])

        if image_extention:
            with open(f'{directory}/nasa_apod_{number}{image_extention}', 'wb') as file:
                file.write(response.content)


def fetch_nasa_epic(url, directory, request_parametrs):
    response = requests.get(url, params=request_parametrs, headers=headers)
    response.raise_for_status()

    epic = response.json()
    for number, photo in enumerate(epic):
        photo_id = epic[number]['identifier']
        photo_date = '/'.join(epic[0]['date'].split()[0].split('-'))

        epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/epic_1b_{photo_id}.png'
        
        response = requests.get(epic_photo_url, params=request_parametrs)
        response.raise_for_status()


        with open(f'{directory}/nasa_epic_{number}.png', 'wb') as file:
            file.write(response.content)
    

if __name__ == '__main__':
    load_dotenv()

    nasa_apod_request_paramerts = {
        'api_key': {os.environ["NASA_TOKEN"]},
        'count': 30,
    }

    nasa_epic_request_paramerts = {
        'api_key': {os.environ["NASA_TOKEN"]},
    }

    filename = 'hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    headers = {'User-Agent': 'AstronomyBot/0.1 (art.gilyazov@mail.ru)'}
    directory = 'images'
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    link = 'https://example.com/txt/hello%20world.txt?v=9#python'
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'

    if not os.path.exists(directory):
        os.makedirs(directory)

    #download_image(url, directory)
    #fetch_spacex_launch_by_id(spacex_url, directory)
    #print(get_image_extension(link))
    #fetch_nasa_apod(nasa_apod_url, directory, nasa_apod_request_paramerts)
    fetch_nasa_epic(nasa_epic_url, directory, nasa_apod_request_paramerts)
