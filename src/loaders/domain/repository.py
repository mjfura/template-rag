from abc import ABC, abstractmethod
from .value import FileValue, DocumentValue


class LoaderRepository(ABC):
    """
    LoaderRepository is an abstract class that defines the methods that a loader repository should implement.

    """

    @abstractmethod
    def load_file(self, path: str) -> list[DocumentValue]:
        """
        load_file is a method that loads a file and returns a list of DocumentValue.

        This method receives a path to a file and returns a list of DocumentValue objects. Each DocumentValue object represents a page of the file.

        Args:
            path (str): The path to the file.

        Returns:
            list[DocumentValue]: A list of DocumentValue objects.
        """
        pass


class BucketRepository(ABC):
    """
    BucketRepository is an abstract class that defines the methods that a bucket repository should implement.

    """

    @abstractmethod
    def upload(self, file: FileValue) -> str:
        """
        upload is a method that uploads a file to a bucket and returns the pathname.

        This method receives a FileValue object and uploads the file to a bucket. It returns the pathname where the file was uploaded.

        Args:
            file (FileValue): The FileValue object to be uploaded.

        Returns:
            str: The pathname where the file was uploaded.
        """
        pass
