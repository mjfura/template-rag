from abc import ABC, abstractmethod
from src.chunking.domain import ChunkValue


class VectorStoreRepository(ABC):
    """
    VectorStoreRepository is an abstract class that defines the methods that a vector store repository should implement.

    """

    @abstractmethod
    def add_documents(self, documents: list[ChunkValue]) -> list[str]:
        """
        add_documents is a method that adds a list of DocumentValue objects to the vector store.

        This method receives a list of DocumentValue objects and adds them to the vector store. It returns a list of strings representing the document IDs.

        Args:
            documents (list[DocumentValue]): A list of DocumentValue objects.

        Returns:
            list[str]: A list of strings representing the document IDs.
        """
        pass

    @abstractmethod
    def search(self, query: str) -> list[ChunkValue]:
        """
        search is a method that searches for documents in the vector store.

        This method receives a query and searches for documents in the vector store. It returns a list of DocumentValue objects.

        Args:
            query (str): The query to search for.

        Returns:
            list[DocumentValue]: A list of DocumentValue objects.
        """
        pass
