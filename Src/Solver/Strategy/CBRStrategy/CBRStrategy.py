from Src.Solver.Strategy.Strategy import Strategy
from abc import abstractmethod


class CBRStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.__caseBase=None

    def getCaseBase(self):
        return self.__caseBase
    
    def setCaseBase(self,base):
        self.__caseBase=base

    @abstractmethod
    def solve(self):
        pass
