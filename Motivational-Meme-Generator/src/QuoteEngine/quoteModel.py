"""Represents a model for a storing a quote.

The `QuoteModel` class represents an object that can hold information
about a quote, including the quote and the author.
"""


class QuoteModel():
    """A model that stores information about a quote.

    A QuoteModel can be initialized with a quote and author and
    can be printed.
    """

    def __init__(self, quote, author):
        """Create a new QuoteModel.

        :param quote: the string representation of a quote
        :param author: the string representation of an author
        """
        self.body = quote
        self.author = author

    def __str__(self):
        """Set the string representation of a quote.

        Format: quote - author
        """
        return f'{self.body} - {self.author}'
