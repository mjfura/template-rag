from ..domain import CleanerRepository

import spacy


class SpacyRepository(CleanerRepository):
    """
    SpacyRepository class.

    This class is used to clean the text using Spacy.

    It implements the CleanerRepository abstract class from the domain layer.

    Args:
        CleanerRepository (ABC): The abstract class that represents the cleaner

    Attributes:
        nlp (spacy.lang.en.English): The Spacy model that will be used to clean the text.
    """

    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_sm")

    def to_lower(self, text: str) -> str:
        return text.lower()

    def remove_stopwords(self, text: str) -> str:
        doc = self.nlp(text)
        tokens = [token.text for token in doc if not token.is_stop]
        return " ".join(tokens)

    def lemmatization(self, text: str) -> str:
        doc = self.nlp(text)
        tokens = [token.lemma_ for token in doc]
        return " ".join(tokens)
