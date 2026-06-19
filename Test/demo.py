import sys
import warnings


warnings.filterwarnings("ignore", category=UserWarning, module="networkx")
sys.path.insert(0, ".")
from Src.Solver.Strategy.CBRStrategy.LinearPatternIsomorphismStrategy import LinearPatternIsomorphismStrategy
from Src.CaseFile.Case import Case
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Situation import Situation
from Src.CaseFile.Questions.AllExtensions import AllExtensions
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
from Src.Core.Attack import Attack
from Src.ExtFile.Preferred import Preferred
from Src.ExtFile.Extension import Extension
from Src.Solver.Specialist.GroundedSpecialist import GroundedSpecialist
from Src.Solver.Specialist.GroundedReductionSpecialist import GroundedReductionSpecialist
from Src.Solver.Orchestrator import Orchestrator
from Src.Solver.Strategy.CBRStrategy.GroundedIsomorphismStrategy import GroundedIsomorphismStrategy
from Src.CaseFile.Solutions.Solution import Solution

def makeAF(*args, attacks=[]):
    af = ArgFramework()
    for i in args:
        af.addArgument(Argument(i))
    for f, t in attacks:
        af.addAttack(Attack(Argument(f), Argument(t)))
    return af

print("="*30)
print('Test 1: The Grounded Isomorphism Strategy')
print("the goal of this test is to return all preferred extensions of a argumentation framework")
#Step 1: Create a ArgFramework
af_target=makeAF(1,2,3,4,5,6, attacks=[(1,2), (2,3), (3,2), (4,3), (5,2), (6,5), (5,6)])
#Step 2: Create the Problem so a Question and a Situation
problem=Problem(Situation(af_target), AllExtensions(Preferred()))
orchestrator=Orchestrator()
strategy= GroundedIsomorphismStrategy()

gr=GroundedSpecialist()
gr.setProblem(problem)
grounde=gr.process()
print("In first the strategy calcul the grounded extension")
print(f"The semantics grounded: {grounde.getExtArgument()}")
gr_reduc=GroundedReductionSpecialist()
gr_reduc.setGroundedExtension(grounde)
gr_reduc.setProblem(problem)
newProblem=gr_reduc.process()

print("Secondly it reduc the graph by the grounded")

print(f"The graph reduc by the grounded: {newProblem.getSituation().getAF()}")
cb=CaseBase()
af_case1=makeAF(1,2,attacks=[(1,2)])
sol_ext_base = SetExtensionSolution({
    Extension({Argument(1)}, semantics=Preferred())
})
cb.addCase(Case(Problem(Situation(af_case1), AllExtensions(Preferred())),sol_ext_base))
af_case2=makeAF(1,2, attacks=[(1,2),(2,1)])
sol_ext_base2 = SetExtensionSolution({
    Extension({Argument(1)}, semantics=Preferred()),
    Extension({Argument(2)}, semantics=Preferred())
})
cb.addCase(Case(Problem(Situation(af_case2), AllExtensions(Preferred())),sol_ext_base2))

print("Thridly it compare the reduc with the case base to search a isomorphism")
print("Here the second case is isomorph so it pick the solution")
print("The solution is: ")
strategy.setCaseBase(cb)
orchestrator.setStrategy(strategy)
sol=orchestrator.solve(problem)
for ext in sol.getAnswer():
    print(ext.getExtArgument())

print("\n" + "="*30)
print('Test 2: The Linear Pattern Isomorphism Strategy')
print("The goal of this test is to return all preferred extensions by compressing linear chains of attacks")

# Step 1: Create a ArgFramework with linear chains (1 -> 2 -> 3 -> 4) and a cycle (1 <-> 5)
af_target_linear = makeAF(1, 2, 3, 4, 5, attacks=[(1, 2), (2, 3), (3, 4), (1, 5), (5, 1)])
problem_linear = Problem(Situation(af_target_linear), AllExtensions(Preferred()))
strategy_linear = LinearPatternIsomorphismStrategy()

print(f"Target graph for linear pattern strategy: {af_target_linear}")
sem=Preferred()
# Step 2: Create a separate case base for the linear strategy
af_base_case_linear = makeAF(6, 7, 8, attacks=[(6, 7), (7, 6), (6, 8)])
sol_ext_base_linear = SetExtensionSolution({
    Extension({Argument(6), Argument(8)}, semantics=sem),
    Extension({Argument(7)}, semantics=sem)
})
cb.addCase(Case(Problem(Situation(af_base_case_linear), AllExtensions(sem)), sol_ext_base_linear))

print("Thirdly it compresses the linear paths and compares the result with the case base")
strategy_linear.setCaseBase(cb)
orchestrator.setStrategy(strategy_linear)
sol_2 = orchestrator.solve(problem_linear)

print("The solution is: ")
for ext in sol_2.getAnswer():
    print(ext.getExtArgument())
print("="*30)

print("="*40)
print('Combined Test: Grounded Strategy then Linear Strategy')
print("Goal: First reduce via Grounded extension, then process the remainder via Linear Pattern")
print("="*40)
af_combined_target = makeAF(
    1, 2, 3, 4, 5, 10, 11, 
    attacks=[(10, 11), (1, 2), (2, 3), (3, 4), (1, 5), (5, 1)])
problem_combined = Problem(Situation(af_combined_target), AllExtensions(sem))
print(f"Target Framework: {af_combined_target}\n")
af_core_case = makeAF(6, 7, 8, attacks=[(6, 7), (7, 6), (6, 8)])
sol_core_case = SetExtensionSolution({
    Extension({Argument(6), Argument(8)}, semantics=sem),
    Extension({Argument(7)}, semantics=sem)
})
cb.addCase(Case(Problem(Situation(af_core_case), AllExtensions(sem)), sol_core_case))
gr_strategy=GroundedIsomorphismStrategy()
gr_strategy.setCaseBase(cb)
orchestrator.setStrategy(gr_strategy)
result=orchestrator.solve(problem_combined)
if not isinstance(result, Problem):
    print("The solution is: ")
    for ext in result.getAnswer():
        print(ext.getExtArgument())
print("We don't conclude with the grounded strategy")
linear_strategy=LinearPatternIsomorphismStrategy()
linear_strategy.setCaseBase(cb)
orchestrator.setStrategy(linear_strategy)
result=orchestrator.solve(result)
if isinstance(result, Solution):
    print("The solution is: ")
    for ext in result.getAnswer():
        print(ext.getExtArgument())