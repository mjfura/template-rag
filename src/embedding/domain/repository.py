from abc import ABC, abstractmethod
from typing import TypeVar,Generic
T = TypeVar("T")
class EmbeddingRepository(ABC,Generic[T]):
        
    @abstractmethod
    def embed(self, text:str) -> list[float]:
        pass
    
    @abstractmethod
    def get_model(self) -> T:
        pass
    