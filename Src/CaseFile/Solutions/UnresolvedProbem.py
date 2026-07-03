from Src.CaseFile.Solutions.Solution import Solution


class UnresolvedProblem(Solution):

    def __init__(self, problem):
        """Init with the problem that could not be solved."""
        super().__init__()
        self.__problem = problem

    def getProblem(self):
        """Return the unresolved problem."""
        return self.__problem

    def getAnswer(self):
        """Return an empty answer, since the problem is unresolved."""
        return set()

    def __eq__(self, other) -> bool:
        """Check equality between two UnresolvedProblem objects."""
        if isinstance(other, UnresolvedProblem):
            return self.getAnswer() == other.getAnswer()
        return False

    def __hash__(self) -> int:
        """Hash based on the answer."""
        return hash(self.getAnswer())

    def __str__(self) -> str:
        """String representation of the solution."""
        return str(self.getAnswer())