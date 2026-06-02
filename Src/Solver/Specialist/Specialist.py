from abc import ABC, abstractmethod
from Src.CaseFile.Problem import Problem

class Specialist(ABC):
    def __init__(self):
        self.__problem=None

    @abstractmethod
    def process(self):
        pass
    
    def getProblem(self):
        if self.__problem is None:
            raise ValueError("problem not be defined")
        return self.__problem
    
    def setProblem(self, problem:Problem):
        if not isinstance(problem,Problem):
            raise TypeError("need a Problem Object")
        self.__problem=problem