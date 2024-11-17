from ..domain import VectorStoreRepository
from src.loaders.domain import DocumentValue
from src.chunking.domain import ChunkValue
class VectorStoreUseCase:
    def __init__(self, vector_store: VectorStoreRepository):
        self.vector_store = vector_store

    def add_documents(self, documents:list[ChunkValue]) -> list[str]:
        return self.vector_store.add_documents(documents)

    def search(self, query:str)->list[DocumentValue]:
        return self.vector_store.search(query)