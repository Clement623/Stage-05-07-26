from abc import ABC, abstractmethod
from Src.CaseFile.Problem import Problem


class SolverStrategy(ABC):
    @abstractmethod
    def solve(self, problem: Problem):
        pass
