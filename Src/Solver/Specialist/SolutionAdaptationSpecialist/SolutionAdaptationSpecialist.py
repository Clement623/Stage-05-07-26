from abc import ABC, abstractmethod


class SolutionAdaptationSpecialist(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self):
        pass
