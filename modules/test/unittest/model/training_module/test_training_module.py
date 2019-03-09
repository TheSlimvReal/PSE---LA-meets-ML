from modules.model.training_module.training_module import TrainingModule
from mock import patch
import os

def parse(module, key):
    if key == "name": return "trained_net_"
    elif key == "path": return "data/LabeledMatrices/"
    elif key == "saving_path": return "data/TrainedNetwork"
    elif key == "train_split": return 0.8
    elif key == "num_conv_layers": return 1
    elif key == "num_dense_layers": return 3
    elif key == "layer_activation": return "relu"
    elif key == "final_activation": return "softmax"
    elif key == "dropout": return 0.1
    elif key == "batch_size": return 1
    elif key == "learning_rate": return 0.001
    elif key == "loss": return "categorical_crossentropy"
    elif key == "epochs": return 1


@patch("modules.shared.configurations.Configurations.get_config")
def test_training_createfile(mocked_config):
    mocked_config.side_effect = parse
    TrainingModule.train("modules/test/unittest/model/training_module/test.hdf5",
                         "", "", "modules/test/unittest/model/training_module/", 0.5)
    file_found = False
    for file in os.listdir("modules/test/unittest/model/training_module/"):
        if str(file)[:2] == "01" and str(file)[-4:] == "hdf5":
            file_found = True

    assert file_found









