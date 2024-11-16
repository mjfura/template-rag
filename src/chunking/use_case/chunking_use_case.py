from ..domain import ChunkingRepository
from src.loaders.domain import DocumentValue
from ..domain import ChunkValue
class ChankingUseCase:
    def __init__(self, chunking_repository:ChunkingRepository):
        self.chunking_repository = chunking_repository

    def get_chunks(self, documents:list[DocumentValue]) -> list[ChunkValue]:
        return self.chunking_repository.basic_chunking(documents)