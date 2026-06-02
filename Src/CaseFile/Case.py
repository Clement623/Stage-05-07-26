from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solutions.Solution import Solution
from Src.CaseFile.GraphConverter import GraphConverter

class Case:
    # A case take a problem and a solution in input
    def __init__(self, problem: Problem, solution: Solution):
        # Check the type of problem and solution
        if not isinstance(problem, Problem):
            raise TypeError("problem need to be a Problem")
        if not isinstance(solution, Solution):
            raise TypeError("solution need to be a Solution")
        self.__problem = problem
        self.__solution = solution
        self.__hashGraph=GraphConverter.computeWeisfeilerLehmanHash(self.getProblem().getSituation().getAF())

    def getProblem(self):
        return self.__problem

    def getSolution(self):
        return self.__solution

    def getHashGraph(self):
        return self.__hashGraph

    def __eq__(self, case2) -> bool:
        if isinstance(case2, Case):
            return (
                self.getSolution() == case2.getSolution()
                and self.getProblem() == case2.getProblem()
            )
        return False
