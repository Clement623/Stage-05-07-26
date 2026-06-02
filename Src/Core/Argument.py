# The class to represent an Argument take an index to create
# The index is the "key" of the argument is unique
class Argument:
    def __init__(self, index):
        if not isinstance(index, int):
            raise TypeError("index need to be a integer")
        self.__index = index

    # Magic method to compare 2 arguments by the index arg1==arg2 if he has the same index
    def __eq__(self, arg) -> bool:
        if isinstance(arg, Argument):
            return self.getIndex() == arg.getIndex()
        return False

    # Returns the hash value of the object based on its index
    def __hash__(self) -> hash:
        return hash(self.getIndex())

    def __repr__(self):
        return f"{self.getIndex()}"

    def getIndex(self):
        return self.__index
