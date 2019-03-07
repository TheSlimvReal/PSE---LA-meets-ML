from modules.exception.exceptions import MyException
from modules.view.observable import Observable
from modules.view.output_service import OutputService


def test_abstract_output_service_can_be_used():
    output_service = OutputService()
    output_service.print_line("some string")
    output_service.print_stream("some string", Observable())
    output_service.print_error(MyException("Example Exception"))
