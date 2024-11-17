from langchain.schema import Document
from src.chunking.domain import ChunkValue
def create_document_from_chunk_adapter(chunks: list[ChunkValue]) -> list[Document]:
    return [Document(page_content=chunk.content, metadata=chunk.metadata) for chunk in chunks]