from dataclasses import dataclass

@dataclass
class ChunkEntity:
    content: str
    metadata: dict