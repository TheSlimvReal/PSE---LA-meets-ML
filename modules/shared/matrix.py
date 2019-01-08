from typing import List


##  This class represents a matrix holding its values and size
class Matrix:

    def __init__(self, values: List[List[float]]):
        self._values: List[List[float]] = values
        self._size: int = len(values)

    @property
    def values(self) -> List[List[float]]:
        return self._values

    @property
    def size(self) -> int:
        return self._size
