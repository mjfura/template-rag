from abc import ABC, abstractmethod


class ChainRepository(ABC):
    """
    Abstract class for the ChainRepository.

    This class defines the abstract methods that must be implemented by the ChainRepository in the infrastructure layer.
    """

    @abstractmethod
    def evaluate_prompt(self, question: str, context: str) -> str:
        pass

    @abstractmethod
    def evaluate_advanced_prompt(self, question: str, context: str) -> str:
        pass
