from Src.Core.ArgFramework import ArgFramework
from Src.ExtFile.Extension import Extension
from Src.Core.Argument import Argument
from Src.ExtFile.Semantics import Semantics


class Preferred(Semantics):
    def isExtension(self, AF: ArgFramework, extension: Extension) -> bool:
        pass

    def isCredulouslyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass

    def isSkepticallyAccepted(self, AF: ArgFramework, arg: Argument) -> bool:
        pass
