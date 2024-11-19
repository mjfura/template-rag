from ..infrastructure import LangchainChunkingRepository
from ..use_case import ChankingUseCase
from src.loaders.adapters import create_document_value_adapter
from langchain.schema import Document
from src.chunking.domain import ChunkValue
langchain_repository = LangchainChunkingRepository()
chunking_use_case = ChankingUseCase(langchain_repository)

def pipeline_chunking(docs:list[Document])->list[ChunkValue]:
    """
    A pipeline function that takes a list of Langchain Document objects, converts them into DocumentValue objects,
    chunks them into smaller pieces, and converts the chunks back into Langchain Document objects.
    Args:
        docs (list[Document]): A list of Langchain Document objects to be chunked.
    Returns:
        list[ChunkValue]: A list of ChunkValue objects created from the given Documents.
    """
    docs_values = create_document_value_adapter(docs)
    chunks = chunking_use_case.get_chunks(docs_values)
    return chunks