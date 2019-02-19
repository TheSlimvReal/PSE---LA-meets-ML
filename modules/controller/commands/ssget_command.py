from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.model.collector_module.ssget import SSGet


##  command to interact with the ssget tool
#
#   this command will be created when entering ssget in the terminal
#   @extends Command to use its parsing logic
class SSGETCommand(Command):

    def __init__(self):
        super().__init__()
        self.valid_arguments = {
            ("u", "update"): Key.UPDATE
        }

    def execute(self) -> None:
        super().execute()
        if Key.UPDATE in self.arguments:
            SSGet.new_search()
