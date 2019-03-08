import pytest
from mock import patch, call

from modules.exception.exceptions import InvalidOSException
from modules.model.collector_module.collector import Collector


@patch("modules.shared.saver.Saver.save")
def test_saver_has_calls(mocked_saver):
    Collector.collect(5, 128, "name", " path")
    mocked_saver.assert_called_once()


@patch("sys.platform", "not_linux")
def test_collector_raises_exception_when_not_on_linux():
    with pytest.raises(InvalidOSException):
        Collector.collect(0, 0, "", "")
