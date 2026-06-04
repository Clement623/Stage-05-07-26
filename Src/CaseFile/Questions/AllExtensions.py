from Src.CaseFile.Questions.Question import Question
from Src.ExtFile.Semantics import Semantics

#Question of the type: All extensions for x semantics
class AllExtensions(Question):
    #Initialize the question with a semantics
    def __init__(self, semantics: Semantics):
        if not isinstance(semantics, Semantics):
            raise TypeError("need a Semantics object")
        self.__semantics = semantics

    #get the type of the answer
    def getAnswerType(self):
        return list
    #get the semantics
    def getSemantics(self) -> Semantics:
        return self.__semantics
    
    def isEquivalentUnderMapping(self, other_question) -> bool:
        return isinstance(other_question, AllExtensions)
    #check the egality in 2 AllExtensions Object
    def __eq__(self, other) -> bool:
        if isinstance(other, AllExtensions):
            return self.getSemantics() == other.getSemantics()
        return False

    def __hash__(self) -> int:
        return hash(self.getSemantics())
