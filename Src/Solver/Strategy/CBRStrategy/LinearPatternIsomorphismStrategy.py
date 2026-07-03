from Src.CaseFile.Solutions.UnresolvedProbem import UnresolvedProblem
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.CaseFile.Solutions.SingleExtensionSolution import SingleExtensionSolution
from Src.Solver.Specialist.BijectionSpecialist import BijectionSpecialist
from Src.Solver.Specialist.IsomorphismSpecialist import IsomorphismSpecialist
from Src.Solver.Specialist.LinearPatternSpecialist import LinearPatternSpecialist
from Src.Solver.Specialist.PolarityDecompressionSpecialist import (
    PolarityDecompressionSpecialist,
)
from Src.Solver.Strategy.CBRStrategy.CBRStrategy import CBRStrategy


class LinearPatternIsomorphismStrategy(CBRStrategy):
    def __init__(self):
        super().__init__()

    def solve(self, problem, caseBase):
        # Make sure a case base was provided
        if caseBase is None:
            raise (TypeError("need a caseBase"))
        else:
            self.setCaseBase(caseBase)

        # Compress the problem by detecting linear patterns
        pattern_specialist = LinearPatternSpecialist()
        pattern_specialist.setProblem(problem)
        compressed_problem = pattern_specialist.process()

        # If compression removed all arguments, nothing to solve
        if len(compressed_problem.getSituation().getAF().getArguments()) == 0:
            return None

        # Look for a structurally isomorphic case in the case base
        iso_specialist = IsomorphismSpecialist()
        iso_specialist.setCaseBase(caseBase)
        iso_specialist.setProblem(compressed_problem)
        isomorphisms = iso_specialist.process()

        # No matching case found, return the compressed problem as unresolved
        if not isomorphisms:
            return UnresolvedProblem(compressed_problem)

        matching_case, all_mapping = isomorphisms

        all_merged_extensions = set()
        is_boolean_problem = False
        final_boolean_answer = None
        had_single_extension = False

        # Try each mapping and translate the matching case's solution back
        for matcher in all_mapping:
            old_solution = matching_case.getSolution()

            if isinstance(old_solution, BooleanSolution):
                # Boolean answers transfer directly, no translation needed
                is_boolean_problem = True
                final_boolean_answer = old_solution.getAnswer()
                break
            else:
                # Translate the case solution back using the inverse mapping
                bij_specialist = BijectionSpecialist(matcher, inverse=True)
                bij_specialist.setElement(old_solution.getAnswer())
                translated_answer = bij_specialist.process()

                if isinstance(
                    old_solution, (SetExtensionSolution, SingleExtensionSolution)
                ):
                    if isinstance(old_solution, SingleExtensionSolution):
                        had_single_extension = True
                        translated_extensions = {translated_answer}
                    else:
                        translated_extensions = translated_answer

                    reduced_solution = SetExtensionSolution(translated_extensions)

                    # Expand the compressed solution back to the original argument space
                    decompression_specialist = PolarityDecompressionSpecialist()
                    decompression_specialist.setPatterns(
                        pattern_specialist.getPatterns()
                    )
                    decompression_specialist.setReducedSolution(reduced_solution)
                    decompressed_sol = decompression_specialist.process()

                    # Collect all decompressed extensions
                    if decompressed_sol is not None:
                        all_merged_extensions.update(decompressed_sol.getAnswer())
                else:
                    raise TypeError("Unsupported solution type from matching case")

        # Return a boolean answer if that's what the problem asked for
        if is_boolean_problem:
            return BooleanSolution(final_boolean_answer)

        if all_merged_extensions:
            # If there was originally a single extension and it stayed unique, keep that type
            if had_single_extension and len(all_merged_extensions) == 1:
                unique_extension = list(all_merged_extensions)[0]
                return SingleExtensionSolution(unique_extension)

            return SetExtensionSolution(all_merged_extensions)

        return None
