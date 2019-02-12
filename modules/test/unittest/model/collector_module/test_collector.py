from mock import patch, call

from modules.model.collector_module.collector import Collector


@patch("modules.shared.saver.Saver.save")
def test_saver_has_calls(mocked_saver):
    Collector.collect(5, 128, "name"," path")
    mocked_saver.assert_called_once()
