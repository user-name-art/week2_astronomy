import os
import requests

from urllib import parse


def get_image_extension(url):
    path = parse.urlsplit(url)
    return os.path.splitext(parse.unquote(path.path))[1]


def get_filenames_in_folder():
    folder_path = 'images'
    file_names = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_names.append(file_name)

    return file_names


def get_and_save_image(photo_url, directory, number, filename_template, params=None):
    response = requests.get(photo_url, params=params)
    response.raise_for_status()

    image_extention = get_image_extension(photo_url)

    if image_extention: 
        with open(f'{directory}/{filename_template}{number}{image_extention}', 'wb') as file:
            file.write(response.content)
