"""A File for running creating memes through the command line.

The generate_meme function is used to create the meme from the
MemeEngine class.
"""
import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    # create meme using MemeEngine in static directory
    meme = MemeEngine('./static')
    path = meme.make_meme(img, quote.body, quote.author)

    return path


if __name__ == "__main__":
    # use argparse to read in path, body and author
    parser = argparse.ArgumentParser(description='Create a meme.')
    parser.add_argument('--path', type=str, default=None,
                        help='An image path')
    parser.add_argument('--body', type=str, default=None,
                        help='A string quote body')
    parser.add_argument('--author', type=str, default=None,
                        help='A string quote author')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
