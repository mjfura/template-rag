from src.loaders.domain import DocumentValue
from src.chunking.domain import ChunkValue
from ..domain import VectorStoreRepository
from langchain_qdrant import RetrievalMode
from langchain_qdrant import QdrantVectorStore
from src.loaders.adapters import create_document_value_adapter
from src.chunking.adapters import create_document_from_chunk_adapter

class QdrantVectorStoreRepository(VectorStoreRepository):
        def __init__(self, embedding_model, collection_name: str):

            self.vector_store = QdrantVectorStore.from_documents(
                [],
                embedding=embedding_model,
                location=":memory:",
                collection_name=collection_name,
                retrieval_mode=RetrievalMode.DENSE,
            )
        
        def add_documents(self, chunks: list[ChunkValue]) -> list[str]:
            documents = create_document_from_chunk_adapter(chunks)
            return self.vector_store.add_documents(documents)
        
        def search(self, query:str) -> list[DocumentValue]:
            documents = self.vector_store.similarity_search(query)
            return create_document_value_adapter(documents)
