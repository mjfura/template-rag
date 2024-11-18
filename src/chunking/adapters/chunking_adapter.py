from langchain.schema import Document
from src.chunking.domain import ChunkValue
def create_document_from_chunk_adapter(chunks: list[ChunkValue]) -> list[Document]:
    """
    Converts a list of ChunkValue objects into a list of Langchain Document objects.
    Args:
        chunks (list[ChunkValue]): A list of ChunkValue objects to be converted.
    Returns:
        list[Document]: A list of Langchain Document objects created from the given chunks.
    """
    
    return [Document(page_content=chunk.content, metadata=chunk.metadata) for chunk in chunks]