from Src.CaseFile.Questions.Question import Question
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


# Question of the type: x in Stable Extension or x in Preferred Extension
class XinExtension(Question):
    # A xInExtension Question take one argument and a Semantics in input
    def __init__(self, argument: Argument, semantics: Semantics):
        # check the type entry
        if not isinstance(argument, Argument):
            raise TypeError("need a argument object")
        if not isinstance(semantics, Semantics):
            raise TypeError("need a Semantics object")
        self.__argument = argument
        self.__semantics = semantics

    def getAnswerType(self):
        return bool

    def getArgument(self):
        return self.__argument

    def getSemantics(self):
        return self.__semantics
    
    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        if not isinstance(other_question, XinExtension):
            return False
        if self.getSemantics() != other_question.getSemantics():
            return False
            
        current_target_index = self.getArgument().getIndex()
        mapped_index = mapping.get(current_target_index)

        return mapped_index == other_question.getArgument().getIndex()

    def __eq__(self, other) -> bool:
        if isinstance(other, XinExtension):
            return (
                self.getArgument() == other.getArgument()
                and self.getSemantics() == other.getSemantics()
            )
        return False

    def __hash__(self) -> hash:
        return hash((self.getArgument(), self.getSemantics()))
