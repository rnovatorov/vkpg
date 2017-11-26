from urllib.parse import urlparse
from argparse import ArgumentParser
from src.vkag import VkAlbumGetter


def main(args):
    with VkAlbumGetter() as vkag:
        vkag.login()
        album = vkag.get_album(args.first_photo_url.geturl())
        for photo in album.photos:
            print(photo.url)


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument(dest="first_photo_url", type=urlparse)
    arg_parser.add_argument("-o", dest="output")
    main(arg_parser.parse_args())