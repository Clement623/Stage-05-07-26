from .Specialist import Specialist
from Src.ExtFile.Grounded import Grounded
from Src.ExtFile.Extension import Extension


class GroundedSpecialist(Specialist):
    def __init__(self):
        super().__init__()

    def process(self):
        label = {}
        und_pre = {}
        to_be_in = set()
        af = self.getProblem().getSituation().getAF()

        for x in af.getArguments():
            label[x] = "undecided"
            attackers = af.getAttackedBy().get(x, set())
            und_pre[x] = len(attackers)

            if und_pre[x] == 0:
                to_be_in.add(x)

        while to_be_in:
            x = to_be_in.pop()
            label[x] = "in"

            targets_of_x = af.getTarget().get(x, set())
            for y in targets_of_x:
                if label.get(y) != "out":
                    label[y] = "out"

                    targets_of_y = af.getTarget().get(y, set())
                    for z in targets_of_y:
                        if label.get(z) == "undecided":
                            und_pre[z] -= 1
                            if und_pre[z] == 0:
                                to_be_in.add(z)

        grounded_set = {x for x in af.iterArgument() if label.get(x) == "in"}
        return Extension(grounded_set, Grounded())
