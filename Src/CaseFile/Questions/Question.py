from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def getAnswerType(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass
