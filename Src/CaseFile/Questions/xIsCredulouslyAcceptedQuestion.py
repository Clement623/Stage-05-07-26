from .Question import Question


class xIsCredulouslyAcceptedQuestion(Question):
    def __init__(self, argument, semantic):
        self.argument = argument
        self.semantic = semantic
        self.answerType = bool

    def getAnswerType(self):
        return self.answerType
