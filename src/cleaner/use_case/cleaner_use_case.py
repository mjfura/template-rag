from ..domain import CleanerRepository
class CleanerUseCase:
    def __init__(self, cleaner_repo:CleanerRepository):
        self.cleaner_repo = cleaner_repo

    def clean_text(self, text:str)->str:
        text_cleaned=self.cleaner_repo.to_lower(text)
        text_cleaned=self.cleaner_repo.remove_stopwords(text_cleaned)
        text_cleaned=self.cleaner_repo.lemmatization(text_cleaned)
        return text_cleaned
        