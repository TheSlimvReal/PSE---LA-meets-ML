from modules.model.training_module.training_module import TrainingModule
from mock import patch
import os
import pytest
from modules.exception.exceptions import IOException

class TestTrainingModule:
    name: str
    path: str
    saving_path: str
    train_split: float
    num_conv_layers: int
    num_dense_layers: int
    layer_activation: str
    final_activation: str
    dropout: float
    batch_size: int
    learning_rate: float
    loss: str
    epochs: int

    @staticmethod
    @pytest.fixture(autouse=True)
    def run_around_tests():
        TestTrainingModule.name = "trained_net_"
        TestTrainingModule.path = "data/LabeledMatrices/"
        TestTrainingModule.saving_path = "data/TrainedNetwork"
        TestTrainingModule.train_split = 0.8
        TestTrainingModule.num_conv_layers = 1
        TestTrainingModule.num_dense_layers = 3
        TestTrainingModule.layer_activation = "relu"
        TestTrainingModule.final_activation = "softmax"
        TestTrainingModule.dropout = 0.1
        TestTrainingModule.batch_size = 1
        TestTrainingModule.learning_rate = 0.001
        TestTrainingModule.loss = "categorical_crossentropy"
        TestTrainingModule.epochs = 1

    @staticmethod
    def parse(module, key):
        if key == "name": return TestTrainingModule.name
        elif key == "path": return TestTrainingModule.path
        elif key == "saving_path": return TestTrainingModule.saving_path
        elif key == "train_split": return TestTrainingModule.train_split
        elif key == "num_conv_layers": return TestTrainingModule.num_conv_layers
        elif key == "num_dense_layers": return TestTrainingModule.num_dense_layers
        elif key == "layer_activation": return TestTrainingModule.layer_activation
        elif key == "final_activation": return TestTrainingModule.final_activation
        elif key == "dropout": return TestTrainingModule.dropout
        elif key == "batch_size": return TestTrainingModule.batch_size
        elif key == "learning_rate": return TestTrainingModule.learning_rate
        elif key == "loss": return TestTrainingModule.loss
        elif key == "epochs": return TestTrainingModule.epochs

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_createfile(mocked_config):
        mocked_config.side_effect = TestTrainingModule.parse
        TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                             "", "", "modules/test/unittest/model/training_module/", 0.5)
        file_found = False
        for file in os.listdir("modules/test/unittest/model/training_module/"):
            if str(file)[:2] == "01" and str(file)[-4:] == "hdf5":
                file_found = True

        assert file_found

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_zerodense(mocked_config):
        TestTrainingModule.num_dense_layers = 0
        mocked_config.side_effect = TestTrainingModule.parse
        TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                             "", "", "modules/test/unittest/model/training_module/", 0.5)

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_zeroconv(mocked_config):
        TestTrainingModule.num_conv_layers = 0
        mocked_config.side_effect = TestTrainingModule.parse

        with pytest.raises(RuntimeError):
            TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                                 "", "", "modules/test/unittest/model/training_module/", 0.5)

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_zerobatch(mocked_config):
        TestTrainingModule.batch_size = 0
        mocked_config.side_effect = TestTrainingModule.parse
        with pytest.raises(ZeroDivisionError):
            TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                                 "", "", "modules/test/unittest/model/training_module/", 0.5)

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_loadednetwork(mocked_config):
        mocked_config.side_effect = TestTrainingModule.parse
        TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                             "modules/test/unittest/model/training_module/testnetwork.hdf5",
                             "name", "modules/test/unittest/model/training_module/", 0.5)

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_no_valid_dataset(mocked_config):
        mocked_config.side_effect = TestTrainingModule.parse
        TrainingModule.train("modules/test/unittest/model/training_module/notvalid.hdf5",
                             "", "", "modules/test/unittest/model/training_module/", 0.5)

    @staticmethod
    @patch("modules.shared.configurations.Configurations.get_config")
    def test_training_moreconv(mocked_config):
        mocked_config.side_effect = TestTrainingModule.parse
        TestTrainingModule.num_conv_layers = 2
        TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                             "", "", "modules/test/unittest/model/training_module/", 0.5)

