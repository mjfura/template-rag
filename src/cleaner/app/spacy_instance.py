from ..infrastructure import SpacyRepository
from ..use_case import CleanerUseCase

spacy_repository = SpacyRepository()
cleaner_use_case = CleanerUseCase(spacy_repository)
