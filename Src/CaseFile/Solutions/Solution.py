from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def getAnswer(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass
