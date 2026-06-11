from .Question import Question


class ExtIsInSemantics(Question):
    def __init__(self, extension):
        self.extension = extension
        self.answerType = bool

    def getAnswerType(self):
        return self.answerType
