from abc import ABC, abstractmethod
from src.loaders.domain import DocumentValue
class VectorStoreRepository(ABC):
        
        @abstractmethod
        def add_documents(self, documents:list[DocumentValue]) -> list[str]:
            pass
        
        @abstractmethod
        def search(self, query:str) -> list[DocumentValue]:
            pass