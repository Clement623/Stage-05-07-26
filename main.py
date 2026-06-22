import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
from Src.Core.Attack import Attack
from Src.CaseFile.Situation import Situation
from Src.CaseFile.Problem import Problem
from Src.CaseFile.CaseBase import CaseBase
from Src.Solver.Orchestrator import Orchestrator
from Src.Solver.Strategy.CBRStrategy.GroundedIsomorphismStrategy import GroundedIsomorphismStrategy
from Src.CaseFile.Questions.AllExtensions import AllExtensions
from Src.ExtFile.Preferred import Preferred
from Src.Solver.Specialist.WCCDecompositionSpecialist import WCCDecompositionSpecialist
from Src.Solver.Specialist.WCCRecompositionSpecialist import WCCRecompositionSpecialist
from Src.Solver.Strategy.CBRStrategy.LinearPatternIsomorphismStrategy import LinearPatternIsomorphismStrategy
from Src.Solver.Strategy.CBRStrategy.CBRStrategy import CBRStrategy
from Src.CaseFile.Solutions.UnresolvedSolution import UnresolvedSolution
from Src.Solver.Strategy.DirectResolutionStrategy import DirectResolutionStrategy
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.ExtFile.Extension import Extension
from Src.CaseFile.Case import Case

def makeAF(*args, attacks=[]):
    af = ArgFramework()
    for i in args:
        af.addArgument(Argument(i))
    for f, t in attacks:
        af.addAttack(Attack(Argument(f), Argument(t)))
    return af

def solveProblem(problem, caseBase):
    # Step 1: Decompose the global problem into Weakly Connected Components (WCC)
    wcc_specialist = WCCDecompositionSpecialist()
    wcc_specialist.setProblem(problem)
    list_problem = wcc_specialist.process()

    unresolved_problem = list_problem.copy()
    orchestrator = Orchestrator()
    
    # Ordered pipeline of strategies to apply sequentially
    list_strategy = [GroundedIsomorphismStrategy(), LinearPatternIsomorphismStrategy(), DirectResolutionStrategy()]
    resolved_solution = []
    
    # Process each isolated sub-problem
    while unresolved_problem:
        problem_to_solve = unresolved_problem.pop()
        
        # Try strategies one by one until a valid solution is found
        for strategy in list_strategy:
            orchestrator.setStrategy(strategy)
            
            # Pass the case base only if the strategy relies on Case-Based Reasoning (CBR)
            if isinstance(strategy, CBRStrategy):
                solution = orchestrator.solve(problem_to_solve, caseBase)
            else:
                solution = orchestrator.solve(problem_to_solve, None)
            
            # If the strategy successfully solved the sub-problem, store it and move to the next WCC
            if not isinstance(solution, UnresolvedSolution):
                resolved_solution.append(solution)
                break
            
            # Update the problem instance in case a strategy performed a partial reduction
            problem_to_solve = solution.getProblem()

            
    # Step 2: Merge and recompose all sub-solutions into a unified global solution
    wcc_recomposition_specialist = WCCRecompositionSpecialist()
    wcc_recomposition_specialist.setSolutions(resolved_solution)
    for solution in resolved_solution:
        print(f"partial Solution: {solution}")
    global_solution = wcc_recomposition_specialist.process()
    
    return global_solution

def main():
    print("Begin the Test")
    cb = CaseBase()
    sem_preferred = Preferred()

    # Case 1 initialization
    af_case = makeAF(1, 2, attacks=[(1, 2), (2,1)])
    problem = Problem(Situation(af_case), AllExtensions(sem_preferred))
    sol_case = SetExtensionSolution({
        Extension({Argument(1)}, semantics=sem_preferred),
        Extension({Argument(2)}, semantics=sem_preferred)
    })
    cb.addCase(Case(problem, sol_case))

    # Case 2 initialization
    af_case = makeAF(1, 2, 3, attacks=[(1, 2), (2, 1), (2, 3)])
    problem = Problem(Situation(af_case), AllExtensions(sem_preferred))
    sol_case = SetExtensionSolution({
        Extension({Argument(1), Argument(3)}, semantics=sem_preferred),
        Extension({Argument(2)}, semantics=sem_preferred)
    })
    cb.addCase(Case(problem, sol_case))

    print("We have a case base with the case: 1<->2 with the solution {{1}, {2}} for the question: All preferred extensions")
    print("We have a case base with the case: 1<->2->3 with the solution {{1,3}, {2}} for the question: All preferred extensions")
    
    af_target = makeAF(1, 2, 3, 4, 5, 6, 7, 8, 9, attacks=[(1, 2), (2, 1), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (9, 8)])
    print("We want to return all preferred extensions of the framework: \n" \
          "1<->2->3->4->5 6->7->8<->9")
          
    question = AllExtensions(Preferred())
    problem = Problem(Situation(af_target), question)
    solution = solveProblem(problem, cb)
    
    print("Step 1: Separate the problem into two WCCs")

    print("Step 2: Solve the second WCC:")
    print("  - Select GroundedIsomorphismStrategy and try to solve the sub-problem")
    print("  - It calculates the grounded part and reduces the graph")
    print("  - It finds an isomorphic graph in the case base and reuses its solution")

    print("Step 3: Solve the first WCC:")
    print("  - Select GroundedIsomorphismStrategy and try to solve the sub-problem")
    print("  - This Strategy does not work with this problem, selecting the next one: LinearPatternIsomorphismStrategy")
    print("  - The Strategy detects a pattern (2->3->4->5) and reduces the AF to 1<->2->3")
    print("  - It finds an isomorphic case, reuses its solution, and returns the updated result")

    print("Step 4: Merge the two partial solutions to obtain the global solution")
    print("\nFinal Recomposed Solution:")
    print(solution)

if __name__ == "__main__":
    main()