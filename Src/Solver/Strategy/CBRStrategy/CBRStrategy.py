from Src.Solver.Strategy.Strategy import Strategy
from abc import abstractmethod


class CBRStrategy(Strategy):
    """
    Abstract strategy for Case-Based Reasoning (CBR).
    Uses a case base to help solve problems.
    """

    def __init__(self):
        super().__init__()
        # Base of past cases used for reasoning
        self.__caseBase = None

    def getCaseBase(self):
        """Return the case base."""
        return self.__caseBase

    def setCaseBase(self, base):
        """Set the case base."""
        self.__caseBase = base

    @abstractmethod
    def solve(self):
        """Solve the problem using the case base. Must be implemented by subclasses."""
        pass