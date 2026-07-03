from .CBRStrategy import CBRStrategy


class DirectionalCBRStrategy(CBRStrategy):
    """
    CBR strategy based on pruning (removing parts of the graph
    that are not essential for the query).
    """

    def solve(self, problem):
        """Solve the problem using directional pruning (not implemented yet)."""
        pass