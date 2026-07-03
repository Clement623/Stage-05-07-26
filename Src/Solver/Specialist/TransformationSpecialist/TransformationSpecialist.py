
from abc import abstractmethod

from Src.CaseFile.Problem import Problem
from Src.Solver.Specialist.Specialist import Specialist


class TransformationSpecialist(Specialist):
    """Abstract specialist that transforms a problem before it is solved."""
    def __init__(self):
        super().__init__()

    @abstractmethod
    def applyTransformation(self, af):
        pass

    def process(self) -> Problem:
        pass
