from Src.CaseFile.Problem import Problem
from abc import ABC, abstractmethod


class Specialist(ABC):
    """
    Abstract base class for all specialists.
    A specialist works on a problem and processes it in some way
    (transformation, decomposition, recomposition, etc.).
    """

    def __init__(self):
        super().__init__()
        # Problem currently assigned to this specialist
        self.__problem = None

    @abstractmethod
    def process(self):
        """Process the problem. Must be implemented by subclasses."""
        pass

    def getProblem(self) -> Problem:
        """Return the current problem."""
        if self.__problem is None:
            raise ValueError("problem not be defined")
        return self.__problem

    def setProblem(self, problem: Problem) -> None:
        """Set the problem to work on."""
        if not isinstance(problem, Problem):
            raise TypeError("need a Problem Object")
        self.__problem = problem