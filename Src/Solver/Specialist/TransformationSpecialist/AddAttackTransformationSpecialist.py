from .TransformationSpecialist import TransformationSpecialist
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Attack import Attack
from Src.Core.Argument import Argument


class AddAttackTransformationSpecialist(TransformationSpecialist):
    def __init__(self):
        super().__init__()
        self.__fromIndex = None
        self.__toIndex = None

    def setAttack(self, fromIndex: int, toIndex: int) -> None:
        self.__fromIndex = fromIndex
        self.__toIndex = toIndex

    def applyTransformation(self, Af: ArgFramework) -> None:
        if self.__fromIndex is None or self.__toIndex is None:
            raise ValueError("Attack not defined, call setAttack() first")
        fromArg = Argument(self.__fromIndex)
        toArg = Argument(self.__toIndex)
        Af.addAttack(Attack(fromArg, toArg))
