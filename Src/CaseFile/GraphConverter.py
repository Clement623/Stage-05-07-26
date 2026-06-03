from Src.Core.ArgFramework import ArgFramework
import networkx as nx


class GraphConverter:
    # Convert a argument framework in a graph of networkx take in  input a ArgFramework object and output a nxDiGraph
    @staticmethod
    def afToNetworkX(Af: ArgFramework) -> nx.DiGraph:
        # Check the type entry
        if not isinstance(Af, ArgFramework):
            raise TypeError("need a ArgFramework object")

        G = nx.DiGraph()
        # Argument=node
        for arg in Af.iterArgument():
            G.add_node(arg.getIndex())

        for att in Af.getAttacks():
            G.add_edge(att.getFromArg().getIndex(), att.getToArg().getIndex())
            
        return G

    @staticmethod
    def computeWeisfeilerLehmanHash(af: ArgFramework) -> str:
        G = GraphConverter.afToNetworkX(af)
        return nx.weisfeiler_lehman_graph_hash(G)
