from .Specialist import Specialist
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
import itertools
from Src.ExtFile.Extension import Extension


class WCCRecompositionSpecialist(Specialist):
    def __init__(self):
        super().__init__()
        self.__solutions=None

    def setSolutions(self, solutions):
        self.__solutions = solutions

    def getSolutions(self):
        return self.__solutions
    
    def iterSolutions(self):
        return iter(self.getSolutions())

    def process(self):
        solutions=self.getSolutions()
        iterSol=self.iterSolutions()
        if not solutions:
            return None
        
        if isinstance(solutions[0], BooleanSolution):
            return BooleanSolution(all(sol.getAnswer() for sol in iterSol))

        if isinstance(solutions[0], SetExtensionSolution):
            components_extensions = [list(sol.getAnswer()) for sol in iterSol]
            merged_extensions = set()
            
            for combo in itertools.product(*components_extensions):
                combined_args = set()
                semantics = combo[0].getSemantics() if combo else None
                for ext in combo:
                    combined_args.update(ext.getExtArgument())
                merged_extensions.add(Extension(combined_args, semantics=semantics))
            return SetExtensionSolution(merged_extensions)
            
        return solutions[0]