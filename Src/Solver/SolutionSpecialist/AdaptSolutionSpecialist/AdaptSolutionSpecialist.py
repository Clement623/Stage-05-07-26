from abc import ABC, abstractmethod
from Src.CaseFile.Solutions.Solution import Solution


class AdaptSolutionSpecialist(ABC):
    def __init__(self):
        self.__solution = None

    @abstractmethod
    def adapt(self) -> any:
        pass

    def getSolution(self) -> Solution:
        if self.__solution is None:
            raise ValueError("solution not be defined")
        return self.__solution

    def setSolution(self, solution: Solution) -> None:
        if not isinstance(solution, Solution):
            raise TypeError("need a Solution Object")
        self.__solution = solution