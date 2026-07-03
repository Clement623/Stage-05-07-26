from Src.Solver.Specialist.Specialist import Specialist
from Src.ExtFile.Extension import Extension
from Src.CaseFile.Solutions.Solution import Solution
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.CaseFile.Solutions.SingleExtensionSolution import SingleExtensionSolution


class GroundedMergeSolutionSpecialist(Specialist):
    """
    Specialist that merges back the grounded extension into the solution
    found on the reduced problem (after removing the grounded arguments).
    """

    def __init__(self):
        super().__init__()
        # Grounded extension removed before solving the reduced problem
        self.__grounded_extension = None
        # Solution found on the reduced problem
        self.__reduced_solution = None

    def setGroundedExtension(self, grounded_ext: Extension) -> None:
        """Set the grounded extension."""
        if not isinstance(grounded_ext, Extension):
            raise TypeError("need an Extension object for grounded_ext")
        self.__grounded_extension = grounded_ext

    def getGroundedExtension(self) -> Extension:
        """Return the grounded extension."""
        return self.__grounded_extension

    def setReducedSolution(self, reduced_sol: Solution) -> None:
        """Set the solution of the reduced problem."""
        if reduced_sol is not None and not isinstance(reduced_sol, Solution):
            raise TypeError("need a Solution object for reduced_sol")
        self.__reduced_solution = reduced_sol

    def getReducedSolution(self) -> Solution:
        """Return the solution of the reduced problem."""
        return self.__reduced_solution

    def process(self):
        """Merge the grounded extension back into the reduced solution."""
        grounded_ext = self.getGroundedExtension()
        reduced_sol = self.getReducedSolution()

        if grounded_ext is None:
            raise ValueError("Grounded_ext not defined")

        # No reduced solution means the reduced problem had no answer
        if reduced_sol is None:
            return None

        grounded_args = grounded_ext.getExtArgument()
        answer = reduced_sol.getAnswer()

        # Boolean answers are independent of the grounded extension, return as-is
        if isinstance(reduced_sol, BooleanSolution):
            return BooleanSolution(reduced_sol.getAnswer())

        # Add the grounded arguments back into each extension of the set
        if isinstance(reduced_sol, SetExtensionSolution):
            merged_extensions = set()
            for ext in answer:
                new_args = ext.getExtArgument().union(grounded_args)
                merged_extensions.add(Extension(new_args, semantics=ext.getSemantics()))
            return SetExtensionSolution(merged_extensions)

        # Add the grounded arguments back into the single extension
        if isinstance(reduced_sol, SingleExtensionSolution):
            return SingleExtensionSolution(
                Extension(answer.getExtArgument().union(grounded_args), semantics=answer.getSemantics())
            )