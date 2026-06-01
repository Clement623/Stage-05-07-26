from Src.CaseFile.Solver.SolverStrategy import SolverStrategy
from Src.CaseFile.Problem import Problem


# class to use for start a solving with a strategy
class Solver:
    def __init__(self, strategy: SolverStrategy):
        if not isinstance(strategy, SolverStrategy):
            raise TypeError("need a SolverStrategy")
        self.__strategy = strategy

    def getStrategy(self):
        return self.__strategy

    def solve(self, problem: Problem):
        if not isinstance(problem, Problem):
            raise TypeError("need a Problem")
        return self.getStrategy().solve(problem)

    def setStrategy(self, strategy: SolverStrategy):
        if not isinstance(strategy, SolverStrategy):
            raise TypeError("need a SolverStrategy")
        self.__strategy = strategy
