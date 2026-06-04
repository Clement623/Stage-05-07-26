from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class Stable(Semantics):
    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass
    #Test if a extension is stable
    def isExtension(self, af: ArgFramework, ext: Extension) -> bool:
        if not isinstance(ext, Extension):
            raise TypeError("ext need to be an Extension")
        if not isinstance(af, ArgFramework):
            raise TypeError("af need to be an ArgFramework")

        if not self.isConflictFree(af, ext):
            return False
        for arg in af.getArguments():
            if not ext.isInExtension(arg):
                if not any(
                    ext.isInExtension(attacker) for attacker in af.getAttackedBy()[arg]
                ):
                    return False
        return True
