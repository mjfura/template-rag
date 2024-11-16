from abc import ABC, abstractmethod
from src.loaders.domain import DocumentValue
from .value import ChunkValue
class ChunkingRepository(ABC):
    
    @abstractmethod
    def basic_chunking(self, documents:list[DocumentValue]) -> list[ChunkValue]:
        pass