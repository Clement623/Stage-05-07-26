from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
if TYPE_CHECKING:
    from Src.ExtFile.Extension import Extension

# Abstract class to define a Semantics
class Semantics(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def isExtension(self, af: ArgFramework, ext: Extension) -> bool:
        pass

    @abstractmethod
    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    @abstractmethod
    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    # Test if a extension is conflictFree
    def isConflictFree(self, af: ArgFramework, ext: Extension) -> bool:
        for arg in ext.iterExtArgument():
            for attacked in af.getTarget()[arg]:
                if ext.isInExtension(attacked):
                    return False
        return True

    # Test if a extension is defends
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
