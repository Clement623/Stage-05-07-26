from Src.Core.Argument import Argument


# The class to represent an Attack take 2 index to create 2 argument
# from=Attacker and to=Attacked
class Attack:
    def __init__(self, fromArg: Argument, toArg: Argument):
        if not isinstance(fromArg, Argument):
            raise TypeError("fromArg need to be an Argument")
        if not isinstance(toArg, Argument):
            raise TypeError("toArg need to be an Argument")
        self.__fromArg = fromArg
        self.__toArg = toArg

    def __repr__(self) -> str:
        return f"{self.getFromArg().getIndex()}->{self.getToArg().getIndex()}"

    def __eq__(self, att) -> bool:
        if isinstance(att, Attack):
            return (self.getFromArg() == att.getFromArg()) and (
                self.getToArg() == att.getToArg()
            )
        return False

    def __hash__(self) -> hash:
        return hash((self.getFromArg(), self.getToArg()))

    def getFromArg(self):
        return self.__fromArg

    def getToArg(self):
        return self.__toArg
