from Src.Core.ArgFramework import ArgFramework


class Situation:
    # Initialize a Situation Object with a ArgFramework
    def __init__(self, framework: ArgFramework):
        if not isinstance(framework, ArgFramework):
            raise TypeError("framework need to be a Argument Framework")
        self.__af = framework

    # get the ArgFramework
    def getAF(self) -> ArgFramework:
        return self.__af

    # check the egality of two Situation Object
    def __eq__(self, other) -> bool:
        if isinstance(other, Situation):
            return self.getAF() == other.getAF()
        return False
