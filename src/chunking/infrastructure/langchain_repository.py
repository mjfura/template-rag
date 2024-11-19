from ..domain import ChunkingRepository
from ..domain.value import ChunkValue
from src.loaders.domain import DocumentValue
class LangchainChunkingRepository(ChunkingRepository):
    """
    LangchainChunkingRepository class.
    
    This class implements the ChunkingRepository abstract class from the domain layer.
    
    It is used to chunk the documents into smaller pieces using Langchain as our infrastructure.    
    """
    def basic_chunking(self, documents:list[DocumentValue]) -> list[ChunkValue]:
        """
        Basic chunking method.
        
        This method receives a list of DocumentValue objects and returns a list of ChunkValue objects. These DocumentValue were created by the LoaderUseCase.
        Basically, each DocumentValue object represents only one page of the file.
        """
        return [ChunkValue(content=doc.content, metadata=doc.metadata) for doc in documents]