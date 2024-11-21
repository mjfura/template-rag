
from dataclasses import dataclass

@dataclass
class EmbeddingSentenceEntity:
    """
    EmbeddingSentenceEntity is a dataclass that represents an embedding sentence entity.
    
    Attributes:
    - sentence: str
    - embedding: list
    """
    sentence: str
    embedding: list[float]