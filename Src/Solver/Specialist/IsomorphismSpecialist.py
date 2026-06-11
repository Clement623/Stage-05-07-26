from networkx.algorithms.isomorphism import DiGraphMatcher
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.GraphConverter import GraphConverter
from Src.Solver.Specialist.Specialist import Specialist

#Search if the problem have a isomorph in the case base
class IsomorphismSpecialist(Specialist):
    def __init__(self, base: CaseBase):
        super().__init__()
        self.__base = base

    def getBase(self) -> CaseBase:
        return self.__base

    # Method to find if a graph of a problem have a isomorph in the CaseBase
    def process(self) -> tuple:
        # convert the Af of the problem in the networkx graph
        Af = self.getProblem().getSituation().getAF()
        HashGraph = GraphConverter.computeWeisfeilerLehmanHash(Af)
        # Iterate sequentially through the stored cases starting from index i
        for c in self.getBase().iterListCase():
            if HashGraph == c.getHashGraph():
                situation = c.getProblem().getSituation()
                G1 = GraphConverter.afToNetworkX(Af)
                G2 = GraphConverter.afToNetworkX(situation.getAF())
                matcher = DiGraphMatcher(G1, G2)
                return c, matcher
        return None

