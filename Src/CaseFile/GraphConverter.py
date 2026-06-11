from Src.Core.ArgFramework import ArgFramework
import networkx as nx


class GraphConverter:
    # Convert an argumentation framework into a networkx graph
    @staticmethod
    def afToNetworkX(Af: ArgFramework) -> nx.DiGraph:
        if not isinstance(Af, ArgFramework):
            raise TypeError("need a ArgFramework object")
        G = nx.DiGraph()
        # Add arguments as nodes in the graph
        for arg in Af.iterArgument():
            G.add_node(arg.getIndex())
        # Add attacks as directed edges in the graph
        for att in Af.getAttacks():
            G.add_edge(att.getFromArg().getIndex(), att.getToArg().getIndex())
        return G

    # Compute a unique hash value for the graph structure
    @staticmethod
    def computeWeisfeilerLehmanHash(af: ArgFramework) -> str:
        G = GraphConverter.afToNetworkX(af)
        return nx.weisfeiler_lehman_graph_hash(G)
