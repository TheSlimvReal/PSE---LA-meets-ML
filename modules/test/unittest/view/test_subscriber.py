import pytest

from modules.exception.exceptions import NotImplementedException
from modules.view.subscriber import Subscriber


def test_subscriber_methods_throw_not_implemented_exception():
    with pytest.raises(NotImplementedException):
        Subscriber().update("Some string")
    with pytest.raises(NotImplementedException):
        Subscriber().finished()
