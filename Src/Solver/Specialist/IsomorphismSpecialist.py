from networkx.algorithms.isomorphism import DiGraphMatcher
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.GraphConverter import GraphConverter
from Src.Solver.Specialist.Specialist import Specialist


# Search if the problem has an isomorph in the case base
class IsomorphismSpecialist(Specialist):
    def __init__(self):
        super().__init__()
        self.__base = None

    def getCaseBase(self) -> CaseBase:
        return self.__base
    
    def setCaseBase(self, base: CaseBase):
        if not isinstance(base, CaseBase):
            raise TypeError("need a CaseBase")
        self.__base = base

    def _is_compatible_question(self, question_a, question_b) -> bool:
        # For now, only exact question type match is considered compatible
        # This method can be extended later to support question hierarchy or partial compatibility
        return type(question_a) is type(question_b)

    def process(self) -> tuple:
        # Convert the problem's AF to a graph and compute its hash for fast lookup
        Af = self.getProblem().getSituation().getAF()
        HashGraph = GraphConverter.computeWeisfeilerLehmanHash(Af)
        
        # Filter the case base to only structurally similar cases
        candidates = self.getCaseBase().get_candidates_by_hash(HashGraph)
        if not candidates:
            return None

        # Sort candidates: exact question type match first
        question = self.getProblem().getQuestion()
        candidates.sort(key=lambda c: not self._is_compatible_question(c.getProblem().getQuestion(), question))

        G1 = GraphConverter.afToNetworkX(Af)

        # Check each candidate for a true graph isomorphism
        for c in candidates:
            situation = c.getProblem().getSituation()
            G2 = GraphConverter.afToNetworkX(situation.getAF())
            matcher = DiGraphMatcher(G1, G2)

            if matcher.is_isomorphic():
                # Return the matching case along with all valid argument mappings
                all_mappings = list(matcher.isomorphisms_iter())
                return c, all_mappings
                    
        return None