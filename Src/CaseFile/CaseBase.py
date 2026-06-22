from Src.CaseFile.Case import Case


class CaseBase:
    # Initialize an empty list of cases
    def __init__(self):
        self.__cases = []

    # Get the list of all cases
    def getListCase(self) -> list:
        return self.__cases

    # Get an iterator for the list of cases
    def iterListCase(self) -> iter:
        return iter(self.getListCase())

    # Check if a case is already in the case base
    def isExactlyInBase(self, case: Case) -> bool:
        if not isinstance(case, Case):
            raise TypeError("case need to be a Case")
        return case in self.getListCase()

    # Add a case to the case base if it is not already there
    def addCase(self, case: Case) -> None:
        if not isinstance(case, Case):
            raise TypeError("case need to be a Case")
        if not self.isExactlyInBase(case):
            self.__cases.append(case)

    # Remove a case from the case base
    def removeCase(self, case: Case) -> None:
        if not isinstance(case, Case):
            raise TypeError("case need to be a Case")
        if not self.isExactlyInBase(case):
            raise ValueError(f"{case} not in Cases")
        self.__cases.remove(case)

    def get_candidates_by_hash_and_question(self, graph_hash: str, question_type: type) -> list:
        candidates = []
        for c in self.__cases:
            if c.getHashGraph() == graph_hash and type(c.getProblem().getQuestion()) is question_type:
                candidates.append(c)
        return candidates

    def __repr__(self):
        nb_cases = len(self.__cases)
        cases_repr = ", ".join(repr(c) for c in self.__cases)
        return f"CaseBase(Total Cases: {nb_cases}, Cases: [{cases_repr}])"
