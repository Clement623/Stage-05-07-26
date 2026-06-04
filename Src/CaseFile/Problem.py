from Src.CaseFile.Situation import Situation 
from Src.CaseFile.Questions.Question import Question 

class Problem:     
    # Initialize the problem with a situation and a question
    def __init__(self, situation: Situation, question: Question):         
        if not isinstance(situation, Situation):             
            raise TypeError("situation need to be a Situation")         
        if not isinstance(question, Question):             
            raise TypeError("question need to be a Question")         
        self.__situation = situation         
        self.__question = question     

    # Check if two problems are equal
    def __eq__(self, probleme2) -> bool:         
        if isinstance(probleme2, Problem):             
            return (                 
                self.getSituation() == probleme2.getSituation()                 
                and self.getQuestion() == probleme2.getQuestion()             
            )         
        return False     

    # Get the situation
    def getSituation(self) -> Situation:         
        return self.__situation     

    # Get the question
    def getQuestion(self) -> Question:         
        return self.__question