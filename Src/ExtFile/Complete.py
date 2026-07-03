from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class Complete(Semantics):

    def isExtension(self, af: ArgFramework, ext: Extension) -> bool:
        """Check if an extension is complete."""

        if not isinstance(ext, Extension):
            raise TypeError("ext need to be an Extension")
        if not isinstance(af, ArgFramework):
            raise TypeError("af need to be an ArgFramework")

        # Must be conflict-free
        if not self.isConflictFree(af, ext):
            return False

        # Must defend all its own arguments
        if not all(self.defends(af, ext, arg) for arg in ext.iterExtArgument()):
            return False

        # Must contain every argument it defends (no missing defended argument)
        for arg in af.getArguments():
            if not ext.isInExtension(arg):
                if self.defends(af, ext, arg):
                    return False

        return True

    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        """Check if the argument is credulously accepted (not implemented)."""
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        """Check if the argument is skeptically accepted (not implemented)."""
        pass