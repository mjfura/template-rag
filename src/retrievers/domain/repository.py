from abc import ABC, abstractmethod
from src.chunking.domain import ChunkValue


class RetrieverRepository(ABC):
    """
    Abstract class for the RetrieverRepository.

    This class defines the abstract methods that must be implemented by the RetrieverRepository in the infrastructure layer.
    """

    @abstractmethod
    def basic_retrieve(self, query: str) -> list[ChunkValue]:
        pass

    @abstractmethod
    def advanced_retrieve(
        self, query: str, entities: list[tuple[str, str]]
    ) -> list[ChunkValue]:
        pass
