from abc import ABC, abstractmethod


# abstract class to define a question
class Question(ABC):
    @abstractmethod
    def getAnswerType(self):
        pass

    @abstractmethod
    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    @abstractmethod
    def __hash__(self) -> hash:
        pass
