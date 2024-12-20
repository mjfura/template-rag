from ..domain import ChainRepository
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain_openai import ChatOpenAI


class OpenAIRepository(ChainRepository):
    """
    OpenAIRepository class.

    This class is used to interact with the OpenAI API.
    """

    def __init__(self) -> None:
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.prompt = hub.pull("rlm/rag-prompt")
        self.rewrite_prompt = hub.pull("langchain-ai/rewrite")

        self.rag_chain = (
            {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def evaluate_prompt(self, question: str, context: str) -> str:
        """
        Evaluate prompt method.

        This method receives a question and a context and returns the answer.

        Args:
            question (str): The question that will be answered.
            context (str): The context in which the question will be answered.

        Returns:
            str: The answer to the question.
        """
        print("Evaluating prompt BASIC ", question, context)
        response = self.rag_chain.invoke({"context": context, "question": question})
        if not isinstance(response, str):
            raise TypeError(f"Expected response to be str, but got {type(response)}")
        return response

    def evaluate_advanced_prompt(self, question: str, context: str) -> str:
        """
        Evaluate prompt method.

        This method receives a question and a context and returns the answer.

        Args:
            question (str): The question that will be answered.
            context (str): The context in which the question will be answered.

        Returns:
            str: The answer to the question.
        """
        base_prompt = f"Context: {context}\nQuestion: {question}"
        print(f"Base prompt: {base_prompt}")
        # Mejorar el prompt usando el modelo de rewriting
        print(f"Prompt: {self.rewrite_prompt}")
        improved_prompt = self.rewrite_prompt.format(x=base_prompt)
        print(f"Improved prompt: {improved_prompt}")
        # Separar el contexto mejorado y la pregunta mejorada
        # improved_context, improved_question = self._split_improved_prompt(improved_prompt)
        response = self.rag_chain.invoke({"context": context, "question": question})
        if not isinstance(response, str):
            raise TypeError(f"Expected response to be str, but got {type(response)}")

        return response
