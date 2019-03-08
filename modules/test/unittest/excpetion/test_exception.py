import pytest

from modules.exception.exceptions import NotImplementedException, MyException


def test_my_exception_throws_error_when_used():
    with pytest.raises(NotImplementedException):
        MyException("").get_info()
