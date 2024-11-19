from abc import ABC, abstractmethod
class CleanerRepository(ABC):
    """
    Abstract class that represents the cleaner repository.
    
    This class should be implemented by any class that will be used to clean text in the infrastructure layer.
    """
    @abstractmethod
    def remove_stopwords(self, text:str) -> str:
        """
        Remove stopwords abstract method.
        
        This method receives a text and returns the same text without stopwords.
        
        Args:
            text (str): The text that will be cleaned.
            
        Returns:
            str: The text without stopwords.
        """
        pass
    
    @abstractmethod
    def to_lower(self, text:str) -> str:
        """
        To lower abstract method.
        
        This method receives a text and returns the same text in lower case.
        
        Args:
            text (str): The text that will be cleaned.
            
        Returns:
            str: The text in lower case.
        """
        pass
    
    @abstractmethod
    def lemmatization(self, text:str) -> str:
        """
        Lemmatization abstract method.
        
        This method receives a text and returns the same text with lemmatization.
        
        Args:
            text (str): The text that will be cleaned.
            
        Returns:
            str: The text with lemmatization.
        """
        pass