from .Specialist import Specialist


class BaseEnrichmentSpecialist(Specialist):
    """Specialist check if a case need to be add to the caseBase"""
    def process(self):
        pass
