from .Specialist import Specialist
from Src.CaseFile.Problem import Problem
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Attack import Attack
from Src.CaseFile.Situation import Situation

class LinearPatternSpecialist(Specialist):
    def __init__(self):
            super().__init__()
            self.__patterns = None

    def setPatterns(self, patterns: list):
        self.__patterns = patterns

    def getPatterns(self) -> list:
        return self.__patterns

    def findLinearpattern(self):
        problem = self.getProblem()
        af = problem.getSituation().getAF()
        target, attackedBy = af.getTarget(), af.getAttackedBy()
        
        patterns = []
        visited = set()  
        
        for arg in af.iterArgument():
            if arg in visited:
                continue
                
            if len(target.get(arg, set())) == 1 and len(attackedBy.get(arg, set())) == 1:
                pattern_right = [arg]
                arg_attacked = list(target[arg])[0] 
                
                while len(target.get(arg_attacked, set())) == 1 and len(attackedBy.get(arg_attacked, set())) == 1:
                    if arg_attacked in pattern_right: 
                        break
                    pattern_right.append(arg_attacked)
                    arg_attacked = list(target[arg_attacked])[0]
                
                pattern_right.append(arg_attacked)
                pattern_left = []
                arg_attacker = list(attackedBy[arg])[0]
                
                while len(target.get(arg_attacker, set())) == 1 and len(attackedBy.get(arg_attacker, set())) == 1:
                    if arg_attacker in pattern_left or arg_attacker in pattern_right:
                        break
                    pattern_left.append(arg_attacker)
                    arg_attacker = list(attackedBy[arg_attacker])[0]
                
                pattern_left.append(arg_attacker)

                pattern_left = pattern_left[::-1]
                full_pattern = pattern_left + pattern_right

                for middle_arg in full_pattern[1:-1]:
                    visited.add(middle_arg)

                if len(full_pattern) >= 4 and len(full_pattern) % 2 == 0:
                    patterns.append(full_pattern)
                    
        return patterns
    
    def process(self) -> Problem:
        problem = self.getProblem()
        if problem is None:
            return None
        
        self.setPatterns(self.findLinearpattern())    
        af = problem.getSituation().getAF()
        patterns = self.getPatterns()
        
        if not patterns:
            return problem
        args_to_remove = set()
        for pattern in patterns:
            for middle_arg in pattern[1:-1]:
                args_to_remove.add(middle_arg)

        new_af = ArgFramework()

        for arg in af.iterArgument():
            if arg not in args_to_remove:
                new_af.addArgument(arg)
        for attacker in af.iterArgument():
            if attacker in args_to_remove:
                continue
            for target in af.getTarget()[attacker]:
                if target not in args_to_remove:
                    new_af.addAttack(Attack(attacker, target))

        for pattern in patterns:
            start_arg = pattern[0]
            end_arg = pattern[-1]
            if start_arg in new_af.getArguments() and end_arg in new_af.getArguments():
                new_af.addAttack(Attack(start_arg, end_arg))

        new_situation = Situation(new_af)
        new_problem = Problem(new_situation, problem.getQuestion())
        
        return new_problem