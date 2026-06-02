from abc import ABC, abstractmethod
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.Solver.Specialist.Specialist import Specialist

class Strategy(ABC):
    def __init__(self):
        self.specialists = [] 

    def addSpecialist(self, specialist: Specialist):
        self.specialists.append(specialist)

    @abstractmethod
    def solve(self, problem: Problem) -> Solution:
        pass
    
