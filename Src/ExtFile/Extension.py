from Src.Core.Argument import Argument


class Extension:
    def __init__(self, arguments: set):
        if not isinstance(arguments, set):
            raise TypeError("arguments need to be a set")
        if not all(isinstance(a, Argument) for a in arguments):
            raise TypeError("all elements need to be Arguments")
        self.__arguments = arguments

    def getExtArgument(self):
        return self.__arguments

    def iterExtArgument(self):
        return iter(self.getExtArgument())

    def isInExtension(self, arg: Argument):
        if not isinstance(arg, Argument):
            raise TypeError("need a argument in input")
        return arg in self.getExtArgument()
