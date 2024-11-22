import os
from src.loaders.domain import BucketRepository
from src.config import BUCKET_PATH
from ..domain import FileValue


class LocalRepository(BucketRepository):
    """
    A concrete implementation of the BucketRepository interface that saves files in the local filesystem.
    """

    def upload(self, file: FileValue) -> str:
        """
        upload is a method that uploads a file to a local bucket and returns the pathname.

        This method receives a FileValue object and uploads the file to a local bucket. It returns the pathname where the file was uploaded.

        Args:
            file (FileValue): The FileValue object to be uploaded.

        Returns:
            str: The pathname where the file was uploaded.
        """
        # Crear la carpeta /bucket si no existe
        if not os.path.exists(BUCKET_PATH):
            os.makedirs(BUCKET_PATH)

        # Guardar el archivo en la carpeta /bucket
        file_path = os.path.join(BUCKET_PATH, file.name)
        with open(file_path, "wb") as f:
            f.write(file.content)

        return file_path
