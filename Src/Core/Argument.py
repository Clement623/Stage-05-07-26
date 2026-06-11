class Argument:
    # Initialize an argument with a unique integer index
    def __init__(self, index):
        if not isinstance(index, int):
            raise TypeError("index need to be a integer")
        self.__index = index

    # Compare two arguments using their indices
    def __eq__(self, arg) -> bool:
        if isinstance(arg, Argument):
            return self.getIndex() == arg.getIndex()
        return False

    # Get the hash value of the argument based on its index
    def __hash__(self) -> hash:
        return hash(self.getIndex())

    # Represent the argument as a string using its index
    def __repr__(self) -> str:
        return f"{self.getIndex()}"

    # Get the index of the argument
    def getIndex(self) -> int:
        return self.__index
