from abc import ABC, abstractmethod
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.Solver.Specialist.Specialist import Specialist

class Strategy(ABC):
    def __init__(self):
        self.__specialists = []

    def getSpecialists(self) -> list[Specialist]:
        return self.__specialists

    def iterSpecialists(self) -> iter:
        return iter(self.getSpecialists())

    def addSpecialist(self, specialist: Specialist) -> None:
        if not isinstance(specialist, Specialist):
            raise TypeError("need a Specialist Object")
        self.getSpecialists().append(specialist)

    @abstractmethod
    def solve(self, problem: Problem) -> Solution:
        pass
