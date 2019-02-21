from mock import patch
from modules.model.labeling_module import cl


@patch('os.system')
def test_cl(mock_os):

    cl.start("testPath", "testSavingName", "testSavingPath")
    mock_os.assert_called_with("python3.6 modules/model/labeling_module/labeling_module.py "
                               "testPath testSavingName testSavingPath")

