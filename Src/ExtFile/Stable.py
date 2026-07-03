from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class Stable(Semantics):

    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        """Check if the argument is credulously accepted (not implemented)."""
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        """Check if the argument is skeptically accepted (not implemented)."""
        pass

    def isExtension(self, af: ArgFramework, ext: Extension) -> bool:
        """Check if an extension is stable."""
        if not isinstance(ext, Extension):
            raise TypeError("ext need to be an Extension")
        if not isinstance(af, ArgFramework):
            raise TypeError("af need to be an ArgFramework")

        # Must be conflict-free
        if not self.isConflictFree(af, ext):
            return False

        # Every argument outside the extension must be attacked by it
        for arg in af.getArguments():
            if not ext.isInExtension(arg):
                if not any(
                    ext.isInExtension(attacker) for attacker in af.getAttackedBy()[arg]
                ):
                    return False

        return True