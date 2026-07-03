from Src.Solver.Specialist.Specialist import Specialist
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.ExtFile.Extension import Extension


class PolarityDecompressionSpecialist(Specialist):
    """
    Specialist that expands extensions back using saved polarity patterns
    (chains of arguments where the status of one implies the status of the next).
    """

    def __init__(self):
        super().__init__()
        # List of polarity patterns to apply
        self.__patterns = None
        # Solution found on the reduced problem
        self.__reduced_solution = None

    def setPatterns(self, patterns: list):
        """Set the list of polarity patterns."""
        self.__patterns = patterns

    def getPatterns(self) -> list:
        """Return the list of polarity patterns."""
        return self.__patterns

    def setReducedSolution(self, reduced_sol):
        """Set the solution of the reduced problem."""
        self.__reduced_solution = reduced_sol

    def getReducedSolution(self):
        """Return the solution of the reduced problem."""
        return self.__reduced_solution

    def process(self):
        """Expand each extension using the polarity patterns."""
        patterns = self.getPatterns()
        reduced_sol = self.getReducedSolution()

        if patterns is None or reduced_sol is None:
            return None

        if isinstance(reduced_sol, SetExtensionSolution):
            # Retrieve the semantics from the first extension if available
            semantics = list(reduced_sol.getAnswer())[0].getSemantics() if reduced_sol.getAnswer() else None
            merged_extensions = set()

            base_answers = reduced_sol.getAnswer()

            # If no extensions, start from an empty one
            if not base_answers:
                base_answers = [Extension(set(), semantics=semantics)]

            # Apply patterns to each extension
            for ext in base_answers:
                current_args = set(ext.getExtArgument())

                for pattern in patterns:
                    start_arg = pattern[0]

                    if start_arg in current_args:
                        # Start is accepted → even-indexed args are in, odd-indexed are out
                        for i in range(0, len(pattern), 2):
                            current_args.add(pattern[i])
                        for i in range(1, len(pattern), 2):
                            current_args.discard(pattern[i])
                    else:
                        # Start is rejected → odd-indexed args are in, even-indexed are out
                        for i in range(1, len(pattern), 2):
                            current_args.add(pattern[i])
                        for i in range(0, len(pattern), 2):
                            current_args.discard(pattern[i])

                merged_extensions.add(Extension(current_args, semantics=semantics))

            return SetExtensionSolution(merged_extensions)

        # Fallback: nothing to decompress, return solution unchanged
        return reduced_sol