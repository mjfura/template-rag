from src.embedding.infrastructure import HuggingFaceEmbeddingRepository
from src.vector_store_client.infrastructure import QdrantVectorStoreRepository
from src.chain.infrastructure import OpenAIRepository
from src.retrievers.infrastructure import LangchainRetrieverRepository
from src.cleaner.infrastructure import SpacyRepository
from src.application import RAGUseCase, KnowledgeBaseUseCase
from src.loaders.use_cases import LoaderUseCase
from src.loaders.infrastructure import LangchainLoaderRepository, LocalRepository
from src.chunking.use_case import ChankingUseCase
from src.chunking.infrastructure import LangchainChunkingRepository
from src.embedding.infrastructure import SentenceTransformerEmbeddingRepository
from dotenv import load_dotenv

load_dotenv()

embedding_repository = HuggingFaceEmbeddingRepository()
qdrant_repository = QdrantVectorStoreRepository(
    embedding_repository.get_model(), "archivos_uk"
)
openai_repository = OpenAIRepository()
retriever_repository = LangchainRetrieverRepository(
    qdrant_repository.vector_store.as_retriever(search_kwargs={"k": 10})
)
cleaner_repository = SpacyRepository()
application = RAGUseCase(
    qdrant_repository, retriever_repository, openai_repository, cleaner_repository
)
loader_repository = LangchainLoaderRepository()
bucket_repository = LocalRepository()
loader_use_case = LoaderUseCase(loader_repository, bucket_repository)
chunking_repository = LangchainChunkingRepository()
sentence_embedding_repository = SentenceTransformerEmbeddingRepository()
chunking_use_case = ChankingUseCase(
    chunking_repository, sentence_embedding_repository, cleaner_repository
)
knowledge_base_use_case = KnowledgeBaseUseCase(
    loader_use_case, chunking_use_case, qdrant_repository
)
