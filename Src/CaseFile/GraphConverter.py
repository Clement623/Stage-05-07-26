from Src.Core.ArgFramework import ArgFramework
import networkx as nx


class GraphConverter:
    # Convert a argument framework in a graph of networkx take in  input a ArgFramework object and output a nxDiGraph
    def afToNetworkX(self, Af: ArgFramework):
        # Check the type entry
        if not isinstance(Af, ArgFramework):
            raise TypeError("need a ArgFramework object")

        G = nx.DiGraph()
        # Argument=node
        for arg in Af.iterArgument():
            G.add_node(arg.getIndex())
        # Attack=edge
        for att in Af.iterAttack():
            G.add_edge(att.getFromArg().getIndex(), att.getToArg().getIndex())
        return G
