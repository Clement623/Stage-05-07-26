from .Specialist import Specialist
import networkx as nx
from Src.CaseFile.GraphConverter import GraphConverter
from Src.Core.Attack import Attack
from Src.Core.Argument import Argument


class SCCDecompositionSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    def process(self):
        converter = GraphConverter()
        af = self.getProblem().getSituation().getAF()
        G = converter.afToNetworkX(af)
        scc = list(nx.strongly_connected_components(G))
        C = nx.condensation(G, scc)
        topological_order = list(nx.topological_sort(C))
        scc_frameworks = []
        for comp_node in topological_order:
            members = C.nodes[comp_node]["members"]
            subgraph = G.subgraph(members)
            new_af = converter.networkXToAf(subgraph)
            incoming_attack = [Attack(Argument(u), Argument(v)) for u, v in G.in_edges(members) if u not in members]
            scc_frameworks.append((new_af, incoming_attack))
        return scc_frameworks
