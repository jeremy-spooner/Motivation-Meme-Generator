"""An Engine for a creating memes.

The `MemeEngine` class can instiatiate an object that can create
memes based on an inputted image path and quote.
"""
import os
from random import randrange
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """An engine that creates memes.

    Memes are based on the image path, text and author.
    """

    def __init__(self, path):
        """Create a new MemeEngine.

        :param path: the string representation of a directory
        """
        self.path = path
        # create directory if not already created
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Return the full path to a new Meme image.

        :param img_path: the string representation of a directory
        :param text: the body of a quote as a string
        :param author: the author of a quote as a string
        """
        # resize the image to fit the width
        img = Image.open(img_path)
        height = int(width/float(img.size[0])*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        # generate random row for quote & author text
        text_pixel_row = randrange(30, height - 100)
        author_pixel_row = text_pixel_row + 30

        # load in the font
        font = ImageFont.truetype("_data/Fonts/Roboto-MediumItalic.ttf", 25)

        # add the text to image
        d = ImageDraw.Draw(img)
        d.text((40, text_pixel_row), text, fill='white', font=font)
        d.text((60, author_pixel_row), f'- {author}', fill='white',
               font=font)

        # save the image to out_path
        out_path = f'{self.path}/{randrange(0, 100000)}-meme.jpg'
        img.save(out_path)

        return out_path
