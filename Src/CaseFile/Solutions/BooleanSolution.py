from Src.CaseFile.Solutions.Solution import Solution


# Solution of the  type True or False
class BooleanSolution(Solution):
    # Initialize the object with a answer
    def __init__(self, answer):
        # check the type of input
        if answer is not None and not isinstance(answer, bool):
            raise TypeError("need a bool")
        self.__answer = answer

    # get the answer
    def getAnswer(self) -> bool:
        return self.__answer

    # check the egality with two BooleanSolution
    def __eq__(self, other) -> bool:
        if isinstance(other, BooleanSolution):
            return self.getAnswer() == other.getAnswer()
        return False

    def __str__(self) -> str:
        return str(self.getAnswer())
