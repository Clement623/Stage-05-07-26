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

        self.__lastIndex = 1

    # getters
    def getArguments(self) -> set[Argument]:
        return self.__arguments

    def getAttacks(self) -> set[Attack]:
        return self.__attacks

    def getTarget(self) -> dict:
        return self.__target

    def getAttackedBy(self) -> dict:
        return self.__attackedBy

    def getNextAvailableIndex(self) -> int:
        if not self.__arguments:
            return 1
        return max(arg.getIndex() for arg in self.__arguments) + 1

    def isInArguments(self, arg: Argument) -> bool:
        return arg in self.getArguments()

    def isInAttacks(self, att: Attack) -> bool:
        return att in self.getAttacks()

    def iterArgument(self) -> iter:
        return iter(self.getArguments())

    def iterAttack(self) -> iter:
        return iter(self.getAttacks())

    # Method to add a argument to the framework
    def addArgument(self, arg: Argument) -> None:
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
    def removeArgument(self, arg: Argument) -> None:
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
            # Delete key
            self.getTarget().pop(arg, None)
            self.getAttackedBy().pop(arg, None)

    # Method to add a attack to the framework
    def addAttack(self, att: Attack) -> None:
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
    def removeAttack(self, att: Attack) -> None:
        if not isinstance(att, Attack):
            raise TypeError("att need to be a attack")
        if self.isInAttacks(att):
            # Remove the attack
            self.getAttacks().remove(att)
            # Update the two dict
            self.getTarget()[att.getFromArg()].discard(att.getToArg())
            self.getAttackedBy()[att.getToArg()].discard(att.getFromArg())

    def __eq__(self, AF2) -> bool:
        if isinstance(AF2, ArgFramework):
            return (
                self.getArguments() == AF2.getArguments()
                and self.getAttacks() == AF2.getAttacks()
            )
        return False
    
    def __repr__(self):
        args_str = ", ".join(str(arg) for arg in self.__arguments)
        attacks_str = ", ".join(str(att) for att in self.__attacks)
        return f"ArgFramework(Arguments: [{args_str}], Attacks: [{attacks_str}])"
