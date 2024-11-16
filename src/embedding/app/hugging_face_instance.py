from ..infrastructure import HuggingFaceEmbeddingRepository
from ..use_case import EmbeddingUseCase
from langchain_huggingface import HuggingFaceEmbeddings
hugging_face_repository = HuggingFaceEmbeddingRepository()

embeddings_use_case = EmbeddingUseCase[HuggingFaceEmbeddings](hugging_face_repository)
