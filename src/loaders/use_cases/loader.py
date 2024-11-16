from src.loaders.domain import LoaderRepository,FileValue
class LoaderUseCase:
    def __init__(self, loader: LoaderRepository):
        self.loader = loader

    def upload_to_bucket(self, file:FileValue) -> dict:
        return self.loader.upload(file)