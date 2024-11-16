from typing import Generic, TypeVar
from ..domain import EmbeddingRepository
T = TypeVar('T')

class EmbeddingUseCase(Generic[T]):
    def __init__(self, embedding_repository: EmbeddingRepository):
        self.embedding_repository = embedding_repository

    def get_embedding(self, text: str) -> list[float]:
        return self.embedding_repository.embed(text)

    def get_model_embedding(self) -> T:
        return self.embedding_repository.get_model()