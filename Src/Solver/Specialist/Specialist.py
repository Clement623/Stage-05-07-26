from Src.CaseFile.Problem import Problem
from abc import ABC,abstractmethod


class Specialist(ABC):
    def __init__(self):
        super().__init__()
        self.__problem = None

    @abstractmethod
    def process(self):
        pass

    def getProblem(self) -> Problem:
        if self.__problem is None:
            raise ValueError("problem not be defined")
        return self.__problem

    def setProblem(self, problem: Problem) -> None:
        if not isinstance(problem, Problem):
            raise TypeError("need a Problem Object")
        self.__problem = problem
