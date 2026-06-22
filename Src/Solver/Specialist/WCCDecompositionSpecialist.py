from .Specialist import Specialist
from Src.CaseFile.GraphConverter import GraphConverter
import networkx as nx
from Src.CaseFile.Situation import Situation
from Src.CaseFile.Problem import Problem

class WCCDecompositionSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    def process(self):
        af = self.getProblem().getSituation().getAF()
        G = GraphConverter.afToNetworkX(af)
        listWCCGraph = [G.subgraph(wcc) for wcc in nx.weakly_connected_components(G)]
        problems_list = []
        
        question=self.getProblem().getQuestion()
        if hasattr(question, 'getArgument'):
            target_arg = question.getArgument().getIndex()
        else:
            target_arg = None

        for wccGraph in listWCCGraph:
            if target_arg is not None and target_arg not in wccGraph.nodes():
                continue
            #Convert the NetworkX subgraph back into an ArgFramework
            sub_af = GraphConverter.networkXToAf(wccGraph)      
            #Wrap it inside a new Situation and match it with the original Question
            sub_problem = Problem(Situation(sub_af), question)
            problems_list.append(sub_problem)
        return problems_list
