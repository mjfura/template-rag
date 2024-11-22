from abc import ABC
from dataclasses import dataclass
from typing import Dict


@dataclass
class FileEntity(ABC):
    """
    FileEntity is a dataclass that represents a file entity.

    Attributes:
    - name: str
    - type: str
    - size: int
    - content: bytes
    """

    name: str
    type: str
    size: int
    content: bytes


@dataclass
class DocumentEntity(ABC):
    """
    DocumentEntity is a dataclass that represents a document entity.

    Attributes:
    - content: str
    - metadata: dict
    """

    content: str
    metadata: Dict[str, str]
