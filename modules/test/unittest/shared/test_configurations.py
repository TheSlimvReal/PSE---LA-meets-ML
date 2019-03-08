import json

from pytest import fixture

from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.shared.configurations import Configurations


##  Runs before each test to setup config file
@fixture(autouse=True)
def setup():
    Configurations.load_config_file()


def test_loading_config_values_works():
    actual = Configurations.get_config_with_key(Module.LABEL, Key.SAVING_PATH)
    with open("config.json") as f:
        data = json.load(f)
    expected = data["label"]["saving_path"]
    assert actual == expected


def test_loading_config_has_right_value():
    actual = Configurations.get_config(Module.TRAIN, "learning_rate")
    expected = 0.001
    assert actual == expected


def test_load_not_existing_key_returns_null():
    actual = Configurations.get_config_with_key(Module.TRAIN, Key.SIZE)
    assert actual is None
