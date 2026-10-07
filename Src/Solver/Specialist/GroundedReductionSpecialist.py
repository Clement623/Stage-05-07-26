from .Specialist import Specialist
from Src.ExtFile.Extension import Extension
import copy


class GroundedReductionSpecialist(Specialist):
    def __init__(self):
        super().__init__()
        self.__groundedExtension = None

    def setGroundedExtension(self, ext: Extension):
        if not isinstance(ext, Extension):
            raise TypeError("need a Extension Object")
        self.__groundedExtension = ext

    def getGroundedExtension(self) -> Extension:
        return self.__groundedExtension

    def process(self):
        problem = self.getProblem()
        af = problem.getSituation().getAF()

        # Accepted arguments are those in the grounded extension
        accepted_arg = self.getGroundedExtension().getExtArguments()

        # Rejected arguments are those attacked by an accepted argument
        rejected_args = set()
        for arg in self.getGroundedExtension().iterExtArguments():
            targets = af.getTarget().get(arg, set())
            rejected_args.update(targets)

        # Both accepted and rejected arguments can be removed from the reduced problem
        args_to_remove = accepted_arg.union(rejected_args)

        # Deep copy to avoid modifying the original problem
        new_problem = copy.deepcopy(problem)
        new_af = new_problem.getSituation().getAF()

        # Remove all settled arguments from the new AF
        for arg in args_to_remove:
            if new_af.isInArguments(arg):
                new_af.removeArgument(arg)

        return new_problem