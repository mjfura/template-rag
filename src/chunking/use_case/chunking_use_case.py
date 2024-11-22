from ..domain import ChunkingRepository
from src.loaders.domain import DocumentValue
from ..domain import ChunkValue
from src.embedding.domain import EmbeddingRepository
from src.embedding.domain import EmbeddingSentence
from typing import TypeVar, Generic

T = TypeVar("T")


class ChankingUseCase(Generic[T]):
    """
    ChankingUseCase class.

    This class is used to get the chunks from the documents.
    Within this class, we use the ChunkingRepository to get the chunks.
    """

    def __init__(
        self,
        chunking_repository: ChunkingRepository,
        embeding_repository: EmbeddingRepository[T],
    ):
        self.chunking_repository = chunking_repository
        self.embeding_repository = embeding_repository

    def get_chunks(self, documents: list[DocumentValue]) -> list[ChunkValue]:
        return self.chunking_repository.basic_chunking(documents)

    def semantic_chunking(
        self,
        documents: list[DocumentValue],
        buffer_size: int = 1,
        breakpoint_percentile: float = 95,
    ) -> list[ChunkValue]:
        combined_sentences = self.chunking_repository.combine_sentences(
            documents, buffer_size
        )
        print(f"combined_sentences: {combined_sentences}")
        embeddings = self.embeding_repository.embed_list(combined_sentences)
        print(f"embeddings: {embeddings}")
        embeddings_sentence = [
            EmbeddingSentence(combined_sentences[i], embeddings[i])
            for i in range(len(combined_sentences))
        ]
        print(f"embeddings_sentence: {embeddings_sentence}")
        chunks = self.chunking_repository.semantic_chunking(
            embeddings_sentence, breakpoint_percentile
        )
        return chunks
