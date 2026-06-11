from Src.Core.ArgFramework import ArgFramework


class Situation:
    # Initialize a Situation Object with a ArgFramework
    def __init__(self, framework: ArgFramework):
        if not isinstance(framework, ArgFramework):
            raise TypeError("framework need to be a Argument Framework")
        self.__AF = framework

    # get the ArgFramework
    def getAF(self) -> ArgFramework:
        return self.__AF

    # check the egality of two Situation Object
    def __eq__(self, framework2) -> bool:
        if isinstance(framework2, Situation):
            return self.getAF() == framework2.getAF()
        return False
