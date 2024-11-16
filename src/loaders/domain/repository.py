from abc import ABC, abstractmethod
from .value import FileValue,DocumentValue
class LoaderRepository(ABC):
    
    @abstractmethod
    def load_file(self, path:str) -> list[DocumentValue]:
        pass

class BucketRepository(ABC):
    @abstractmethod
    def upload(self, file: FileValue) -> str:
        pass