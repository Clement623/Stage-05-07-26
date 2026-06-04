import sys

sys.path.insert(0, ".")

from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
from Src.Core.Attack import Attack
from Src.CaseFile.Situation import Situation
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Case import Case
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.GraphConverter import GraphConverter
from Src.CaseFile.Questions.XinExtension import XinExtension
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.ExtFile.Extension import Extension
from Src.ExtFile.Admissible import Admissible
from Src.ExtFile.Complete import Complete
from Src.ExtFile.Stable import Stable
from Src.Solver.ProblemSpecialist.IsomorphismSpecialist import IsomorphismSpecialist
from Src.Solver.ProblemSpecialist.TransformationSpecialist.ArgumentTransformationSpecialist import (
    ArgumentTransformationSpecialist,
)
from Src.Solver.ProblemSpecialist.TransformationSpecialist.AttackTransformationSpecialist import (
    AttackTransformationSpecialist,
)
from Src.Solver.Strategy.TransformAndIsomorphStrategy import (
    TransformAndIsomorphStrategy,
)
from Src.Solver.Orchestrator import Orchestrator

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


def makeCase(af, questionArgIndex, answer):
    sem = Admissible()
    q = XinExtension(Argument(questionArgIndex), sem)
    s = BooleanSolution(answer)
    p = Problem(Situation(af), q)
    return Case(p, s)


def makeProblem(af, questionArgIndex):
    sem = Admissible()
    q = XinExtension(Argument(questionArgIndex), sem)
    return Problem(Situation(af), q)


print("ArgFramework")

af = makeAF(1, 2, 3, attacks=[(1, 2), (2, 3)])
test("addArgument : 3 arguments présents", len(af.getArguments()) == 3)
test("addAttack : 2 attaques présentes", len(af.getAttacks()) == 2)
test("target 1 attaque 2", Argument(2) in af.getTarget()[Argument(1)])
test("attackedBy 2 est attaqué par 1", Argument(1) in af.getAttackedBy()[Argument(2)])

af2 = makeAF(1, 2, 3, attacks=[(1, 2), (2, 3)])
test("__eq__ deux AF identiques", af == af2)

af3 = makeAF(1, 2, attacks=[(1, 2)])
test("__eq__ deux AF différents", af != af3)

af.removeArgument(Argument(2))
test("removeArgument supprime l'argument", not af.isInArguments(Argument(2)))
test("removeArgument supprime les attaques", len(af.getAttacks()) == 0)

print("GraphConverter")

af_a = makeAF(1, 2, attacks=[(1, 2)])
af_b = makeAF(3, 4, attacks=[(3, 4)])

hash_a = GraphConverter.computeWeisfeilerLehmanHash(af_a)
hash_b = GraphConverter.computeWeisfeilerLehmanHash(af_b)
test("hash identique pour deux AF isomorphes", hash_a == hash_b)

af_c = makeAF(1, 2, 3, attacks=[(1, 2), (2, 3)])  # 1 -> 2 -> 3
hash_c = GraphConverter.computeWeisfeilerLehmanHash(af_c)

af_d = makeAF(1, 2, 3, attacks=[(1, 2), (3, 2)])  # 1 -> 2 <- 3
hash_d = GraphConverter.computeWeisfeilerLehmanHash(af_d)

test("hash différent si direction inversée", hash_c != hash_d)

print("IsomorphismSpecialist")

af_base = makeAF(1, 2, attacks=[(1, 2)])
case1 = makeCase(af_base, 1, True)
cb = CaseBase()
cb.addCase(case1)

af_prob = makeAF(1, 2, attacks=[(1, 2)])
prob = makeProblem(af_prob, 1)
spec = IsomorphismSpecialist(cb)
spec.setProblem(prob)
sol = spec.process()
test("iso direct : solution trouvée", sol is not None)
test(
    "iso direct : réponse correcte (True)", sol is not None and sol.getAnswer() == True
)

af_iso = makeAF(5, 6, attacks=[(5, 6)])
prob_iso = makeProblem(af_iso, 5)
spec2 = IsomorphismSpecialist(cb)
spec2.setProblem(prob_iso)
sol2 = spec2.process()
test("iso avec indices différents : trouvé", sol2 is not None)

af_no = makeAF(1, 2, 3, attacks=[(1, 2), (2, 3)])
prob_no = makeProblem(af_no, 1)
spec3 = IsomorphismSpecialist(cb)
spec3.setProblem(prob_no)
sol3 = spec3.process()
test("pas d'isomorphe : retourne None", sol3 is None)

print("ArgumentTransformationSpecialist")

af_t = makeAF(1, 2, attacks=[(1, 2)])
prob_t = makeProblem(af_t, 1)
transformer = ArgumentTransformationSpecialist()
transformer.setProblem(prob_t)
newProb = transformer.process()

newAf = newProb.getSituation().getAF()
test("argument ajouté : AF original inchangé", len(af_t.getArguments()) == 2)
test("argument ajouté : newAF a 3 arguments", len(newAf.getArguments()) == 3)
test("argument ajouté : pas de nouvelles attaques", len(newAf.getAttacks()) == 1)
test("argument ajouté : index correct (3)", Argument(3) in newAf.getArguments())
test(
    "question préservée après deepcopy",
    newProb.getQuestion().getArgument().getIndex() == 1,
)

print("AttackTransformationSpecialist")

af_att = makeAF(1, 2, 3)
prob_att = makeProblem(af_att, 1)
attSpec = AttackTransformationSpecialist()
attSpec.setAttack(1, 3)
attSpec.setProblem(prob_att)
newProbAtt = attSpec.process()

newAfAtt = newProbAtt.getSituation().getAF()
test("attaque ajoutée : AF original inchangé", len(af_att.getAttacks()) == 0)
test("attaque ajoutée : newAF a 1 attaque", len(newAfAtt.getAttacks()) == 1)
test(
    "attaque ajoutée : bonne direction (1→3)",
    Attack(Argument(1), Argument(3)) in newAfAtt.getAttacks(),
)

try:
    badSpec = AttackTransformationSpecialist()
    badSpec.setProblem(prob_att)
    badSpec.process()
    test("setAttack manquant lève ValueError", False)
except ValueError:
    test("setAttack manquant lève ValueError", True)

print("TransformAndIsomorphStrategy")

af_s = makeAF(1, 2, attacks=[(1, 2)])
case_s = makeCase(af_s, 1, True)
cb2 = CaseBase()
cb2.addCase(case_s)
strategy = TransformAndIsomorphStrategy(cb2)

prob_direct = makeProblem(makeAF(1, 2, attacks=[(1, 2)]), 1)
sol_direct = strategy.solve(prob_direct)
test("passe 1 : solution trouvée", sol_direct is not None)
test(
    "passe 1 : réponse correcte",
    sol_direct is not None and sol_direct.getAnswer() == True,
)

print("\n── TransformAndIsomorphStrategy — passe 2 (transfo + iso) ──")

af_base2 = makeAF(1, 2, 3, attacks=[(1, 2)])
case_base2 = makeCase(af_base2, 1, True)
cb3 = CaseBase()
cb3.addCase(case_base2)
strategy2 = TransformAndIsomorphStrategy(cb3)

prob_p2 = makeProblem(makeAF(1, 2, attacks=[(1, 2)]), 1)
sol_p2 = strategy2.solve(prob_p2)
test("passe 2 : solution trouvée via transfo", sol_p2 is not None)
test("passe 2 : réponse correcte", sol_p2 is not None and sol_p2.getAnswer() == True)

prob_none = makeProblem(makeAF(1, 2, 3, attacks=[(1, 2), (2, 3), (3, 1)]), 1)
sol_none = strategy2.solve(prob_none)
test("aucune passe ne trouve : retourne None", sol_none is None)

print("Orchestrator")

orch = Orchestrator()
try:
    orch.solve(makeProblem(makeAF(1), 1))
    test("solve sans strategy lève ValueError", False)
except ValueError:
    test("solve sans strategy lève ValueError", True)

orch.setStrategy(strategy2)
sol_orch = orch.solve(makeProblem(makeAF(1, 2, attacks=[(1, 2)]), 1))
test("orchestrator délègue correctement", sol_orch is not None)

print("\n── Sémantiques d'Argumentation ──")

# Graphe de test : 1 -> 2 -> 3  et  4 -> 4 (boucle réflexive)
af_sem = makeAF(1, 2, 3, 4, attacks=[(1, 2), (2, 3), (4, 4)])

sem_admissible = Admissible()

# {1, 3} est sans conflit et 1 défend 3 contre 2 -> Admissible
ext_ok = Extension({Argument(1), Argument(3)})
test(
    "Admissible : {1, 3} est une extension valide",
    sem_admissible.isExtension(af_sem, ext_ok),
)

# {1, 2} contient un conflit (1->2) -> Non admissible
ext_conflict = Extension({Argument(1), Argument(2)})
test(
    "Admissible : {1, 2} rejeté pour conflit",
    not sem_admissible.isExtension(af_sem, ext_conflict),
)

# {3} n'est pas défendu contre 2 -> Non admissible
ext_undefended = Extension({Argument(3)})
test(
    "Admissible : {3} rejeté car non défendu",
    not sem_admissible.isExtension(af_sem, ext_undefended),
)

sem_complete = Complete()

# {1, 3} défend 1 et 3, et aucun autre argument n'est défendu par {1, 3} -> Complet
test(
    "Complete : {1, 3} est une extension complète",
    sem_complete.isExtension(af_sem, ext_ok),
)

# {} (l'extension vide) défend l'argument 1. Comme 1 n'est pas dedans, {} n'est PAS complète
ext_vide = Extension(set())
test(
    "Complete : Extension vide rejetée si elle omet un argument défendu (1)",
    not sem_complete.isExtension(af_sem, ext_vide),
)


sem_stable = Stable()

# Dans af_sem, l'extension {1, 3} attaque l'argument restant {2}, mais n'attaque pas {4}. Donc non stable.
test(
    "Stable : {1, 3} rejeté car il n'attaque pas tous les arguments extérieurs (4)",
    not sem_stable.isExtension(af_sem, ext_ok),
)

# Nouveau graphe adapté pour la stabilité : 1 -> 2 et 3 -> 2
af_stable_valid = makeAF(1, 2, 3, attacks=[(1, 2), (3, 2)])
ext_stable = Extension({Argument(1), Argument(3)})
# {1, 3} n'a pas de conflit et attaque le seul élément extérieur {2} -> Stable
test(
    "Stable : {1, 3} est stable (attaque tout le monde à l'extérieur)",
    sem_stable.isExtension(af_stable_valid, ext_stable),
)


# ─────────────────────────────────────────────
# Résumé
# ─────────────────────────────────────────────
passed = sum(1 for _, r in results if r)
total = len(results)
print(f"\n{'─' * 40}")
print(f"  {passed}/{total} tests passés")
if passed < total:
    print("  Tests échoués :")
    for name, r in results:
        if not r:
            print(f"    ✗ {name}")
print(f"{'─' * 40}\n")
