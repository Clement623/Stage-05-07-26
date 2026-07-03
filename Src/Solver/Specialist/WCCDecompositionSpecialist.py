from .Specialist import Specialist
from Src.CaseFile.GraphConverter import GraphConverter
import networkx as nx
from Src.CaseFile.Situation import Situation
from Src.CaseFile.Problem import Problem

class WCCDecompositionSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    def order_problems(self, problems: list, question) -> list:
        # For now, return the problems in the same order as they were decomposed
        # This method can be extended later to sort by question type, component size, etc.
        return problems

    def process(self):
        # Convert the AF to a NetworkX graph and split it into weakly connected components
        af = self.getProblem().getSituation().getAF()
        G = GraphConverter.afToNetworkX(af)
        listWCCGraph = [G.subgraph(wcc) for wcc in nx.weakly_connected_components(G)]
        problems_list = []
        
        question = self.getProblem().getQuestion()

        # If the question targets a specific argument, only keep its component
        if hasattr(question, 'getArgument'):
            target_arg = question.getArgument().getIndex()
        else:
            target_arg = None

        for wccGraph in listWCCGraph:
            # Skip components that don't contain the target argument
            if target_arg is not None and target_arg not in wccGraph.nodes():
                continue

            # Convert the NetworkX subgraph back into an ArgFramework
            sub_af = GraphConverter.networkXToAf(wccGraph)
            # Wrap it inside a new Situation and match it with the original question
            sub_problem = Problem(Situation(sub_af), question)
            problems_list.append(sub_problem)

        return self.order_problems(problems_list, question)