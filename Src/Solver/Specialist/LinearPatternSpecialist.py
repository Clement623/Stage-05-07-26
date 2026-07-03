from .Specialist import Specialist
from Src.CaseFile.Problem import Problem
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Attack import Attack
from Src.CaseFile.Situation import Situation


class LinearPatternSpecialist(Specialist):
    """
    Specialist that detects linear chains of arguments (each with exactly
    one attacker and one target) and compresses them into a single
    shortcut attack, to simplify the argumentation framework.
    """

    def __init__(self):
        super().__init__()
        # List of detected linear patterns (chains)
        self.__patterns = None

    def setPatterns(self, patterns: list):
        """Set the list of detected patterns."""
        self.__patterns = patterns

    def getPatterns(self) -> list:
        """Return the list of detected patterns."""
        return self.__patterns

    def findLinearpattern(self):
        """Find all linear chains of arguments in the AF."""
        problem = self.getProblem()
        af = problem.getSituation().getAF()
        target, attackedBy = af.getTarget(), af.getAttackedBy()

        patterns = []
        visited = set()

        for arg in af.iterArgument():
            # Skip arguments already part of a detected pattern
            if arg in visited:
                continue

            # An interior node of a linear chain has exactly one attacker and one target
            if len(target.get(arg, set())) == 1 and len(attackedBy.get(arg, set())) == 1:
                # Expand rightward along the chain
                pattern_right = [arg]
                arg_attacked = list(target[arg])[0]

                while len(target.get(arg_attacked, set())) == 1 and len(attackedBy.get(arg_attacked, set())) == 1:
                    # Stop if we loop back (cycle detected)
                    if arg_attacked in pattern_right:
                        break
                    pattern_right.append(arg_attacked)
                    arg_attacked = list(target[arg_attacked])[0]

                # arg_attacked is now the right endpoint of the chain
                pattern_right.append(arg_attacked)

                # Expand leftward along the chain
                pattern_left = []
                arg_attacker = list(attackedBy[arg])[0]

                while len(target.get(arg_attacker, set())) == 1 and len(attackedBy.get(arg_attacker, set())) == 1:
                    # Stop if we loop back or overlap with the right side
                    if arg_attacker in pattern_left or arg_attacker in pattern_right:
                        break
                    pattern_left.append(arg_attacker)
                    arg_attacker = list(attackedBy[arg_attacker])[0]

                # arg_attacker is now the left endpoint of the chain
                pattern_left.append(arg_attacker)

                # Reverse so the left side reads left-to-right, then join both sides
                pattern_left = pattern_left[::-1]
                full_pattern = pattern_left + pattern_right

                # Mark interior nodes as visited so they aren't processed again
                for middle_arg in full_pattern[1:-1]:
                    visited.add(middle_arg)

                # Only keep chains long enough to compress (≥4 nodes, even length)
                if len(full_pattern) >= 4 and len(full_pattern) % 2 == 0:
                    patterns.append(full_pattern)

        return patterns

    def process(self) -> Problem:
        """Compress linear chains in the AF and return a simplified problem."""
        problem = self.getProblem()
        if problem is None:
            return None

        # Detect all linear patterns in the AF
        self.setPatterns(self.findLinearpattern())
        af = problem.getSituation().getAF()
        patterns = self.getPatterns()

        if not patterns:
            return problem

        # Collect all interior nodes to remove (endpoints are kept)
        args_to_remove = set()
        for pattern in patterns:
            for middle_arg in pattern[1:-1]:
                args_to_remove.add(middle_arg)

        # Build a new AF without the interior nodes
        new_af = ArgFramework()

        for arg in af.iterArgument():
            if arg not in args_to_remove:
                new_af.addArgument(arg)

        # Keep all attacks between non-removed arguments
        for attacker in af.iterArgument():
            if attacker in args_to_remove:
                continue
            for target in af.getTarget()[attacker]:
                if target not in args_to_remove:
                    new_af.addAttack(Attack(attacker, target))

        # Add a direct attack from each chain's start to its end (shortcut attack)
        for pattern in patterns:
            start_arg = pattern[0]
            end_arg = pattern[-1]
            if start_arg in new_af.getArguments() and end_arg in new_af.getArguments():
                new_af.addAttack(Attack(start_arg, end_arg))

        new_situation = Situation(new_af)
        new_problem = Problem(new_situation, problem.getQuestion())

        return new_problem