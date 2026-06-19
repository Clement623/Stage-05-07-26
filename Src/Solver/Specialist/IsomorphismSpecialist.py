from networkx.algorithms.isomorphism import DiGraphMatcher
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.GraphConverter import GraphConverter
from Src.Solver.Specialist.Specialist import Specialist


# Search if the problem have a isomorph in the case base
class IsomorphismSpecialist(Specialist):
    def __init__(self):
        super().__init__()
        self.__base = None

    def getCaseBase(self) -> CaseBase:
        return self.__base
    
    def setCaseBase(self, base: CaseBase):
        if not isinstance(base, CaseBase):
            raise TypeError("need a CaseBase")
        self.__base = base
    # Method to find if a graph of a problem have a isomorph in the CaseBase
    def process(self) -> tuple:
        # convert the Af of the problem in the networkx graph
        Af = self.getProblem().getSituation().getAF()
        HashGraph = GraphConverter.computeWeisfeilerLehmanHash(Af)
        
        for c in self.getCaseBase().iterListCase():
            if HashGraph == c.getHashGraph():
                situation = c.getProblem().getSituation()
                G1 = GraphConverter.afToNetworkX(Af)
                G2 = GraphConverter.afToNetworkX(situation.getAF())
                matcher = DiGraphMatcher(G1, G2)

                if matcher.is_isomorphic() and type(c.getProblem().getQuestion()) is type(self.getProblem().getQuestion()):
                    all_mappings = list(matcher.isomorphisms_iter())
                    return c, all_mappings
                    
        return None

