from Src.CaseFile.Solutions.Solution import Solution


# Solution of the  type True or False
class BooleanSolution(Solution):
    def __init__(self, answer):
        # check the type of input
        if answer is not None and not isinstance(answer, bool):
            raise TypeError("need a bool")
        self.__answer = answer

    def getAnswer(self):
        return self.__answer

    def __eq__(self, Solution2) -> bool:
        if isinstance(Solution2, BooleanSolution):
            return self.getAnswer() == Solution2.getAnswer()
        return False

    def __str__(self) -> str:
        return str(self.getAnswer())
