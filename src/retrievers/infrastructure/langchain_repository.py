from ..domain import RetrieverRepository
from langchain.vectorstores.base import VectorStoreRetriever
from src.chunking.domain import ChunkValue
from src.chunking.adapters import create_chunk_from_document

from qdrant_client.http import models


class LangchainRetrieverRepository(RetrieverRepository):
    def __init__(self, retriever: VectorStoreRetriever):
        self.retriever = retriever

    def basic_retrieve(self, query: str) -> list[ChunkValue]:
        docs = self.retriever.invoke(query)
        chunks = create_chunk_from_document(docs)
        return [chunks[0]]

    def advanced_retrieve(
        self, query: str, entities: list[tuple[str, str]]
    ) -> list[ChunkValue]:
        conditions = []
        for entity, entity_type in entities:
            conditions.append(
                models.FieldCondition(
                    key="entities",  # Campo en la metadata
                    match=models.MatchValue(
                        value=entity,
                    ),  # Coincide con el texto de la entidad
                )
            )

        _filter_conditions = models.Filter(should=conditions)

        docs = self.retriever.invoke(query)
        chunks = create_chunk_from_document(docs)
        return chunks
