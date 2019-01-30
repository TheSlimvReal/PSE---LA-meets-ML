from modules.controller.commands.command import Command
from modules.controller.commands.key import Key
from modules.model.collector_module.ssget import SSGet


class SSGETCommand(Command):

    def __init__(self):
        super().__init__()
        self.valid_arguments = {
            ("u", "update"): Key.UPDATE
        }

    def execute(self) -> None:
        super().execute()
        SSGet.update_indices()
