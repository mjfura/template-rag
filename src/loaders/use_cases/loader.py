from src.loaders.domain import LoaderRepository,FileValue,BucketRepository,DocumentValue
class LoaderUseCase:
    def __init__(self, loader: LoaderRepository,bucket:BucketRepository):
        self.loader = loader
        self.bucket = bucket

    def upload_to_bucket(self, file:FileValue) -> list[DocumentValue]:
        pathname = self.bucket.upload(file)
        docs = self.loader.load_file(pathname)
        return docs