from .Specialist import Specialist
from Src.Core.Argument import Argument
from Src.ExtFile.Extension import Extension


class BijectionSpecialist(Specialist):
    def __init__(self, mapping: dict, inverse: bool = False):
        super().__init__()
        if inverse:
            self.__mapping = {v: k for k, v in mapping.items()}
        else:
            self.__mapping = mapping
        self.__element=None

    def getElement(self):
        return self.__element

    def setElement(self, element):
        self.__element = element


    def getMapping(self) -> dict:
        return self.__mapping

    def setMapping(self, mapping: dict, inverse: bool = False):
        if inverse:
            self.__mapping = {v: k for k, v in mapping.items()}
        else:
            self.__mapping = mapping

    def apply_to_argument(self, arg: Argument) -> Argument:
        target_index = self.getMapping().get(arg.getIndex())
        if target_index is not None:
            return Argument(target_index)
        return None

    def apply_to_extension(self, extension: Extension) -> Extension:
        translated_args = set()
        for arg in extension.iterExtArgument():
            translated_arg = self.apply_to_argument(arg)
            if translated_arg is not None:
                translated_args.add(translated_arg)

        return Extension(translated_args, semantics=extension.getSemantics())

    def process(self):
        element = self.getElement()
        if isinstance(element, Argument):
            return self.apply_to_argument(element)
        elif isinstance(element, Extension):
            return self.apply_to_extension(element)
        elif isinstance(element, set):
            translated_set = set()
            for item in element:
                self.setElement(item)
                translated_set.add(self.process())
            return translated_set
        else:
            raise TypeError("Type non supporting by the bijection specialist")
