from Src.Core.Argument import Argument
from Src.Core.Attack import Attack


# The class to represent the Argumentation Framework no take parameter and is in association with Attack and Argument
class ArgFramework:
    # Constructor of the class
    def __init__(self):
        # set who represent all of arguments and attack
        self.__arguments = set()
        self.__attacks = set()

        self.__target = {}  # dict with Argument in key and in value the set of Argument who the first attack
        self.__attackedBy = {}  # dict with Argument in key and and in value the set of Argument who attack the first

        self.lastIndex = 1

    # getters
    def getArguments(self):
        return self.__arguments

    def getAttacks(self):
        return self.__attacks

    def getTarget(self):
        return self.__target

    def getAttackedBy(self):
        return self.__attackedBy

    def isInArguments(self, arg: Argument):
        return arg in self.getArguments()

    def isInAttacks(self, att: Attack):
        return att in self.getAttacks()

    def iterArgument(self):
        return iter(self.getArguments())

    def iterAttack(self):
        return iter(self.getAttacks)

    # Method to add a argument to the framework
    def addArgument(self, arg: Argument):
        if not isinstance(arg, Argument):
            raise TypeError("arg need to be a argument")
        if not self.isInArguments(arg):
            self.getArguments().add(arg)
            # update of two dict
            self.getTarget().setdefault(arg, set())
            self.getAttackedBy().setdefault(arg, set())
        else:
            print(f"{arg.getIndex()} is already in the framework")

    # Method to remove a argument to the framework
    def removeArgument(self, arg: Argument):
        if not isinstance(arg, Argument):
            raise TypeError("arg need to be a argument")
        if self.isInArguments(arg):
            # remove of the set
            self.getArguments().remove(arg)
            # Remove all attack if the arg is in
            to_remove = {
                att
                for att in self.iterAttack()
                if att.getFromArg() == arg or att.getToArg() == arg
            }
            for att in to_remove:
                self.removeAttack(att)
            # Update two dict
            for attacker in self.getTarget()[arg]:
                self.getAttackedBy()[attacker].discard(arg)
            for attacked in self.getAttackedBy()[arg]:
                self.getTarget()[attacked].discard(arg)
            # Delete key
            self.getTarget().pop(arg)
            self.getAttackedBy().pop(arg)

    # Method to add a attack to the framework
    def addAttack(self, att: Attack):
        if not isinstance(att, Attack):
            raise TypeError("att need to be a attack")
        # Verify if two arguments of the attack are in the framework
        if self.isInArguments(att.getFromArg()) and self.isInArguments(att.getToArg()):
            # Add the attack
            self.getAttacks().add(att)
            # Update the two dict with new attack
            self.getTarget()[att.getFromArg()].add(att.getToArg())
            self.getAttackedBy()[att.getToArg()].add(att.getFromArg())
        else:
            print("Missing 1 argument in the framework")

    # Method to remove a attack to the framework
    # Input: Attack
    def removeAttack(self, att: Attack):
        if not isinstance(att, Attack):
            raise TypeError("att need to be a attack")
        if self.isInAttacks(att):
            # Remove the attack
            self.getAttacks().remove(att)
            # Update the two dict
            self.getTarget()[att.getFromArg()].discard(att.getToArg())
            self.getAttackedBy()[att.getToArg()].discard(att.getFromArg())

    def __eq__(self, AF2):
        if isinstance(AF2, ArgFramework):
            return (
                self.getArguments() == AF2.getArguments()
                and self.getAttacks() == AF2.getAttacks()
            )
        return False
