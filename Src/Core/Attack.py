from Src.Core.Argument import Argument


class Attack:
    # Initialize an attack with a source argument and a target argument
    def __init__(self, fromArg: Argument, toArg: Argument):
        if not isinstance(fromArg, Argument):
            raise TypeError("fromArg need to be an Argument")
        if not isinstance(toArg, Argument):
            raise TypeError("toArg need to be an Argument")
        self.__fromArg = fromArg
        self.__toArg = toArg

    # Represent the attack as a string like source->target
    def __repr__(self) -> str:
        return f"{self.getFromArg().getIndex()}->{self.getToArg().getIndex()}"

    # Check if two attacks have the same source and target
    def __eq__(self, att) -> bool:
        if isinstance(att, Attack):
            return (self.getFromArg() == att.getFromArg()) and (
                self.getToArg() == att.getToArg()
            )
        return False

    # Get the hash value of the attack
    def __hash__(self) -> hash:
        return hash((self.getFromArg(), self.getToArg()))

    # Get the source argument of the attack
    def getFromArg(self) -> Argument:
        return self.__fromArg

    # Get the target argument of the attack
    def getToArg(self) -> Argument:
        return self.__toArg
