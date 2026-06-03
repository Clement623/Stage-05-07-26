from Src.CaseFile.Questions.Question import Question
from Src.ExtFile.Semantics import Semantics

class AllExtensions(Question):
    def __init__(self, semantics: Semantics):
        if not isinstance(semantics, Semantics):
            raise TypeError("need a Semantics object")
        self.__semantics = semantics

    def getAnswerType(self):
        return list

    def getSemantics(self) -> Semantics:
        return self.__semantics

    def isEquivalentUnderMapping(self, other_question) -> bool:
        if not isinstance(other_question, AllExtensions):
            return False

        if self.getSemantics() != other_question.getSemantics():
            return False
        return True

    def __eq__(self, other) -> bool:
        if isinstance(other, AllExtensions):
            return self.getSemantics() == other.getSemantics()
        return False

    def __hash__(self) -> int:
        return hash(self.getSemantics())