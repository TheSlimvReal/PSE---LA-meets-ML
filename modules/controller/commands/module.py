from enum import Enum


##  enum that represents all possible modules
#
#   @extends Enum to get enum logic
class Module(Enum):
    UNDEFINED = "undefined"
    COLLECT = "collect"
    LABEL = "label"
    TRAIN = "train"
    CLASSIFY = "classify"
