"""A File for running Flask.

This is the main project file used to run the Flask app.
"""

import os
from random import randrange, choice
import requests
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine
from flask import Flask, render_template, abort, request

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []

    # append all quotes from the files to the quotes array
    for file in quote_files:
        for quote in Ingestor.parse(file):
            quotes.append(quote)

    # save all of the image file names in the image_dir
    image_dir = "./_data/photos/dog/"
    img_names = os.listdir(image_dir)
    imgs = []
    for name in img_names:
        imgs.append(f'{image_dir}/{name}')

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # choose random quote and image url
    quote = choice(quotes)
    image = choice(imgs)

    # create meme and return its path
    self_path = meme.make_meme(image, quote.body, quote.author)

    return render_template('meme.html', path=self_path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # save the image from the image_url form to a temp local file
    image_url = request.form['image_url']
    
    # attempt to retrive the image_url
    try:
        image_data = requests.get(image_url)
    except requests.exceptions.ConnectionError:
        print("Invalid image. Please verify image address is valid")
        return render_template('meme_error.html')
  
    temp_path = f'./static/{randrange(0, 100000)}-tmp.jpg'

    # write content to the temp_path
    with open(temp_path, 'wb') as out_img:
        out_img.write(image_data.content)

    # create quote using request form input
    quote = QuoteModel(request.form['body'], request.form['author'])

    # create meme and return its path
    meme_path = meme.make_meme(temp_path, quote.body, quote.author)

    # remove the temporary file
    os.remove(temp_path)

    return render_template('meme.html', path=meme_path)


if __name__ == "__main__":
    app.run()
