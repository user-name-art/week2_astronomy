import os

from urllib import parse


def get_image_extension(url):
    path = parse.urlsplit(url)
    return os.path.splitext(parse.unquote(path.path))[1]
