from .TransformationSpecialist import TransformationSpecialist
from Src.Core.ArgFramework import ArgFramework


class RemoveArgumentTransformationSpecialist(TransformationSpecialist):
    def __init__(self):
        super().__init__()

    def applyTransformation(self, Af: ArgFramework):
        pass
