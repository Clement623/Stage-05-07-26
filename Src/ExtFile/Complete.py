from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class Complete(Semantics):
    def isExtension(self, af: ArgFramework, ext: Extension):

        if not isinstance(ext, Extension):
            raise TypeError("ext need to be an Extension")
        if not isinstance(af, ArgFramework):
            raise TypeError("af need to be an ArgFramework")

        if not self.isConflictFree(af, ext):
            return False
        if not all(self.defends(af, ext, arg) for arg in ext.iterExtArgument()):
            return False

        for arg in af.getArguments():
            if not ext.isInExtension(arg):
                if self.defends(af, ext, arg):
                    return False
        return True

    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass
