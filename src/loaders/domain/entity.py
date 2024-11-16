from abc import ABC
from dataclasses import dataclass

@dataclass
class FileEntity(ABC):
    name: str
    type: str
    size: int
    content: bytes

@dataclass
class DocumentEntity(ABC):
    content:str
    metadata: dict