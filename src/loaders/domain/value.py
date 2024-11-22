from .entity import FileEntity, DocumentEntity


class FileValue(FileEntity):
    """
    FileValue is a dataclass that represents a file value.

    Attributes:
    - name: str
    - type: str
    - size: int
    - content: bytes

    """

    pass


class DocumentValue(DocumentEntity):
    """
    DocumentValue is a dataclass that represents a document value.

    Attributes:
    - content: str
    - metadata: dict
    """

    pass
