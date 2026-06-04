from Src.Solver.SolutionSpecialist.AdaptSolutionSpecialist.AdaptSolutionSpecialist import AdaptSolutionSpecialist
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.ListExtensionSolution import ListExtensionSolution
from Src.Core.Argument import Argument
from Src.ExtFile.Extension import Extension

class AdaptIsomorphSolution(AdaptSolutionSpecialist):
    def __init__(self):
        super().__init__()
        self.__mapping=None

    def setMapping(self,mapping:dict):
        self.__mapping=mapping

    def getInverseMapping(self) -> dict:
        """Returns the inverted mapping: {case_node: problem_node}"""
        if self.__mapping is None:
            raise ValueError("Mapping not defined, call setMapping() first")
        return {v: k for k, v in self.__mapping.items()}

    def adapt(self):
        solution = self.getSolution()
        inverse = self.getInverseMapping()

        if isinstance(solution,BooleanSolution):
            return solution
        
        if isinstance(solution, ListExtensionSolution):
            adapted_extensions = []
            for extension in solution.getAnswer():
                new_args = set()
                for arg in extension:
                    original_index = arg.getIndex()
                    new_index = inverse.get(original_index, original_index)
                    new_args.add(Argument(new_index))
                adapted_extensions.append(Extension(new_args))
            return ListExtensionSolution(adapted_extensions)




