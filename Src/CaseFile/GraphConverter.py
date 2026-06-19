from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
from Src.Core.Attack import Attack
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

    # Convert a networkx DiGraph back into an argumentation framework
    @staticmethod
    def networkXToAf(G: nx.DiGraph) -> ArgFramework:
        if not isinstance(G, nx.DiGraph):
            raise TypeError("need a nx.DiGraph object")

        af = ArgFramework()

        # Add arguments (nodes)
        for node in G.nodes():
            af.addArgument(Argument(node))

        # Add attacks (edges)
        for u, v in G.edges():
            af.addAttack(Attack(Argument(u), Argument(v)))

        return af

    # Compute a unique hash value for the graph structure
    @staticmethod
    def computeWeisfeilerLehmanHash(af: ArgFramework) -> str:
        G = GraphConverter.afToNetworkX(af)
        return nx.weisfeiler_lehman_graph_hash(G)
