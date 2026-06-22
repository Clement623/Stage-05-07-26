from Src.CaseFile.Solutions.Solution import Solution


# Solution of the type List of Extensions
class SetExtensionSolution(Solution):
    # Initialize the object with a answer
    def __init__(self, answer: set):
        if not isinstance(answer, set):
            raise TypeError("need a set of extensions")
        self.__answer = answer

    # get the answer
    def getAnswer(self) -> set:
        return self.__answer

    # check the egality in two ListExtensionSolution object
    def __eq__(self, other) -> bool:
        if isinstance(other, SetExtensionSolution):
            return self.getAnswer() == other.getAnswer()
        return False

    def __hash__(self) -> int:
        return hash(frozenset(self.getAnswer()))

    def __repr__(self) -> str:
        extensions_str = [str(ext.getExtArgument()) for ext in self.getAnswer()]
        return f"SetExtensionSolution([{', '.join(extensions_str)}])"