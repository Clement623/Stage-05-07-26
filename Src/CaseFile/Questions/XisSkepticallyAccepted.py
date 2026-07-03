from .Question import Question
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class XisSkepticallyAccepted(Question):

    def __init__(self, argument, semantic):
        """Init the question with an argument and a semantics."""
        self.__argument = argument
        self.__semantic = semantic
        self.answerType = bool

    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        """Check if two questions are equivalent under a given mapping."""
        if not isinstance(other_question, XisSkepticallyAccepted):
            return False
        if self.getSemantics() != other_question.getSemantics():
            return False

        current_target_index = self.getArgument().getIndex()
        mapped_index = mapping.get(current_target_index)

        return mapped_index == other_question.getArgument().getIndex()

    def getArgument(self) -> Argument:
        """Return argument x.
        """
        return self.__argument

    def getSemantics(self) -> Semantics:
        """Return the semantics.
        """
        return self.__semantics

    def getAnswerType(self):
        """Return the type of the answer."""
        return self.answerType