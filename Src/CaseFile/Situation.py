from Src.Core.ArgFramework import ArgFramework


class Situation:
    def __init__(self, framework: ArgFramework):
        if not isinstance(framework, ArgFramework):
            raise TypeError("framework need to be a Argument Framework")
        self.__AF = framework

    def getAF(self):
        return self.__AF

    def __eq__(self, framework2) -> bool:
        if isinstance(framework2, Situation):
            return self.getAF() == framework2.getAF()
        return False
