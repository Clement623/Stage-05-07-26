from Src.Solver.Strategy.Strategy import Strategy
from abc import abstractmethod


class CBRStrategy(Strategy):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def solve(self):
        pass
