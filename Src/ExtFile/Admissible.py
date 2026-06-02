from Src.ExtFile.Semantics import Semantics
from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument


class Admissible(Semantics):
    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    def isExtension(self, af: ArgFramework, ext: Extension) -> bool:

        if not isinstance(ext, Extension):
            raise TypeError("ext need to be an Extension")
        if not isinstance(af, ArgFramework):
            raise TypeError("af need to be an ArgFramework")

        if not self.isConflictFree(af, ext):
            return False
        return all(self.defends(af, ext, arg) for arg in ext.iterExtArgument())
