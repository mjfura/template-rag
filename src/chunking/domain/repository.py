from abc import ABC, abstractmethod
from src.loaders.domain import DocumentValue
from .value import ChunkValue
class ChunkingRepository(ABC):
    """
    Abstract class for the ChunkingRepository.
    
    This class defines the abstract methods that must be implemented by the ChunkingRepository in the infrastructure layer.
    """
    
    @abstractmethod
    def basic_chunking(self, documents:list[DocumentValue]) -> list[ChunkValue]:
        pass