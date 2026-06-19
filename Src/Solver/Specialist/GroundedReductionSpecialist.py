from .Specialist import Specialist
from Src.ExtFile.Extension import Extension
import copy


class GroundedReductionSpecialist(Specialist):
    def __init__(self):
        super().__init__()
        self.__grounded_ext = None

    def setGroundedExtension(self, ext: Extension):
        if not isinstance(ext, Extension):
            raise TypeError("need a Extension Object")
        self.__grounded_ext = ext

    def getGroundedExtension(self) -> Extension:
        return self.__grounded_ext

    def process(self):

        problem = self.getProblem()
        af = problem.getSituation().getAF()
        accepted_arg = self.getGroundedExtension().getExtArgument()
        rejected_args = set()
        for arg in self.getGroundedExtension().iterExtArgument():
            targets = af.getTarget().get(arg, set())
            rejected_args.update(targets)

        args_to_remove = accepted_arg.union(rejected_args)
        new_problem = copy.deepcopy(problem)
        new_af = new_problem.getSituation().getAF()
        for arg in args_to_remove:
            if new_af.isInArguments(arg):
                new_af.removeArgument(arg)

        return new_problem
