from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class Grounded(Semantics):
    def isExtension(self, af: ArgFramework, extension: Extension) -> bool:
        pass

    def isCredulouslyAccepted(self, af: ArgFramework, arg: Argument) -> bool:
        pass

    def isSkepticallyAccepted(self, af: ArgFramework, arg: Argument) -> bool:
        pass
