from Src.Solver.Strategy.Strategy import Strategy
from Src.CaseFile.CaseBase import CaseBase
from Src.Solver.ProblemSpecialist.IsomorphismSpecialist import IsomorphismSpecialist
from Src.CaseFile.Problem import Problem
from Src.Solver.ProblemSpecialist.TransformationSpecialist.ArgumentTransformationSpecialist import (
    ArgumentTransformationSpecialist,
)
from Src.Solver.SolutionSpecialist.AdaptSolutionSpecialist.AdaptReductionSolution import AdaptReductionSolution


class TransformAndIsomorphStrategy(Strategy):
    def __init__(self, caseBase: CaseBase):
        super().__init__()
        self.__base = caseBase

    def getBase(self):
        return self.__base

    def tryDirectisomorphism(self, problem: Problem):
        base = self.getBase()
        specialist = IsomorphismSpecialist(base)
        specialist.setProblem(problem)
        return specialist.process()

    def tryAddArgument(self, problem: Problem):

        base = self.getBase()
        specialist = ArgumentTransformationSpecialist()
        specialist.setProblem(problem)
        newProblem = specialist.process()

        isoSpecialist = IsomorphismSpecialist(base)
        isoSpecialist.setProblem(newProblem)
        raw_solution = isoSpecialist.process()
        if raw_solution is not None:
            reduction_specialist = AdaptReductionSolution()
            reduction_specialist.setSolution(raw_solution)
            original_arguments = problem.getSituation().getAF().getArguments()
            reduction_specialist.setTargetArguments(original_arguments)

            return reduction_specialist.adapt()
        return None
    def solve(self, problem: Problem):
        results = self.tryDirectisomorphism(problem)
        if results is not None:
            return results

        results = self.tryAddArgument(problem)
        if results is not None:
            return results
