"""Represents an interface for an Ingestor.

The `IngestorInterface` abstract class represents an interface for an class
that can parse quotes from a file.

"""

import boolean
from typing import List
from .quoteModel import QuoteModel
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """An Interface to ingest quotes from different file types.

    A IngestorInterface contains a method to check if it can ingest
    a certain file type and a method to carry out the parsing.
    """

    @abstractmethod
    def can_ingest(cls, path: str) -> boolean:
        """Determine if the file can be read based on its file extension.

        :param path: the string holding the path to a file
        """
        pass

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a new List of QuoteModel objects from the contents of a file.

        :param path: the string holding the path to a file
        """
        pass
