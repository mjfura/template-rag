from ..infrastructure import LangchainChunkingRepository
from ..use_case import ChankingUseCase
langchain_repository = LangchainChunkingRepository()
chunking_use_case = ChankingUseCase(langchain_repository)