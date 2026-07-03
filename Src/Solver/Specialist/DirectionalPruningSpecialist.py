from .Specialist import Specialist


class DirectionalPruningSpecialist(Specialist):
    """
    Specialist that computes if a part of a graph is essential
    when looking for information about a specific argument.
    """

    def __init__(self):
        super().__init__()

    def process(self):
        """Run the pruning process (not implemented yet)."""
        pass
