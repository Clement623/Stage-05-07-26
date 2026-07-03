from .Specialist import Specialist
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
import itertools
from Src.ExtFile.Extension import Extension


class WCCRecompositionSpecialist(Specialist):
    """
    Recomposes the global solution from the partial solutions
    of each connected component.
    """

    def __init__(self):
        super().__init__()
        # Partial solutions to recompose
        self.__solutions = None

    def setSolutions(self, solutions):
        """Set the list of partial solutions."""
        self.__solutions = solutions

    def getSolutions(self):
        """Return the list of partial solutions."""
        return self.__solutions

    def process(self):
        """Build the final solution from the partial ones."""
        solutions = self.getSolutions()

        if not solutions:
            return None

        # Boolean case: true only if all components are true
        # Note: not valid for all question types, may need filtering later
        if isinstance(solutions[0], BooleanSolution):
            return BooleanSolution(all(sol.getAnswer() for sol in solutions))

        # Set of extensions case
        if isinstance(solutions[0], SetExtensionSolution):
            # Extensions per component
            components_extensions = [list(sol.getAnswer()) for sol in solutions]
            merged_extensions = set()

            # Combine one extension per component
            for combo in itertools.product(*components_extensions):
                combined_args = set()
                semantics = combo[0].getSemantics() if combo else None

                # Merge arguments together
                for ext in combo:
                    combined_args.update(ext.getExtArgument())

                merged_extensions.add(Extension(combined_args, semantics=semantics))

            return SetExtensionSolution(merged_extensions)

        # Fallback: return first solution
        return solutions[0]