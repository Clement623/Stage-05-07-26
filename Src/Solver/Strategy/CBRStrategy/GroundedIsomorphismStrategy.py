from Src.Solver.Strategy.CBRStrategy.CBRStrategy import CBRStrategy
from Src.Solver.Specialist.GroundedSpecialist import GroundedSpecialist
from Src.Solver.Specialist.GroundedReductionSpecialist import GroundedReductionSpecialist
from Src.Solver.Specialist.IsomorphismSpecialist import IsomorphismSpecialist
from Src.Solver.Specialist.BijectionSpecialist import BijectionSpecialist
from Src.Solver.Specialist.GroundedMergeSolutionSpecialist import GroundedMergeSolutionSpecialist
from Src.CaseFile.Solutions.BooleanSolution import BooleanSolution
from Src.CaseFile.Solutions.SetExtensionSolution import SetExtensionSolution
from Src.CaseFile.Solutions.SingleExtensionSolution import SingleExtensionSolution
from Src.CaseFile.Solutions.UnresolvedSolution import UnresolvedSolution



class GroundedIsomorphismStrategy(CBRStrategy):
    def __init__(self):
        super().__init__()

    def solve(self, problem, caseBase):
        if caseBase is None:
            raise(TypeError('need a caseBase'))
        else:
            self.setCaseBase(caseBase)
        
        grounded_specialist = GroundedSpecialist()
        grounded_specialist.setProblem(problem)
        grounded_ext = grounded_specialist.process()

        question = problem.getQuestion()
        if hasattr(question, 'getArgument'):
            target_arg = question.getArgument() 
            if grounded_ext.isInExtension(target_arg):
                return BooleanSolution(True)
            
            af = problem.getSituation().getAF()
            is_attacked_by_grounded = False
            target_dict = af.getTarget()
            
            for g_arg in grounded_ext.iterExtArgument():
                if target_arg in target_dict.get(g_arg, set()):
                    is_attacked_by_grounded = True
                    break
                    
            if is_attacked_by_grounded:
                return BooleanSolution(False)
        reduced_solution = None
        reduction_specialist = GroundedReductionSpecialist()
        reduction_specialist.setProblem(problem)
        reduction_specialist.setGroundedExtension(grounded_ext)
        new_problem = reduction_specialist.process()

        if len(new_problem.getSituation().getAF().getArguments()) > 0:
            iso_specialist = IsomorphismSpecialist()
            iso_specialist.setCaseBase(self.getCaseBase())
            iso_specialist.setProblem(new_problem)
            result = iso_specialist.process()
            if result is not None:
                matching_case, all_mappings = result
                old_solution = matching_case.getSolution()
                
                question = problem.getQuestion()
                base_question = matching_case.getProblem().getQuestion()
                
                if type(question) is type(base_question):
                    for mapping in all_mappings:
                        
                        if hasattr(question, 'getArgument'):
                            target_index = question.getArgument().getIndex()
                            if target_index not in mapping:
                                continue
                        if question.isEquivalentUnderMapping(base_question, mapping):
                            if isinstance(old_solution, BooleanSolution):
                                reduced_solution = BooleanSolution(old_solution.getAnswer())
                            else:
                                bij_specialist = BijectionSpecialist(mapping, inverse=True)
                                bij_specialist.setElement(old_solution.getAnswer()) 
                                translated_answer = bij_specialist.process()
                                
                                if isinstance(old_solution, SetExtensionSolution):
                                    reduced_solution = SetExtensionSolution(translated_answer)
                                elif isinstance(old_solution, SingleExtensionSolution):
                                    reduced_solution = SingleExtensionSolution(translated_answer)
                                else:
                                    raise TypeError("Unsupported solution type from matching case")
                            break
            else:
                return UnresolvedSolution(new_problem)
            
        merge_specialist = GroundedMergeSolutionSpecialist()
        merge_specialist.setGroundedExtension(grounded_ext)
        merge_specialist.setReducedSolution(reduced_solution)
        merge_specialist.setProblem(problem)

        return merge_specialist.process()
