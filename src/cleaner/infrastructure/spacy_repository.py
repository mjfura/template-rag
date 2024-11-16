from ..domain import CleanerRepository
import spacy
# antes de corred la celda: python -m spacy download en_core_web_sm
class SpacyRepository(CleanerRepository):
    def __init__(self):
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
    

    