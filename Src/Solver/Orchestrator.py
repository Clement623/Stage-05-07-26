from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.Solver.Strategy.Strategy import Strategy


class Orchestrator:
    """
    Orchestrator that delegates problem solving to a chosen strategy.
    """

    def __init__(self):
        # Strategy used to solve problems
        self.__strategy: Strategy = None

    def setStrategy(self, strategy: Strategy) -> None:
        """Set the strategy to use for solving."""
        if not isinstance(strategy, Strategy):
            raise TypeError("need a Strategy Object")
        self.__strategy = strategy

    def solve(self, problem: Problem, caseBase=None) -> Solution | Problem:
        """Solve the problem using the current strategy."""
        if self.__strategy is None:
            raise ValueError("The strategy not be defined")

        return self.__strategy.solve(problem, caseBase)