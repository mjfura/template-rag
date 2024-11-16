from src.loaders.infrastructure import LocalRepository,LangchainLoaderRepository
from src.loaders.use_cases import LoaderUseCase

local_repository = LocalRepository()
langchain_repository = LangchainLoaderRepository()
loader_use_case = LoaderUseCase(langchain_repository,local_repository)
