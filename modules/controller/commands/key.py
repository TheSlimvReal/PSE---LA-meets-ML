from enum import Enum


##  enum that represents the possible keys a user can enter
#
#   @extends Enum to get the enum logic
class Key(Enum):
    QUIT = 0
    AMOUNT = 1
    NAME = 2
    SIZE = 3
    PATH = 4
    GENERATE = 5
    SAVING_PATH = 6
    TRAIN = 7
    NETWORK = 8
    SOLVE = 9
    HELP = 10
    UPDATE = 11
