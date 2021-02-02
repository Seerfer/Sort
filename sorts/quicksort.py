from array import array
def quicksort(tab):
    # stops the recursive function if the array contains fewer than two elements.
    if len(tab) < 2:
        return tab
    # Selecting pivot and creating lists to sorts table items to them
    pivot_index = len(tab) // 2
    pivot_value = tab[pivot_index]
    lower, higher, same = array("i"), array("i"), array("i")
    # Comparing elements and moving them into sorting them into special list
    for number in tab:
        if number < pivot_value:
            lower.append(number)
        elif number == pivot_value:
            same.append(number)
        elif number > pivot_value:
            higher.append(number)
    return quicksort(lower) + same + quicksort(higher)