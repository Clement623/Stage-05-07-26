from abc import ABC, abstractmethod
from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument

#Abstract class to define a Semantics
class Semantics(ABC):
    @abstractmethod
    def isExtension(self) -> bool:
        pass

    @abstractmethod
    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    @abstractmethod
    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass
    #Test if a extension is conflictFree
    def isConflictFree(self, af: ArgFramework, ext: Extension) -> bool:
        for arg in ext.iterExtArgument():
            for attacked in af.getTarget()[arg]:
                if ext.isInExtension(attacked):
                    return False
        return True

    #Test if a extension is defends
    def defends(self, af: ArgFramework, ext: Extension, arg: Argument) -> bool:
        for attacker in af.getAttackedBy()[arg]:
            if not any(
                ext.isInExtension(counter) for counter in af.getAttackedBy()[attacker]
            ):
                return False
        return True

    def __eq__(self, other):
        if type(self) is type(other):
            return True
        return False
