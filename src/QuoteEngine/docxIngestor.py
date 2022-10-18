"""Represents a model for a DocxIngestor.

The `DocxIngestor` class represents an object that can read in quotes from DOCX
files. It is a strategy object that is passed a path as a string.
"""

import docx
import boolean
from typing import List
from .quoteModel import QuoteModel
from .ingestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """A DocxIngestor.

    A DocxIngestor reads in quotes to QuoteModel Objects from a docx file.
    """

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        """Determine if the file can be read based on its file extension.

        :param path: the string holding the path to a file
        """
        if path.split('.')[-1] == 'docx':
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a new List of QuoteModel objects from the contents of a file.

        :param path: the string holding the path to a file
        """
        quotes = []
        document = docx.Document(path)

        for paragraph in document.paragraphs:
            line = paragraph.text
            if line != "":
                body = line.split('-')[0].strip().strip('"')
                author = line.split('-')[1].strip().strip('"')
                quotes.append(QuoteModel(body, author))
        return quotes
