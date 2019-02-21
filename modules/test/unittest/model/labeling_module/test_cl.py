from mock import patch
from modules.model.labeling_module import cl


@patch("modules.model.labeling_module.labeling_module.LabelingModule.start")
def test_cl(mock_labeling_module):
    def mocked_labeling_module_start(path: str, saving_name: str, saving_path: str):
        assert path == "testPath"
        assert saving_name == "testSavingName"
        assert saving_path == "testSavingPath"

    mock_labeling_module.side_effect = mocked_labeling_module_start
    cl.start("testPath", "testSavingName", "testSavingPath")


