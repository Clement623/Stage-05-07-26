from abc import ABC, abstractmethod


# Abstract class to define a solution
class Solution(ABC):
    @abstractmethod
    def getAnswer(self) -> any:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    @abstractmethod
    def __hash__(self) -> hash:
        pass
