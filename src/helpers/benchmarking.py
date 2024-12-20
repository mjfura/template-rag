from src.app.main_instances import embedding_repository, openai_repository
from src.application.rag_use_case import RAGUseCase
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)
from datasets import Dataset
from pandas import DataFrame


def evaluate_retrievers(
    application: RAGUseCase, ground_truth: list[dict[str, str]] = []
) -> tuple[DataFrame, DataFrame]:
    # Parsear preguntas y respuestas
    contexts_basic = []
    answers_basic = []
    questions = [element["question"] for element in ground_truth]
    answers_ground_truth = [element["reference"] for element in ground_truth]
    # Inferencia
    for element in ground_truth:
        answers_basic.append(application.pipeline_rag(element["question"]))
        contexts_basic.append(
            [
                docs.content
                for docs in application.retriever.basic_retrieve(element["question"])
            ]
        )

    data_basic = {
        "question": questions,
        "answer": answers_basic,
        "reference": answers_ground_truth,
        "retrieved_contexts": contexts_basic,
    }

    # Convert dict to dataset
    dataset_basic = Dataset.from_dict(data_basic)

    result_basic_retriever = evaluate(
        dataset=dataset_basic,
        llm=openai_repository.llm,
        embeddings=embedding_repository.get_model(),
        metrics=[
            context_recall,
            faithfulness,
            answer_relevancy,
            context_precision,
        ],
    )

    df_basic_retriever = result_basic_retriever.to_pandas()

    contexts_advanced = []
    answers_advanced = []
    # Inferencia
    for element in ground_truth:
        answers_advanced.append(application.pipeline_rag_advanced(element["question"]))
        entities = application.cleaner_repository.get_entities(element["question"])
        contexts_advanced.append(
            [
                docs.content
                for docs in application.retriever.advanced_retrieve(
                    element["question"], entities
                )
            ]
        )

    data_advanced = {
        "question": questions,
        "answer": answers_advanced,
        "reference": answers_ground_truth,
        "retrieved_contexts": contexts_advanced,
    }

    # Convert dict to dataset
    dataset_advanced = Dataset.from_dict(data_advanced)

    result_advanced_retriever = evaluate(
        dataset=dataset_advanced,
        llm=openai_repository.llm,
        embeddings=embedding_repository.get_model(),
        metrics=[
            context_recall,
            faithfulness,
            answer_relevancy,
            context_precision,
        ],
    )
    df_advanced_retriever = result_advanced_retriever.to_pandas()

    return df_basic_retriever, df_advanced_retriever
