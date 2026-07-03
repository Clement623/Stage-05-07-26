from abc import ABC, abstractmethod


# Abstract class to define a solution
class Solution(ABC):

    @abstractmethod
    def getAnswer(self) -> any:
        """Return the answer of the solution."""
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        """Check equality between two solutions."""
        pass

    @abstractmethod
    def __hash__(self) -> hash:
        """Hash of the solution."""
        pass