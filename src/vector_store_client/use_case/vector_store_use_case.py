from ..domain import VectorStoreRepository
from src.loaders.domain import DocumentValue
from src.chunking.domain import ChunkValue
class VectorStoreUseCase:
    """
    VectorStoreUseCase class.
    
    This class is used to interact with the vector store repository.
    
    Attributes:
        vector_store (VectorStoreRepository): The vector store repository.
    """
    def __init__(self, vector_store: VectorStoreRepository):
        self.vector_store = vector_store

    def add_documents(self, documents:list[ChunkValue]) -> list[str]:
        """
        add_documents is a method that adds a list of ChunkValue objects to the vector store.
        
        This method receives a list of ChunkValue objects and adds them to the vector store. It returns a list of strings representing the document IDs.
        
        Args:
            documents (list[ChunkValue]): A list of ChunkValue objects.
            
        Returns:
            list[str]: A list of strings representing the document IDs.
        """
        return self.vector_store.add_documents(documents)

    def search(self, query:str)->list[DocumentValue]:
        """
        search is a method that searches for documents in the vector store.
        
        This method receives a query and searches for documents in the vector store. It returns a list of DocumentValue objects.
        
        Args:
            query (str): The query to search for.
            
        Returns:
            list[DocumentValue]: A list of DocumentValue objects
        """
        return self.vector_store.search(query)