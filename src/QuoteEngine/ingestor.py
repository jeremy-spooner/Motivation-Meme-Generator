"""Represents a model for an Ingestor.

The `Ingestor` class represents an object that can read in quotes from
different file types. It is a strategy object that is passed a path as
a string.

It references four other strategy objects, CsvIngestor, DocxIngestor,
PdfIngestor, and TxtIngestor. All of these strategy objects, including the
'Ingestor' class inherit the abstract class IngestorInterface.

"""

import boolean
from typing import List
from .quoteModel import QuoteModel
from .csvIngestor import CsvIngestor
from .docxIngestor import DocxIngestor
from .pdfIngestor import PdfIngestor
from .txtIngestor import TxtIngestor
from .ingestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    """An Ingestor.

    An Ingestor reads in quotes to QuoteModel Objects from different
    file types. It can accept csv, docx, pdf, or txt.
    """

    ingestors = [CsvIngestor, DocxIngestor, PdfIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a new List of QuoteModel objects from the contents of a file.

        :param path: the string holding the path to a file
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception("Invalid file type. Try with txt, csv, docx, or pdf")
