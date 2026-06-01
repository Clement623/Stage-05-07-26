from Src.CaseFile.Case import Case


# Class to represent the Case Base
class CaseBase:
    def __init__(self):
        self.__cases = []

    def getListCase(self):
        return self.__cases

    # Check if a Case is in the Case Base
    def isExactlyInBase(self, case: Case):
        if not isinstance(case, Case):
            raise TypeError("case need to be a Case")
        return case in self.getListCase()

    # Add a Case of the Case Base
    def addCase(self, case: Case):
        if not isinstance(case, Case):
            raise TypeError("case need to be a Case")
        if not self.isExactlyInBase(case):
            self.__cases.append(case)

    # Remove a Case of the Case Base
    def removeCase(self, case: Case):
        if not isinstance(case, Case):
            raise TypeError("case need to be a Case")
        if not self.isExactlyInBase(case):
            raise ValueError(f"{case} not in Cases")
        self.__cases.remove(case)

    def afficherBase(self):
        for case in self.iterCases():
            print(case)
