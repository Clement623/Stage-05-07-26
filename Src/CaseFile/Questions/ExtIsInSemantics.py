from .Question import Question
from Src.ExtFile.Semantics import Semantics
from Src.ExtFile.Extension import Extension


class ExtIsInSemantics(Question):

    def __init__(self, extension: Extension, semantics: Semantics):
        """Init the question with an extension and a semantics."""
        self.__extension = extension
        self.__answerType = bool
        self.__semantics = semantics

    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        """Check if two questions are equivalent under a given mapping."""
        if not isinstance(other_question, ExtIsInSemantics):
            return False
        if self.getSemantics() != other_question.getSemantics():
            return False

        for arg in self.getExtension().getExtArgument():
            if arg not in other_question.getExtension():
                return False

        return True

    def getExtension(self) -> Extension:
        """Return the extension x."""
        return self.__extension

    def getSemantics(self) -> Semantics:
        """Return the semantics."""
        return self.__semantics

    def getAnswerType(self):
        """Return the type of the answer."""
        return self.__answerType