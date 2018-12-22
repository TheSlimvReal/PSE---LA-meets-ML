from modules.controller.commands.command import Command


class QuitCommand(Command):
    def execute(self):
        super().execute()

    def validate(self) -> bool:
        return super().validate()
