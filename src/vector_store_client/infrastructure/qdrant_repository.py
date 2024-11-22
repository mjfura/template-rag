from src.chunking.domain import ChunkValue
from ..domain import VectorStoreRepository
from langchain_qdrant import RetrievalMode
from langchain_qdrant import QdrantVectorStore
from src.chunking.adapters import (
    create_document_from_chunk_adapter,
    create_chunk_from_document,
)
from langchain.embeddings.base import Embeddings
from typing import cast


class QdrantVectorStoreRepository(VectorStoreRepository):
    """
    QdrantVectorStoreRepository class.

    This class implements the VectorStoreRepository abstract class from the domain layer.

    It is used to interact with the Qdrant vector store as our infrastructure.

    Attributes:
        vector_store (QdrantVectorStore): The Qdrant vector store object.
    """

    def __init__(self, embedding_model: Embeddings, collection_name: str) -> None:
        self.vector_store = QdrantVectorStore.from_documents(
            [],
            embedding=embedding_model,
            location=":memory:",
            collection_name=collection_name,
            retrieval_mode=RetrievalMode.DENSE,
        )

    def add_documents(self, chunks: list[ChunkValue]) -> list[str]:
        """
        add_documents is a method that adds a list of ChunkValue objects to the vector store.

        This method receives a list of ChunkValue objects and adds them to the vector store. It returns a list of strings representing the document IDs.

        Args:
            chunks (list[ChunkValue]): A list of ChunkValue objects.

        Returns:
            list[str]: A list of strings representing the document IDs.
        """
        documents = create_document_from_chunk_adapter(chunks)
        return cast(list[str], self.vector_store.add_documents(documents))

    def search(self, query: str) -> list[ChunkValue]:
        """
        search is a method that searches for documents in the vector store.

        This method receives a query and searches for documents in the vector store. It returns a list of DocumentValue objects.

        Args:
            query (str): The query to search for.

        Returns:
            list[DocumentValue]: A list of DocumentValue objects.
        """
        documents = self.vector_store.similarity_search(query)
        return create_chunk_from_document(documents)
