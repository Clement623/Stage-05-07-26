from .Question import Question
from Src.ExtFile.Semantics import Semantics
from Src.ExtFile.Extension import Extension



class ExtIsInSemantics(Question):
    def __init__(self, extension: Extension, semantics: Semantics):
        self.__extension = extension
        self.__answerType = bool
        self.__semantics = semantics


    def isEquivalentUnderMapping(self, other_question, mapping: dict) -> bool:
        if not isinstance(other_question, ExtIsInSemantics):
            return False
        if self.getSemantics() != other_question.getSemantics():
            return False

        current_target_index = self.getArgument().getIndex()
        mapped_index = mapping.get(current_target_index)

        return mapped_index == other_question.getArgument().getIndex()
    
        # get extension x
    def getExtension(self) -> Extension:
        return self.__extension

    # get the semantics
    def getSemantics(self) -> Semantics:
        return self.__semantics
    
    def getAnswerType(self):
        return self.__answerType
