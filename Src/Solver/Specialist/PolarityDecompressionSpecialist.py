from Src.Solver.Specialist.Specialist import Specialist
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.ExtFile.Extension import Extension

class PolarityDecompressionSpecialist(Specialist):
    def __init__(self):
        super().__init__()
        self.__patterns = None
        self.__reduced_solution = None

    def setPatterns(self, patterns: list):
        self.__patterns = patterns

    def getPatterns(self) -> list:
        return self.__patterns

    def setReducedSolution(self, reduced_sol):
        self.__reduced_solution = reduced_sol

    def getReducedSolution(self):
        return self.__reduced_solution

    def process(self):
        patterns = self.getPatterns()
        reduced_sol = self.getReducedSolution()

        if patterns is None or reduced_sol is None:
            return None

        if isinstance(reduced_sol, SetExtensionSolution):
            semantics = list(reduced_sol.getAnswer())[0].getSemantics() if reduced_sol.getAnswer() else None
            merged_extensions = set()

            base_answers = reduced_sol.getAnswer()
            
            if not base_answers:
                base_answers = [Extension(set(), semantics=semantics)]

            for ext in base_answers:
                current_args = set(ext.getExtArgument())

                for pattern in patterns:
                    start_arg = pattern[0]
                    
                    if start_arg in current_args:
                        for i in range(0, len(pattern), 2):
                            current_args.add(pattern[i])
                        for i in range(1, len(pattern), 2):
                            current_args.discard(pattern[i])
                    else:
                        for i in range(1, len(pattern), 2):
                            current_args.add(pattern[i])
                        for i in range(0, len(pattern), 2):
                            current_args.discard(pattern[i])

                merged_extensions.add(Extension(current_args, semantics=semantics))
            
            return SetExtensionSolution(merged_extensions)

        return reduced_sol