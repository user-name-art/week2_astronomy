import os

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