from .SolutionAdaptationSpecialist import SolutionAdaptationSpecialist
from Src.ExtFile.Extension import Extension
from Src.CaseFile.Solutions.Solution import Solution
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.CaseFile.Solutions.SingleExtensionSolution import SingleExtensionSolution

class GroundedMergeSolutionSpecialist(SolutionAdaptationSpecialist):
    def __init__(self):
        super().__init__()
        self.__grounded_extension = None
        self.__reduced_solution = None

    def setGroundedExtension(self, grounded_ext: Extension) -> None:
        if not isinstance(grounded_ext, Extension):
            raise TypeError("need an Extension object for grounded_ext")
        self.__grounded_extension = grounded_ext

    def getGroundedExtension(self) -> Extension:
        return self.__grounded_extension

    def setReducedSolution(self, reduced_sol: Solution) -> None:
        if reduced_sol is not None and not isinstance(reduced_sol, Solution):
            raise TypeError("need a Solution object for reduced_sol")
        self.__reduced_solution = reduced_sol

    def getReducedSolution(self) -> Solution:
        return self.__reduced_solution

    def process(self):
        grounded_ext = self.getGroundedExtension()
        reduced_sol = self.getReducedSolution()
        if grounded_ext is None:
                    raise ValueError("Grounded_ext not defined")
        if reduced_sol is None:
            return None

        grounded_args = grounded_ext.getExtArgument()
        answer = reduced_sol.getAnswer()

        if isinstance(reduced_sol, BooleanSolution):
            return BooleanSolution(reduced_sol.getAnswer())

        if isinstance(reduced_sol,SetExtensionSolution):
            merged_extensions = set()
            for ext in answer:
                new_args = ext.getExtArgument().union(grounded_args)
                merged_extensions.add(Extension(new_args, semantics=ext.getSemantics()))         
            return SetExtensionSolution(merged_extensions)
        
        if isinstance(reduced_sol,SingleExtensionSolution):
            return SingleExtensionSolution(Extension(answer.getExtArgument().union(grounded_args),semantics=answer.getSemantics()))