from src.loaders.use_cases import LoaderUseCase
from src.chunking.use_case import ChankingUseCase
from src.vector_store_client.domain import VectorStoreRepository
from src.loaders.adapters import create_file_adapter
from streamlit.runtime.uploaded_file_manager import UploadedFile
from langchain_huggingface import HuggingFaceEmbeddings


class KnowledgeBaseUseCase:
    def __init__(
        self,
        loader_use_case: LoaderUseCase,
        chunking_use_case: ChankingUseCase[HuggingFaceEmbeddings],
        vector_store_repository: VectorStoreRepository,
    ):
        self.loader_use_case = loader_use_case
        self.chunking_use_case = chunking_use_case
        self.vector_store_repository = vector_store_repository

    def generate_knowledge_base(self, files: list[UploadedFile]) -> list[str]:
        ids: list[str] = []
        for file in files:
            file = create_file_adapter(file)
            docs = self.loader_use_case.upload_to_bucket(file)
            chunks = self.chunking_use_case.second_semantic_chunking(docs)
            ids = ids + self.vector_store_repository.add_documents(chunks)
        return ids
