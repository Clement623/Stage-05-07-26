from Src.ExtFile.Semantics import Semantics
from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument


class Admissible(Semantics):

    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        """Check if the argument is credulously accepted (not implemented)."""
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        """Check if the argument is skeptically accepted (not implemented)."""
        pass

    def isExtension(self, af: ArgFramework, ext: Extension) -> bool:
        """Check if an extension is admissible."""

        if not isinstance(ext, Extension):
            raise TypeError("ext need to be an Extension")
        if not isinstance(af, ArgFramework):
            raise TypeError("af need to be an ArgFramework")

        # An admissible extension must be conflict-free
        if not self.isConflictFree(af, ext):
            return False

        # And every argument in the extension must be defended by it
        return all(self.defends(af, ext, arg) for arg in ext.iterExtArgument())