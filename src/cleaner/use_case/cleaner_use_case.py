from ..domain import CleanerRepository
class CleanerUseCase:
    """
    CleanerUseCase class.
    
    This class is used to clean the text.
    Within this class, we use the CleanerRepository to clean the text.
    
    Args:
        cleaner_repo (CleanerRepository): The repository that will be used to clean the text.
        
    Attributes:
        cleaner_repo (CleanerRepository): The repository that will be used to clean the text.
    """
    def __init__(self, cleaner_repo:CleanerRepository):
        self.cleaner_repo = cleaner_repo

    def clean_text(self, text:str)->str:
        """
        Clean text method.
        
        This method receives a text and returns the same text cleaned.
        
        Args:
            text (str): The text that will be cleaned.
            
        Returns:
            str: The text cleaned.
        """
        text_cleaned=self.cleaner_repo.to_lower(text)
        text_cleaned=self.cleaner_repo.remove_stopwords(text_cleaned)
        text_cleaned=self.cleaner_repo.lemmatization(text_cleaned)
        return text_cleaned
        