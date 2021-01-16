def introsort(tab):
    maxdepth = (len(tab) - 1) * 2
    introsortHelper(tab, 0, len(tab), maxdepth)
    return tab

def introsortHelper(tab, start, end, maxdepth):
    if end - start <= 1:
        return
    elif maxdepth == 0:
        heapsort(tab, start, end)
    else:
        pivot = part(tab, start, end)
        introsortHelper(tab, start, pivot + 1, maxdepth - 1)
        introsortHelper(tab, pivot + 1, end, maxdepth - 1)


def part(tab, start, end):
    pivot = tab[start]
    i = start - 1
    j = end

    while True:
        i = i + 1
        while tab[i] < pivot:
            i = i + 1
        j = j - 1
        while tab[j] > pivot:
            j = j - 1

        if i >= j:
            return j

        tab[i], tab[j] = tab[j], tab[i]


def heapsort(tab, start, end):
    buildMaxHeap(tab, start, end)
    for i in range(end - 1, start, -1):
        tab[start], tab[i] = tab[i], tab[start]
        maxHeapify(tab, index=0, start=start, end=i)


def buildMaxHeap(tab, start, end):
    def parent(i):
        return (i - 1) // 2

    length = end - start
    index = parent(length - 1)
    while index >= 0:
        maxHeapify(tab, index, start, end)
        index = index - 1


def maxHeapify(tab, index, start, end):
    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and tab[start + l] > tab[start + index]):
        largest = l
    else:
        largest = index
    if (r < size and tab[start + r] > tab[start + largest]):
        largest = r
    if largest != index:
        tab[start + largest], tab[start + index] = tab[start + index], tab[start + largest]
        maxHeapify(tab, largest, start, end)