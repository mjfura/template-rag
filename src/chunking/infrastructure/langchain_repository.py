from ..domain import ChunkingRepository
from ..domain.value import ChunkValue
from src.loaders.domain import DocumentValue
class LangchainChunkingRepository(ChunkingRepository):
    def basic_chunking(self, documents:list[DocumentValue]) -> list[ChunkValue]:
        return [ChunkValue(content=doc.content, metadata=doc.metadata) for doc in documents]