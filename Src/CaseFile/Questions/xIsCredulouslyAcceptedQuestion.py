from .Question import Question
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics



class xIsCredulouslyAcceptedQuestion(Question):
    def __init__(self, argument, semantic):
        self.argument = argument
        self.semantic = semantic
        self.answerType = bool

    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        if not isinstance(other_question, xIsCredulouslyAcceptedQuestion):
            return False
        if self.getSemantics() != other_question.getSemantics():
            return False

        current_target_index = self.getArgument().getIndex()
        mapped_index = mapping.get(current_target_index)

        return mapped_index == other_question.getArgument().getIndex()
    
        # get argument x
    def getArgument(self) -> Argument:
        return self.__argument

    # get the semantics
    def getSemantics(self) -> Semantics:
        return self.__semantics
    
    def getAnswerType(self):
        return self.answerType
