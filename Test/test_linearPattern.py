import sys

sys.path.insert(0, ".")

from Src.Solver.Strategy.CBRStrategy.LinearPatternIsomorphismStrategy import LinearPatternIsomorphismStrategy
from Src.CaseFile.Case import Case
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Situation import Situation
from Src.CaseFile.Questions.XinExtension import XinExtension
from Src.CaseFile.Questions.AllExtensions import AllExtensions
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
from Src.Core.Attack import Attack
from Src.ExtFile.Preferred import Preferred
from Src.ExtFile.Extension import Extension

results = []


def test(name, condition):
    status = "✅ PASS" if condition else "❌ FAIL"
    print(f"  {status} — {name}")
    results.append((name, condition))


def makeAF(*args, attacks=[]):
    af = ArgFramework()
    for i in args:
        af.addArgument(Argument(i))
    for f, t in attacks:
        af.addAttack(Attack(Argument(f), Argument(t)))
    return af

af_target = makeAF(1, 2, 3, 4, 5, attacks=[(1, 2), (2, 3), (3, 4), (1, 5), (5, 1)])
af_grand_target = makeAF(
    1, 2, 3, 4, 5, 6, 7, 8, 9,10,
    attacks=[
        (1, 2), (2, 1),       
        (1, 3), (3, 4), (4, 5), (5, 6), (6, 10),
        (2, 7), (7, 8), (8, 9)          
    ]
)
af_base_case = makeAF(6, 7, 8, attacks=[(6, 7), (7, 6), (6, 8)])
sem = Preferred()
cb = CaseBase()

prob_bool_base = Problem(Situation(af_base_case), XinExtension(Argument(6), sem))
sol_bool_base = BooleanSolution(True)
cb.addCase(Case(prob_bool_base, sol_bool_base))
prob_ext_base = Problem(Situation(af_base_case), AllExtensions(sem))
sol_ext_base = SetExtensionSolution({
    Extension({Argument(6), Argument(8)}, semantics=sem),
    Extension({Argument(7)}, semantics=sem)
})
cb.addCase(Case(prob_ext_base, sol_ext_base))

strategy = LinearPatternIsomorphismStrategy()
strategy.setCaseBase(cb)


print("\n── Tests : LinearPatternIsomorphismStrategy ──")
print(f"The ArgFramework source is: {af_target}")
print(f"We have a case base: {cb}")

prob_linear_1 = Problem(Situation(af_target), XinExtension(Argument(1), sem))
sol_1 = strategy.solve(prob_linear_1)
test("The argument 1 evaluation with linear pattern", 
     sol_1 is not None and isinstance(sol_1, BooleanSolution) and sol_1.getAnswer() is True)

prob_linear_2 = Problem(Situation(af_target), XinExtension(Argument(4), sem))
sol_2 = strategy.solve(prob_linear_2)
test("The argument 4 evaluation with linear pattern", 
     sol_2 is not None and isinstance(sol_2, BooleanSolution) and sol_2.getAnswer() is True)

prob_linear_all = Problem(Situation(af_target), AllExtensions(sem))
sol_3 = strategy.solve(prob_linear_all)
for ext in sol_3.getAnswer():
    print(ext.getExtArgument())
test("Enumeration with linear pattern and isomorphism", 
     sol_3 is not None and isinstance(sol_3, SetExtensionSolution))

af_base_case2 = makeAF(
    10, 11, 12, 13, 
    attacks=[
        (10, 11), (11, 10), 
        (10, 12),           
        (11, 13)        
    ]
)
prob_ext_base2 = Problem(Situation(af_base_case2), AllExtensions(sem))
sol_ext_base2 = SetExtensionSolution({
    Extension({Argument(10), Argument(13)}, semantics=sem),
    Extension({Argument(11), Argument(12)}, semantics=sem)
})
cb.addCase(Case(prob_ext_base2, sol_ext_base2))


strategy = LinearPatternIsomorphismStrategy()
strategy.setCaseBase(cb)

prob_linear_all2=Problem(Situation(af_grand_target),AllExtensions(sem))
sol_4=strategy.solve(prob_linear_all2)
for ext in sol_4.getAnswer():
    print(ext.getExtArgument())
test("Enumeration with linear pattern and isomorphism", 
     sol_4 is not None and isinstance(sol_4, SetExtensionSolution))



passed = sum(1 for _, r in results if r)
total = len(results)
print(f"\n{'─' * 40}")
print(f"  {passed}/{total} tests passed by LinearPatternIsomorphismStrategy")
if passed < total:
    print("  Tests failed :")
    for name, r in results:
        if not r:
            print(f"    ✗ {name}")
print(f"{'─' * 40}\n")