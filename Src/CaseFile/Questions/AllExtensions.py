from Src.CaseFile.Questions.Question import Question
from Src.ExtFile.Semantics import Semantics


# Question of the type: All extensions for x semantics
class AllExtensions(Question):

    def __init__(self, semantics: Semantics):
        """Init the question with a semantics."""
        if not isinstance(semantics, Semantics):
            raise TypeError("need a Semantics object")
        self.__semantics = semantics

    def getAnswerType(self):
        """Return the type of the answer (a list)."""
        return list

    def getSemantics(self) -> Semantics:
        """Return the semantics of this question."""
        return self.__semantics

    def isEquivalentUnderMapping(self, other_question, mapping=None) -> bool:
        """Check if two questions are equivalent (same semantics)."""
        if not isinstance(other_question, AllExtensions):
            return False
        return self.getSemantics() == other_question.getSemantics()

    def __eq__(self, other) -> bool:
        """Check equality between two AllExtensions objects."""
        if isinstance(other, AllExtensions):
            return self.getSemantics() == other.getSemantics()
        return False

    def __hash__(self) -> int:
        """Hash based on semantics."""
        return hash(self.getSemantics())