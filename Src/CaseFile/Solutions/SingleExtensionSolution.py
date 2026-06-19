
from Src.CaseFile.Solutions.Solution import Solution
from Src.ExtFile.Extension import Extension


# Solution of the type Single Extension
class SingleExtensionSolution(Solution):
    # Initialize the object with an extension
    def __init__(self, answer: Extension):
        if not isinstance(answer, Extension):
            raise TypeError("need an Extension object")
        self.__answer = answer

    # get the answer
    def getAnswer(self) -> Extension:
        return self.__answer

    # check the equality in two SingleExtensionSolution objects
    def __eq__(self, other) -> bool:
        if isinstance(other, SingleExtensionSolution):
            return self.getAnswer() == other.getAnswer()
        return False

    def __hash__(self) -> int:
        return hash(self.getAnswer())

    def __str__(self) -> str:
        return str(self.getAnswer())
