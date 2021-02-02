def bubblesort(tab):
    n = len(tab)
    for i in range(n):
        is_sorted = True
        # Start looking at each elements one by one and then compare them with next elements
        # At the end if we had to swap at least one pair, we can t be sure is list sorted or not
        # so we have to iterate over out list again
        for j in range(n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
                is_sorted = False
        if is_sorted:
            return tab
