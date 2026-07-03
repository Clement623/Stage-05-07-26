from .TransformationSpecialist import TransformationSpecialist



class AddAttackTransformationSpecialist(TransformationSpecialist):
    def __init__(self):
        super().__init__()
        self.__fromIndex = None
        self.__toIndex = None

        def process():
            pass
