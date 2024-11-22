from langchain_huggingface import HuggingFaceEmbeddings
from ..domain import EmbeddingRepository
from typing import cast


class HuggingFaceEmbeddingRepository(EmbeddingRepository[HuggingFaceEmbeddings]):
    """
    A concrete implementation of the EmbeddingRepository interface that uses the HuggingFaceEmbeddings class from the langchain-huggingface package.

    Attributes:
        embeddings_model (HuggingFaceEmbeddings): The HuggingFaceEmbeddings object used to embed text.
    """

    def __init__(self) -> None:
        self.embeddings_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-MiniLM-L6-v2"
        )

    def embed(self, text: str) -> list[float]:
        return cast(list[float], self.embeddings_model.embed_query(text))

    def get_model(self) -> HuggingFaceEmbeddings:
        return self.embeddings_model

    def embed_list(self, texts: list[str]) -> list[list[float]]:
        return cast(list[list[float]], self.embeddings_model.embed_documents(texts))
