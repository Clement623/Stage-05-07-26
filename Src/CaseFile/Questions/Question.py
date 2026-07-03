from abc import ABC, abstractmethod


# Abstract class to define a question
class Question(ABC):

    @abstractmethod
    def getAnswerType(self):
        """Return the expected type of the answer."""
        pass

    @abstractmethod
    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        """Check if two questions are equivalent under a given mapping."""
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        """Check equality between two questions."""
        pass

    @abstractmethod
    def __hash__(self) -> hash:
        """Hash of the question."""
        pass