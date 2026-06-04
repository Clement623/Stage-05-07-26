from Src.Solver.SolutionSpecialist.AdaptSolutionSpecialist.AdaptSolutionSpecialist import AdaptSolutionSpecialist
from Src.CaseFile.Solutions.ListExtensionSolution import ListExtensionSolution
from Src.ExtFile.Extension import Extension

class AdaptReductionSolution(AdaptSolutionSpecialist):
    # Initialize the reduction specialist
    def __init__(self):
        super().__init__()
        self.__target_arguments = set()

    # Set the arguments that we want to keep
    def setTargetArguments(self, arguments: set) -> None:
        self.__target_arguments = arguments

    # Get the target arguments
    def getTargetArguments(self) -> set:
        return self.__target_arguments

    # Adapt the solution by removing extra arguments
    def adapt(self):
        solution = self.getSolution()
        allowed_arguments = self.getTargetArguments()

        # If the solution is a list of extensions
        if isinstance(solution, ListExtensionSolution):
            adapted_extensions = []
            
            for extension in solution.getAnswer():
                new_args = set()
                # Only keep arguments that are in the target problem
                for arg in extension.iterExtArgument():
                    if arg in allowed_arguments:
                        new_args.add(arg)
                
                # Add the cleaned extension to our new list
                adapted_extensions.append(Extension(new_args))
                
            return ListExtensionSolution(adapted_extensions)
            
        # Return the original solution if it is not a ListExtensionSolution
        return solution