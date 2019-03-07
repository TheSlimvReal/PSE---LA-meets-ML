import pytest
from mock import patch

from modules.exception.exceptions import InvalidOSException
from modules.model.labeling_module import cl


@patch('os.system')
def test_cl(mock_os):

    cl.start("testPath", "testSavingName", "testSavingPath")
    mock_os.assert_called_with("python3.6 modules/model/labeling_module/labeling_module.py "
                               "testPath testSavingName testSavingPath")


@patch("sys.platform", "not_linux")
def test_cl_with_wrong_os_raises_exception():
    with pytest.raises(InvalidOSException):
        cl.start("", "", "")


@patch("sys.platform", "linux")
@patch("os.system")
def test_cl_with_linux_platform_works(mocked_sys):
    cl.start("", "", "")
    mocked_sys.assert_called_once()
