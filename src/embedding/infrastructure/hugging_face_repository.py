from langchain_huggingface import HuggingFaceEmbeddings
from ..domain import EmbeddingRepository

class HuggingFaceEmbeddingRepository(EmbeddingRepository[HuggingFaceEmbeddings]):
    """
    A concrete implementation of the EmbeddingRepository interface that uses the HuggingFaceEmbeddings class from the langchain-huggingface package.
    
    Attributes:
        embeddings_model (HuggingFaceEmbeddings): The HuggingFaceEmbeddings object used to embed text.
    """
    def __init__(self):
        self.embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")

    def embed(self, text: str) -> str:
        return self.embeddings_model.embed_query(text)
    
    def get_model(self)->HuggingFaceEmbeddings:
        return self.embeddings_model
    