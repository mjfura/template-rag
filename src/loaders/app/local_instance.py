from src.loaders.infrastructure import LocalRepository
from src.loaders.use_cases import LoaderUseCase

local_repository = LocalRepository()
loader_use_case = LoaderUseCase(local_repository)
