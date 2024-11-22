from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class EmbeddingRepository(ABC, Generic[T]):
    """
    Abstract class that represents the embedding repository.

    This class should be implemented by any class that will be used to embed text in the infrastructure layer.

    Attributes:
        ABC: Abstract class from the abc module.
        Generic: Generic class from the typing module
    """

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Embed abstract method.

        This method receives a text and returns the same text embedded.

        Args:
            text (str): The text that will be embedded.

        Returns:
            list[float]: The text embedded.
        """
        pass

    @abstractmethod
    def get_model(self) -> T:
        """
        Get model abstract method.

        This method returns the model that will be used to embed the text.

        Returns:
            T: The model that will be used to embed the text.
        """
        pass

    @abstractmethod
    def embed_list(self, texts: list[str]) -> list[list[float]]:
        """
        Embed list abstract method.

        This method receives a list of text and returns a list of embedded text.

        Args:
            texts (list[str]): The list of text that will be embedded.

        Returns:
            list[list[float]]: The list of embedded text.
        """
        pass
