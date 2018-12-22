from typing import List
from modules.controller.commands.key import Key


##  Interface for the module specific commands
class Command:

    arguments: List[Key]

    ##  can be called the execute the module
    def execute(self):
        pass

    ##  will be called in the command construction
    def validate(self) -> bool:
        pass
