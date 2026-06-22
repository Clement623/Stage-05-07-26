from abc import ABC, abstractmethod
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.Solver.Specialist.Specialist import Specialist

class Strategy(ABC):
    def __init__(self):
        self.__ListSpecialist = []

    def getListSpecialist(self) -> list[Specialist]:
        return self.__ListSpecialist

    def iterSpecialist(self) -> iter:
        return iter(self.getListSpecialist())

    def addSpecialist(self, specialist: Specialist) -> None:
        if not isinstance(specialist, Specialist):
            raise TypeError("need a Specialist Object")
        self.getListSpecialist().append(specialist)

    @abstractmethod
    def solve(self, problem: Problem) -> Solution:
        pass
