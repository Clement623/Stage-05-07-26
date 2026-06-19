from abc import abstractmethod
from Src.Solver.Specialist.Specialist import Specialist


class SolutionAdaptationSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self):
        pass
