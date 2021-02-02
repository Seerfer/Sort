from test.set_conditions import partsort, number_of_arrays, array_length, reverse, algorithms
from test.test import test


def set_tests():
    for n in array_length:
        for algorithm in algorithms:
            if reverse is True:
                result = test(number_of_arrays, n, algorithm, reverse=True)
                print(result)
            for part in partsort:
                result = test(number_of_arrays, n, algorithm, partsortvalue=part)
                print(result)
