from Src.Solver.ProblemSpecialist.TransformationSpecialist.TransformationSpecialist import (
    TransformationSpecialist,
)
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument


class ArgumentTransformationSpecialist(TransformationSpecialist):
    def __init__(self):
        super().__init__()

    def applyTransformation(self, Af: ArgFramework):

        newIndex = Af.getNextAvailableIndex()
        Af.addArgument(Argument(newIndex))
 