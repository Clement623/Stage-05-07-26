from .Specialist import Specialist
from Src.CaseFile.GraphConverter import GraphConverter
import networkx as nx


class WCCDecompositionSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    def process(self):
        converter = GraphConverter()
        af = self.getProblem().getSituation().getAF()
        G = converter.afToNetworkX(af)
        listWCCGraph = [G.subgraph(wcc) for wcc in nx.weakly_connected_components(G)]
        return [converter.networkXToAf(wccGraph) for wccGraph in listWCCGraph]
