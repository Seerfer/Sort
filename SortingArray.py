import random
import sorts
from Errors import Error
from array import array


class SortingArray:

    def __init__(self, n):
        self.tab = array("i")
        self.fill(n)

    def fill(self, n):
        if n < 1 or n > 5000000:
            raise Error("Number of elements should be between 1 and 5000000")
        for i in range(0, n):
            self.tab.append(random.randint(0, 10000))

    def __str__(self):
        return "Array values: " + str(self.tab)

    def quicksort(self):
        self.tab = sorts.quicksort(self.tab)

    def mergesort(self):
        self.tab = sorts.mergesort(self.tab)

    def introsort(self):
        self.tab = sorts.introsort(self.tab)

    def bubblesort(self):
        self.tab = sorts.bubblesort(self.tab)

    @property
    def list(self):
        return self.tab

    def partsort(self, n):
        if n > 1:
            raise Error("Value should be equal or less than 1")

        list = self.tab.tolist()
        tmp = list[0:round(len(self.tab) * n)]
        tmp.sort()
        list[0:round(len(self.tab) * n)] = tmp
        self.tab = array("i", list)

    def reversesort(self):
        self.tab = sorts.quicksort(self.tab)
        self.tab.reverse()

    def reset(self):
        self.tab = []
