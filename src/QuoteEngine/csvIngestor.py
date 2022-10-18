"""Represents a model for a CsvIngestor.

The `CsvIngestor` class represents an object that can read in quotes from CSV
files. It is a strategy object that is passed a path as a string.
"""

import pandas
import boolean
from typing import List
from .quoteModel import QuoteModel
from .ingestorInterface import IngestorInterface


class CsvIngestor(IngestorInterface):
    """A CsvIngestor.

    A CsvIngestor reads in quotes to QuoteModel Objects from a CSV file.
    """

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        """Determine if the file can be read based on its file extension.

        :param path: the string holding the path to a file
        """
        if path.split('.')[-1] == 'csv':
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a new List of QuoteModel objects from the contents of a file.

        :param path: the string holding the path to a file
        """
        quotes = []
        data = pandas.read_csv(path, header=0)

        for index, row in data.iterrows():
            quotes.append(QuoteModel(row['body'].strip('"'), row['author']))

        return quotes
