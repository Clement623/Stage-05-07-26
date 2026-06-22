from .Strategy import Strategy
from Src.CaseFile.Solutions.UnresolvedSolution import UnresolvedSolution

class DirectResolutionStrategy(Strategy):
    def solve(self, problem,caseBase):
        sol=UnresolvedSolution()
        return sol
