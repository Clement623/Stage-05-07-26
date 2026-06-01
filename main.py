from Src.Parse.Parser import Parser
from Src.Core.Argument import Argument
from Src.CaseFile.CaseBase import CaseBase
from Src.CaseFile.Case import Case
from Src.CaseFile.Problem import Problem
from Src.CaseFile.Questions.XinExtension import XinExtension
from CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Situation import Situation
from Src.ExtFile.Admissible import Admissible
from CaseFile.Solver.Solver import Solver
from Src.CaseFile.GraphConverter import GraphConverter


Af = Parser(r"Test\Test_af\graph1.af").parse()
Af2 = Parser(r"Test\Test_af\graph2.af").parse()
situation = Situation(Af)
semantic = Admissible()
question = XinExtension(Argument(1), semantic)
problem = Problem(situation, question)
solution = BooleanSolution(problem, True)
case1 = Case(problem, solution)
CB = CaseBase()
CB.addCase(case1)
situation = Situation(Af2)
semantic = Admissible()
question = XinExtension(Argument(1), semantic)
problem = Problem(situation, question)
converter = GraphConverter()
solver = Solver(CB, converter)
print(solver.solve(problem))
