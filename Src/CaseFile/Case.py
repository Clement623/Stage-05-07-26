from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.CaseFile.GraphConverter import GraphConverter


class Case:
    # Initialize the case with a problem and a solution
    def __init__(self, problem: Problem, solution: Solution):
        # Check if the problem is of type Problem
        if not isinstance(problem, Problem):
            raise TypeError("problem need to be a Problem")
        # Check if the solution is of type Solution
        if not isinstance(solution, Solution):
            raise TypeError("solution need to be a Solution")
        self.__problem = problem
        self.__solution = solution
        # Compute the hash value of the graph to check for isomorphism
        self.__graphHash = GraphConverter.computeWeisfeilerLehmanHash(
            self.getProblem().getSituation().getAF()
        )

    # Get the problem of the case
    def getProblem(self) -> Problem:
        return self.__problem

    # Get the solution of the case
    def getSolution(self) -> Solution:
        return self.__solution

    # Get the graph hash value
    def getGraphHash(self) -> str:
        return self.__graphHash

    # Check if two cases are equal
    def __eq__(self, other) -> bool:
        if isinstance(other, Case):
            return (
                self.getSolution() == other.getSolution()
                and self.getProblem() == other.getProblem()
            )
        return False
