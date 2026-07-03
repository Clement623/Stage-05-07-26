from Src.CaseFile.Solutions.UnresolvedProbem import UnresolvedProblem

from .Strategy import Strategy


class DirectResolutionStrategy(Strategy):
    """
    Strategy that resolve a problem from scratch, use in last
    """

    def solve(self, problem, caseBase):
        """Return an unresolved problem temporally, change with a solution after"""
        sol = UnresolvedProblem()
        return sol
