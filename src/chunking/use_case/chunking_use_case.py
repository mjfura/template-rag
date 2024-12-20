from ..domain import ChunkingRepository
from src.loaders.domain import DocumentValue
from ..domain import ChunkValue
from src.embedding.domain import EmbeddingRepository
from src.embedding.domain import EmbeddingSentence
from src.cleaner.domain import CleanerRepository
from typing import TypeVar, Generic
import re
from sentence_transformers import util
from tqdm import tqdm

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
        cleaner_repository: CleanerRepository,
    ):
        self.chunking_repository = chunking_repository
        self.embeding_repository = embeding_repository
        self.cleaner_repository = cleaner_repository

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
        embeddings = self.embeding_repository.embed_list(combined_sentences)
        embeddings_sentence = [
            EmbeddingSentence(combined_sentences[i], embeddings[i])
            for i in range(len(combined_sentences))
        ]
        chunks = self.chunking_repository.semantic_chunking(
            embeddings_sentence, breakpoint_percentile
        )
        return chunks

    def second_semantic_chunking(
        self, documents: list[DocumentValue], chunk_size: int = 2500
    ) -> list[ChunkValue]:
        model = self.embeding_repository
        chunks = []

        for document in tqdm(documents):
            content = document.content
            metadata = document.metadata

            paragraphs = re.split(r"\n{2,}", content)
            current_chunk = ""
            current_size = 0

            for paragraph in paragraphs:
                sentences = re.split(
                    r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", paragraph
                )

                for sentence in sentences:
                    sentence_embedding = model.embed_tensor(sentence)

                    if current_chunk:
                        current_chunk_embedding = model.embed_tensor(current_chunk)
                        similarity = util.cos_sim(
                            sentence_embedding, current_chunk_embedding
                        ).item()
                    else:
                        similarity = 1.0

                    if (current_size + len(sentence) <= chunk_size) and (
                        similarity > 0.65
                    ):
                        current_chunk += " " + sentence
                        current_size += len(sentence)
                    else:
                        if current_chunk.strip():
                            entities = self.cleaner_repository.get_entities(
                                current_chunk.strip()
                            )
                            chunk = ChunkValue(
                                content=current_chunk.strip(),
                                metadata={"entities": entities, **metadata},
                            )
                            chunks.append(chunk)
                        current_chunk = sentence
                        current_size = len(sentence)

            if current_chunk.strip():
                chunk = ChunkValue(
                    content=current_chunk.strip(),
                    metadata={
                        "entities": self.cleaner_repository.get_entities(
                            current_chunk.strip()
                        ),
                        **metadata,
                    },
                )
                chunks.append(chunk)
        return chunks
