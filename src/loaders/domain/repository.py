from abc import ABC, abstractmethod
from .value import FileValue
class LoaderRepository(ABC):
    @abstractmethod
    def upload(self, file: FileValue) -> dict:
        pass
