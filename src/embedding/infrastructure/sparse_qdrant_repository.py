from langchain_qdrant import FastEmbedSparse
from ..domain import EmbeddingRepository
from typing import cast
from torch import Tensor


class SparseQdrantEmbeddingRepository(EmbeddingRepository[FastEmbedSparse]):
    """
    A concrete implementation of the EmbeddingRepository interface that uses the FastEmbedSparse class from the langchain_qdrant package.

    Attributes:
        embeddings_model (FastEmbedSparse): The FastEmbedSparse object used to embed text.
    """

    def __init__(self) -> None:
        self.embeddings_model = FastEmbedSparse(model_name="Qdrant/bm25")

    def embed(self, text: str) -> list[float]:
        return cast(list[float], self.embeddings_model.embed_query(text))

    def get_model(self) -> FastEmbedSparse:
        return self.embeddings_model

    def embed_list(self, texts: list[str]) -> list[list[float]]:
        return cast(list[list[float]], self.embeddings_model.embed_documents(texts))

    def embed_tensor(self, text: str) -> Tensor:
        return self.embeddings_model.embed_query(text, convert_to_tensor=True)
