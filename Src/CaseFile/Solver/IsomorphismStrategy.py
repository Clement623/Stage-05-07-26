from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.GraphConverter import GraphConverter
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Solver.SolverStrategy import SolverStrategy
import networkx as nx
from networkx.algorithms.isomorphism import DiGraphMatcher


class IsomorphismStrategy(SolverStrategy):
    def __init__(self, base: CaseBase, converter: GraphConverter):
        self.__base = base
        self.__converter = converter

    def getBase(self):
        return self.__base

    def getConverter(self):
        return self.__converter

    # Method to find if a graph of a problem have a isomorph in the CaseBase
    def findIsomorph(self, problem: Problem, i=0):
        # check the type
        if not isinstance(problem, Problem):
            raise TypeError("problem need to be a Problem")

        # convert the Af of the problem in the networkx graph
        G1 = self.getConverter().afToNetworkX(problem.getSituation().getAF())
        # Iterate sequentially through the stored cases starting from index i
        for c in self.getBase().getListCase()[i:]:
            situation = c.getProblem().getSituation()
            # Optimization check: graphs can only be isomorphic if they have the exact same node and edge counts
            if (
                len(situation.getAF().getArguments()) == G1.number_of_nodes()
                and len(situation.getAF().getAttacks()) == G1.number_of_edges()
            ):
                G2 = self.getConverter().afToNetworkX(situation.getAF())
                if nx.is_isomorphic(G1, G2):
                    return G1, G2, c, i
            i += 1
        return None

    # The method of the solving
    def solve(self, problem: Problem):
        # chek the good type
        if not isinstance(problem, Problem):
            raise TypeError("problem need to be a Problem")
        i = 0
        # iterate to find all isomorph
        while i < len(self.getBase().getListCase()):
            result = self.findIsomorph(problem, i)
            if result is None:
                return None

            G1, G2, case, i_trouve = result
            # create the matching with the index of two graph
            matcher = DiGraphMatcher(G1, G2)
            target = problem.getQuestion().getArgument().getIndex()
            # Map the new name of Af
            for mapping in matcher.isomorphisms_iter():
                target_in_G2 = mapping[target]
                if (
                    case.getProblem().getQuestion().getArgument().getIndex()
                    == target_in_G2
                ):
                    return case.getSolution()
            i = i_trouve + 1
        return None
