from ..domain import ChunkingRepository
from ..domain.value import ChunkValue
from src.embedding.domain import EmbeddingSentence
from src.loaders.domain import DocumentValue
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np


class LangchainChunkingRepository(ChunkingRepository):
    """
    LangchainChunkingRepository class.

    This class implements the ChunkingRepository abstract class from the domain layer.

    It is used to chunk the documents into smaller pieces using Langchain as our infrastructure.
    """

    def basic_chunking(self, documents: list[DocumentValue]) -> list[ChunkValue]:
        """
        Basic chunking method.

        This method receives a list of DocumentValue objects and returns a list of ChunkValue objects. These DocumentValue were created by the LoaderUseCase.
        Basically, each DocumentValue object represents only one page of the file.

        Args:
            documents (list[DocumentValue]): A list of DocumentValue objects.

        Returns:
            list[ChunkValue]: A list of ChunkValue objects.
        """
        return [
            ChunkValue(content=doc.content, metadata=doc.metadata) for doc in documents
        ]

    def combine_sentences(
        self, documents: list[DocumentValue], buffer_size: int
    ) -> list[str]:
        """
        Combined sentences method.

        This method receives a list of sentences and a buffer size, and returns a list of combined sentences.

        Args:
            documents (list[DocumentValue]): A list of DocumentValue objects.
            buffer_size (int): The buffer size.

        Returns:
            list[str]: A list of combined sentences.
        """
        print("documents queantity: ", len(documents))
        all_sentences = []
        for doc in documents:
            sentences = re.split(r"(?<=[.?!])\s+", doc.content)
            all_sentences.extend(sentences)
        combined_sentences = []
        for i, sentence in enumerate(all_sentences):
            combined = " ".join(
                all_sentences[max(0, i - buffer_size) : i + buffer_size + 1]
            )
            combined_sentences.append(combined)
        print(f"combined_sentences: {len(combined_sentences)}")
        return combined_sentences

    def semantic_chunking(
        self, embeddings_sentence: list[EmbeddingSentence], breakpoint_percentile: float
    ) -> list[ChunkValue]:
        """
        Semantic chunking method.

        This method receives a list of EmbeddingSentence objects and a breakpoint percentile, and returns a list of ChunkValue objects.

        Args:
            embeddings_sentence (list[EmbeddingSentence]): A list of EmbeddingSentence objects.
            breakpoint_percentile (float): The breakpoint percentile.

        Returns:
            list[ChunkValue]: A list of ChunkValue objects.
        """

        similarities = []
        print(f"embeddings_sentence: {len(embeddings_sentence)}")
        for i in range(len(embeddings_sentence) - 1):
            embedding_current = embeddings_sentence[i].embedding
            embedding_next = embeddings_sentence[i + 1].embedding
            similarity = cosine_similarity([embedding_current], [embedding_next])[0][0]
            similarities.append(1 - similarity)  # Convertimos a distancia
        breakpoint_threshold = np.percentile(similarities, breakpoint_percentile)
        indices_above_thresh = [
            i for i, x in enumerate(similarities) if x > breakpoint_threshold
        ]

        chunks: list[ChunkValue] = []
        start_index = 0

        for index in indices_above_thresh:
            end_index = index
            group = embeddings_sentence[start_index : end_index + 1]
            combined_text = " ".join([d.sentence for d in group])
            chunks.append(ChunkValue(content=combined_text, metadata={}))
            start_index = index + 1

        if start_index < len(embeddings_sentence):
            combined_text = " ".join(
                [d.sentence for d in embeddings_sentence[start_index:]]
            )
            chunks.append(ChunkValue(content=combined_text, metadata={}))
        print(f"chunks quantity: {len(chunks)}")
        return chunks
