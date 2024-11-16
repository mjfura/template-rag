from abc import ABC, abstractmethod
class CleanerRepository(ABC):
    @abstractmethod
    def remove_stopwords(self, text:str) -> str:
        pass
    
    @abstractmethod
    def to_lower(self, text:str) -> str:
        pass
    
    @abstractmethod
    def lemmatization(self, text:str) -> str:
        pass