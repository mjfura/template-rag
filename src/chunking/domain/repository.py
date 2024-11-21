from abc import ABC, abstractmethod
from src.loaders.domain import DocumentValue
from src.embedding.domain import EmbeddingSentence
from .value import ChunkValue
class ChunkingRepository(ABC):
    """
    Abstract class for the ChunkingRepository.
    
    This class defines the abstract methods that must be implemented by the ChunkingRepository in the infrastructure layer.
    """
    
    @abstractmethod
    def basic_chunking(self, documents:list[DocumentValue]) -> list[ChunkValue]:
        pass
    
    @abstractmethod
    def combine_sentences(self, documents:list[DocumentValue], buffer_size:int) -> list[str]:
        pass
    
    @abstractmethod
    def semantic_chunking(self, embeddings_sentence:list[EmbeddingSentence],breakpoint_percentile:float) -> list[ChunkValue]:
        pass