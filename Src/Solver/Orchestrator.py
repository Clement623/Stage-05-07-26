from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.Solver.Strategy.Strategy import Strategy


class Orchestrator:
    def __init__(self):
        self.__strategy: Strategy = None

    def setStrategy(self, strategy: Strategy) -> None:
        if not isinstance(strategy, Strategy):
            raise TypeError("need a Strategy Object")
        self.__strategy = strategy

    def solve(self, problem: Problem) -> Solution:
        if self.__strategy is None:
            raise ValueError("The strategy not be defined")

        return self.__strategy.solve(problem)
