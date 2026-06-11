import copy
from abc import abstractmethod

from Src.CaseFile.Problem import Problem
from Src.Solver.Specialist.Specialist import Specialist


class TransformationSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def applyTransformation(self, af):
        pass

    def process(self) -> Problem:

        problem = self.getProblem()
        newProblem = copy.deepcopy(problem)
        Af = newProblem.getSituation().getAF()
        self.applyTransformation(Af)

        return newProblem
