from .Specialist import Specialist
import networkx as nx
from Src.CaseFile.GraphConverter import GraphConverter
from Src.Core.Attack import Attack
from Src.Core.Argument import Argument


class SCCDecompositionSpecialist(Specialist):
    """
    Specialist that decomposes the argumentation framework into its
    strongly connected components (SCCs), ordered topologically,
    to allow solving them one after another.
    """

    def __init__(self):
        super().__init__()

    def process(self):
        """Split the AF into SCCs and return them in topological order."""
        converter = GraphConverter()
        af = self.getProblem().getSituation().getAF()

        # Convert the AF into a networkx graph
        G = converter.afToNetworkX(af)

        # Find strongly connected components
        scc = list(nx.strongly_connected_components(G))

        # Condense the graph: each SCC becomes a single node
        C = nx.condensation(G, scc)

        # Order the SCCs so dependencies come before dependents
        topological_order = list(nx.topological_sort(C))

        scc_frameworks = []
        for comp_node in topological_order:
            # Arguments belonging to this SCC
            members = C.nodes[comp_node]["members"]

            # Sub-graph containing only this SCC
            subgraph = G.subgraph(members)
            new_af = converter.networkXToAf(subgraph)

            # Attacks coming from outside this SCC into it
            incoming_attack = [Attack(Argument(u), Argument(v)) for u, v in G.in_edges(members) if u not in members]

            scc_frameworks.append((new_af, incoming_attack))

        return scc_frameworks