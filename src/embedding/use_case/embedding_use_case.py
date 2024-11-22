from typing import Generic, TypeVar
from ..domain import EmbeddingRepository

T = TypeVar("T")


class EmbeddingUseCase(Generic[T]):
    """
    EmbeddingUseCase class.

    This class is used to get the embeddings of a given text using the EmbeddingRepository.

    Args:
        Generic (T): The type of the model that will be used to get the embeddings.

    Attributes:
        embedding_repository (EmbeddingRepository): The repository that will be used to get the embeddings.
    """

    def __init__(self, embedding_repository: EmbeddingRepository[T]):
        self.embedding_repository = embedding_repository

    def get_embedding(self, text: str) -> list[float]:
        return self.embedding_repository.embed(text)

    def get_model_embedding(self) -> T:
        return self.embedding_repository.get_model()
