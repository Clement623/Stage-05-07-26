from Src.CaseFile.Solutions.Solution import Solution


# Solution of the type List of Extensions
class ListExtensionSolution(Solution):
    # Initialize the object with a answer
    def __init__(self, answer: list):
        if not isinstance(answer, list):
            raise TypeError("need a list of extensions")
        self.__answer = answer

    # get the answer
    def getAnswer(self) -> list:
        return self.__answer

    # check the egality in two ListExtensionSolution object
    def __eq__(self, other) -> bool:
        if isinstance(other, ListExtensionSolution):
            return self.getAnswer() == other.getAnswer()
        return False

    def __hash__(self) -> int:
        return hash(tuple(self.getAnswer()))
