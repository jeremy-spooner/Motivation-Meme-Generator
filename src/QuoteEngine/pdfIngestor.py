"""Represents a model for a PdfIngestor.

The `PdfIngestor` class represents an object that can read in quotes from DOCX
files. It is a strategy object that is passed a path as a string.
"""

import os
import random
import boolean
import subprocess
from typing import List
from .quoteModel import QuoteModel
from .ingestorInterface import IngestorInterface


class PdfIngestor(IngestorInterface):
    """A PdfIngestor.

    A PdfIngestor reads in quotes to QuoteModel Objects from a pdf file.
    """

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        """Determine if the file can be read based on its file extension.

        :param path: the string holding the path to a file
        """
        if path.split('.')[-1] == 'pdf':
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a new List of QuoteModel objects from the contents of a file.

        :param path: the string holding the path to a file
        """
        temp_file_path = f'{random.randint(0,10000)}.txt'
        call = subprocess.call(['pdftotext', path, temp_file_path])
        with open(temp_file_path, 'r') as infile:
            quotes = []
            for line in infile.readlines():
                line = line.strip('\n\r"').strip()
                if len(line) > 0:
                    body = line.split('-')[0].strip().strip('"')
                    author = line.split('-')[1].strip().strip('"')
                    quotes.append(QuoteModel(body, author))
                    # quotes.append(QuoteModel(line.split('-')[0].strip(),
                    #                         line.split('-')[1].strip()))
        infile.close()
        os.remove(temp_file_path)
        return quotes
