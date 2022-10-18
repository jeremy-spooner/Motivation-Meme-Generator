"""Represents a model for a TxtIngestor.

The `TxtIngestor` class represents an object that can read in quotes from TXT
files. It is a strategy object that is passed a path as a string.
"""

import pandas
import boolean
from typing import List
from .quoteModel import QuoteModel
from .ingestorInterface import IngestorInterface


class TxtIngestor(IngestorInterface):
    """A TxtIngestor.

    A TxtIngestor reads in quotes to QuoteModel Objects from a pdf file.
    """

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        """Determine if the file can be read based on its file extension.

        :param path: the string holding the path to a file
        """
        if path.split('.')[-1] == 'txt':
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a new List of QuoteModel objects from the contents of a file.

        :param path: the string holding the path to a file
        """
        quotes = []
        with open(path, 'r') as infile:
            for line in infile.readlines():
                body = line.split('-')[0].strip().strip('"')
                author = line.split('-')[1].strip().strip('"')
                quotes.append(QuoteModel(body, author))
        return quotes
