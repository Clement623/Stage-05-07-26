from Src.CaseFile.Solutions.Solution import Solution

class ListExtensionSolution(Solution):
    def __init__(self, answer: list):
        if not isinstance(answer, list):
            raise TypeError("need a list of extensions")
        self.__answer = answer

    def getAnswer(self) -> list:
        return self.__answer

    def __eq__(self, other) -> bool:
        if isinstance(other, ListExtensionSolution):
            return self.getAnswer() == other.getAnswer()
        return False

    def __hash__(self) -> int:
        return hash(tuple(self.getAnswer()))