import random
from sorts import *
from Errors import Error

class Table:
    def __init__(self):
        self.tab = []

    def fill(self, n):
        for i in range(0, n):
            self.tab.append(random.randint(0, 10000))

    def __str__(self):
        return "Table values: " + str(self.tab)

    def quicksort(self):
        self.tab = quicksort.quicksort(self.tab)

    def mergesort(self):
        self.tab = mergesort.mergesort(self.tab)

    def introsort(self):
        self.tab = introsort.introsort(self.tab)

    def bubblesort(self):
        self.tab = mergesort.mergesort(self.tab)

    def list(self):
        return self.tab

    def partsort(self, n):
        if n > 1:
            raise Error("Value should be equal or less than 1")
        tmp = self.tab[0:round(len(self.tab)*n)]
        tmp.sort()
        self.tab[0:round(len(self.tab) * n)] = tmp