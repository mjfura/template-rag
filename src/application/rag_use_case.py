from src.vector_store_client.domain import VectorStoreRepository
from src.chain.domain import ChainRepository
from src.retrievers.domain import RetrieverRepository
from src.cleaner.infrastructure import SpacyRepository


class RAGUseCase:
    def __init__(
        self,
        vector_store_repository: VectorStoreRepository,
        retriever: RetrieverRepository,
        chain_repository: ChainRepository,
        cleaner_repository: SpacyRepository,
    ):
        self.vector_store_repository = vector_store_repository
        self.chain_repository = chain_repository
        self.retriever = retriever
        self.cleaner_repository = cleaner_repository

    def pipeline_rag(self, question: str) -> str:
        chunks = self.retriever.basic_retrieve(question)
        context = ""
        for chunk in chunks:
            context += chunk.content + " "
        return self.chain_repository.evaluate_prompt(question, context)

    def pipeline_rag_advanced(self, question: str) -> str:
        entities = self.cleaner_repository.get_entities(question)
        chunks = self.retriever.advanced_retrieve(question, entities)
        context = ""
        for chunk in chunks:
            context += chunk.content + " "
        return self.chain_repository.evaluate_advanced_prompt(question, context)
