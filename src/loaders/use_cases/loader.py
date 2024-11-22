from src.loaders.domain import (
    LoaderRepository,
    FileValue,
    BucketRepository,
    DocumentValue,
)


class LoaderUseCase:
    """
    LoaderUseCase class.

    This class is used to load the file into the system and upload it to the bucket.

    Attributes:
        loader (LoaderRepository): The loader repository.
        bucket (BucketRepository): The bucket repository.
    """

    def __init__(self, loader: LoaderRepository, bucket: BucketRepository):
        self.loader = loader
        self.bucket = bucket

    def upload_to_bucket(self, file: FileValue) -> list[DocumentValue]:
        """
        upload_to_bucket is a method that uploads a file to the bucket and returns a list of DocumentValue.

        This method receives a FileValue object, uploads the file to the bucket, and returns a list of DocumentValue objects. Each DocumentValue object represents a page of the file.

        Args:
            file (FileValue): The FileValue object to be uploaded.

        Returns:
            list[DocumentValue]: A list of DocumentValue objects.
        """
        pathname = self.bucket.upload(file)
        docs = self.loader.load_file(pathname)
        return docs
