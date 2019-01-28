from enum import Enum


class Module(Enum):
    UNDEFINED = "undefined"
    COLLECT = "collect"
    LABEL = "label"
    TRAIN = "train"
    CLASSIFY = "classify"
