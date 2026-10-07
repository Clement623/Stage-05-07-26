import re
from Src.Core.ArgFramework import ArgFramework
from Src.Core.Argument import Argument
from Src.Core.Attack import Attack


# Class permettant de parser un fichier en un système d'argumentation
# if need to read a new extension file juste create the method and add the execution in method parse()
class Parser:
    # Input: file
    def __init__(self, file):
        self.__extension = re.search(r"\.(.+)$", file).group(
            1
        )  # Extract the extension of file, self.extension = string
        with open(file, "r", encoding="utf-8") as f:
            self.__content = f.read().split(
                "\n"
            )  # read the content and split by return of the line, self.content = list of string

    def getExtension(self) -> str:
        return self.__extension

    def getContent(self) -> str:
        return self.__content

    # Principal method use the method adapt to the good extension
    def parse(self) -> ArgFramework:
        framework = ArgFramework()
        # af file
        ext = self.getExtension()
        if ext == "af":
            self.parseAfFile(framework)
        # apx file
        elif ext == "apx":
            self.parseApxFile(framework)
        return framework

    # The parser for the af File, input: framework = ArgFramework object
    def parseAfFile(self, framework) -> None:
        # First part, the arguments: p as nb , the regex take off the nb to create arguments
        content = self.getContent()
        nb_argument = int(re.search(r"\D+(\d+)$", content[0]).group(1))
        for i in range(1, nb_argument + 1):
            framework.addArgument(Argument(i))
        # Second part, the attacks
        for attack in content[1:]:
            if attack and "#" != attack[0]:
                attack = (
                    attack.split()
                )  # attack is a string like nb nb so split by space
                from_arg = Argument(int(attack[0]))
                to_arg = Argument(int(attack[1]))
                framework.addAttack(Attack(from_arg, to_arg))
                # Add the attack in the framework

    # The parser for the apx File, input: framework = ArgFramework object
    def parseApxFile(self, framework) -> None:
        # process line by line
        content = self.getContent()
        for element in content:
            if element:
                # 2 regex to capture the part in arg(...) and att(...,...)
                arguments = re.findall(r"arg\(a(.+)\)", element)
                attacks = re.findall(r"att\(a(.+),a(.+)\)", element)
                if arguments:
                    # Add argument to the framework
                    framework.addArgument(Argument(int(arguments[0])))
                if attacks:
                    # Add attack
                    from_arg = Argument(int(attacks[0][0]))
                    to_arg = Argument(int(attacks[0][1]))
                    framework.addAttack(Attack(from_arg, to_arg))
