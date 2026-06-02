from Src.CaseFile.Situation import Situation
from Src.CaseFile.Questions.Question import Question


class Problem:
    def __init__(self, situation: Situation, question: Question):
        if not isinstance(situation, Situation):
            raise TypeError("situation need to be a Situation")
        if not isinstance(question, Question):
            raise TypeError("question need to be a Question")
        self.__situation = situation
        self.__question = question

    def __eq__(self, probleme2) -> bool:
        if isinstance(probleme2, Problem):
            return (
                self.getSituation() == probleme2.getSituation()
                and self.getQuestion() == probleme2.getQuestion()
            )
        return False

    def getSituation(self):
        return self.__situation

    def getQuestion(self):
        return self.__question
