from collections import namedtuple
import sys
import os

from PIL import Image, ImageDraw, ImageFont
from settings import *

Font = namedtuple('Font', 'ttf text color size offset')
ImageDetails = namedtuple('Image', 'left top size')


class Banner:
    def __init__(self, size=DEFAULT_CANVAS_SIZE, background=DEFAULT_BG, output_file=DEFAULT_OUTPUT_FILE):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.output_file = output_file
        self.image = Image.open(os.path.join(DEFAULT_ASSET_DIR, background))
        self.image = self.image.resize(DEFAULT_CANVAS_SIZE)
        self.image_coords = []

    def add_image(self, image, resize=False,
                  top=DEFAULT_TOP_MARGIN, margin_left=15, right=False, margin_right=15, background=False):
        """
           Adds (pastes) image on canvas
           If right is given calculate left, else take left
           Returns added img size
        """
        img = Image.open(os.path.join(DEFAULT_ASSET_DIR, image))

        if resize:
            size = self.height * RESIZE_PERCENTAGE
            img.thumbnail((size, size), Image.ANTIALIAS)

        if right:
            img = img.resize(RIGHT_IMAGE_SIZE)
            margin_left = self.image.size[0] - img.size[0] - margin_right  # 15 is slight shift from right
        else:
            img = img.resize(LEFT_IMAGE_SIZE)

        offset = (margin_left, top)
        self.image.paste(img, offset)


def main():
    banner = Banner(background="midPB.jpg")  # :background name of the image file for background

    LEFT_BOX = "polar-white.jpg"   # image on the left
    RIGHT_BOX = "leftPB.jpg"       # image on the right
    banner.add_image(image=LEFT_BOX, right=False)  # place left image
    banner.add_image(image=RIGHT_BOX, right=True)  # place right image

    banner.image.save(os.path.join(DEFAULT_RESULT_DIR, DEFAULT_OUTPUT_FILE), quality=100)


main()
