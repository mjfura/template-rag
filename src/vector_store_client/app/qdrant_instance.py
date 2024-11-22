from ..infrastructure import QdrantVectorStoreRepository
from ..use_case import VectorStoreUseCase
from src.embedding.app import embeddings_use_case

collection_name = "archivos_uk"
qdrant_repository = QdrantVectorStoreRepository(
    embeddings_use_case.get_model_embedding(), collection_name
)
vector_store_use_case = VectorStoreUseCase(qdrant_repository)
