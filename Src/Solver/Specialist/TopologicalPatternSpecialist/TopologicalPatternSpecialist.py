from abc import ABC, abstractmethod
from Src.Solver.Specialist.Specialist import Specialist


class TopologicalPatternSpecialist(Specialist, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self):
        pass
