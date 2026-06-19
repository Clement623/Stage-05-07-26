import sys

sys.path.insert(0, ".")

from Src.Solver.Strategy.CBRStrategy.GroundedIsomorphismStrategy import (GroundedIsomorphismStrategy)
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

af_target = makeAF(1, 2, 3, 4, attacks=[(1, 2), (3, 4), (4, 3)])

af_base_case = makeAF(5, 6, attacks=[(5, 6), (6, 5)])

sem = Preferred()
cb = CaseBase()

prob_bool_base = Problem(Situation(af_base_case), XinExtension(Argument(5), sem))
sol_bool_base = BooleanSolution(True)
cb.addCase(Case(prob_bool_base, sol_bool_base))

prob_ext_base = Problem(Situation(af_base_case), AllExtensions(sem))
sol_ext_base = SetExtensionSolution({
    Extension({Argument(5)}, semantics=sem),
    Extension({Argument(6)}, semantics=sem)
})
cb.addCase(Case(prob_ext_base, sol_ext_base))

strategy = GroundedIsomorphismStrategy()
strategy.setCaseBase(cb)


print("\n── Tests : GroundedIsomorphismStrategy ──")
print(f'The ArgFramework source is: {af_target}')
print(f'We have a case base: {cb}')
#the Argument 1 is in the grounded so he needs to be True 
prob_grounded_in = Problem(Situation(af_target), XinExtension(Argument(1), sem))
sol_1 = strategy.solve(prob_grounded_in)
test("The argument 1 is in the grounded extension", 
     sol_1 is not None and isinstance(sol_1, BooleanSolution) and sol_1.getAnswer() is True)

#the Argument 2 is attack by a argument of the grounded is never in a extension
prob_grounded_out = Problem(Situation(af_target), XinExtension(Argument(2), sem))
sol_2 = strategy.solve(prob_grounded_out)
test("Argument 2 is attack by a Argument of the Grounded extension", 
     sol_2 is not None and isinstance(sol_2, BooleanSolution) and sol_2.getAnswer() is False)

#The Argument 3 is not attack not in the grounded
prob_reduced_iso = Problem(Situation(af_target), XinExtension(Argument(3), sem))
sol_3 = strategy.solve(prob_reduced_iso)
test("Argument 3 is resolve with the isomorph problem", 
     sol_3 is not None and isinstance(sol_3, BooleanSolution) and sol_3.getAnswer() is True)

prob_all_extensions = Problem(Situation(af_target), AllExtensions(sem))
sol_4 = strategy.solve(prob_all_extensions)
print(sol_4)
test("Enumeration with isomorphism", sol_4 is not None and isinstance(sol_4, SetExtensionSolution) and sol_4.getAnswer() == {Extension({Argument(1), Argument(3)}, semantics=sem), Extension({Argument(1), Argument(4)}, semantics=sem)})




passed = sum(1 for _, r in results if r)
total = len(results)
print(f"\n{'─' * 40}")
print(f"  {passed}/{total} tests passed by GroundedIsomorphismStrategy")
if passed < total:
    print("  Tests loose :")
    for name, r in results:
        if not r:
            print(f"    ✗ {name}")
print(f"{'─' * 40}\n")