from SortingArray import SortingArray
from Errors import Error
import datetime


def _partsort(n, arrays):
    for array in arrays:
        array.partsort(n)
    return arrays


def _reversesort(arrays):
    for array in arrays:
        array.reversesort()
        return arrays


def _prepare_arrays(arrays_number, length_of_array, partsortvalue=0, reverse=False):
    arrays = []

    for _ in range(arrays_number):
        array = SortingArray(length_of_array)
        arrays.append(array)

    _partsort(partsortvalue, arrays)

    if reverse is True:
        _reversesort(arrays)

    return arrays


def test(arrays_number, length_of_array, algorithm_name, partsortvalue=0, reverse=False):
    if type(algorithm_name) is not str:
        raise Error("Algorithm value must be a string")

    if algorithm_name not in ["quicksort", "introsort", "bubblesort", "mergesort"]:
        raise Error("Wrong algoritm value")

    arrays = _prepare_arrays(arrays_number, length_of_array, partsortvalue, reverse)
    algoritmh = getattr(SortingArray, algorithm_name)

    start = datetime.datetime.now()
    for array in arrays:
        algoritmh(array)
    end = datetime.datetime.now()

    return (end - start).microseconds
