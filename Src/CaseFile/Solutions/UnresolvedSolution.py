from Src.CaseFile.Solutions.Solution import Solution

class UnresolvedSolution(Solution):
    def __init__(self, problem):
        super().__init__()
        self.__problem = problem

    def getProblem(self):
        return self.__problem

    def getAnswer(self):
        return set()
        
    def __eq__(self, other) -> bool:
        if isinstance(other, UnresolvedSolution):
            return self.getAnswer() == other.getAnswer()
        return False

    def __hash__(self) -> int:
        return hash(self.getAnswer())

    def __str__(self) -> str:
        return str(self.getAnswer())