from ..domain import EmbeddingRepository
from sentence_transformers import SentenceTransformer
class SentenceTransformerEmbeddingRepository(EmbeddingRepository[SentenceTransformer]):
    """
    A concrete implementation of the EmbeddingRepository interface that uses the HuggingFaceEmbeddings class from the langchain-huggingface package.
    
    Attributes:
        embeddings_model (HuggingFaceEmbeddings): The HuggingFaceEmbeddings object used to embed text.
    """
    def __init__(self):
        self.embeddings_model = SentenceTransformer("all-mpnet-base-v2")

    def embed(self, text: str) -> str:
        return self.embeddings_model.encode(text)
    
    def get_model(self)->SentenceTransformer:
        return self.embeddings_model
    
    def embed_list(self, texts: list[str]) -> list[list[float]]:
        return self.embeddings_model.encode(texts)