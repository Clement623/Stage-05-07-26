from Src.Core.Argument import Argument


class Extension:
    #Initialize a extension with a set of arguments
    def __init__(self, arguments: set):
        if not isinstance(arguments, set):
            raise TypeError("arguments need to be a set")
        if not all(isinstance(a, Argument) for a in arguments):
            raise TypeError("all elements need to be Arguments")
        self.__arguments = arguments
    #get the set of arguments
    def getExtArgument(self) -> set[Argument]:
        return self.__arguments
    #get a iter object of the set of arguments
    def iterExtArgument(self) -> iter:
        return iter(self.getExtArgument())
    #test if a argument is in a extension
    def isInExtension(self, arg: Argument) -> bool:
        if not isinstance(arg, Argument):
            raise TypeError("need a argument in input")
        return arg in self.getExtArgument()

    def __eq__(self, other):
        if isinstance(other, Extension):
            return self.getExtArgument() == other.getExtArgument()
        return False

    def __hash__(self):
        return hash(tuple(sorted(arg.getIndex() for arg in self.getExtArgument())))