from array import array
def merge(left, right):
    # If one of the lists are empty we don t have to do anything, just return the other one
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = array("i")
    index_left = index_right = 0
    # Iterate over all of the elements from both lists. Compare each element from both lists one by one.
    # If one of them is greater we are putting this into result list, and move on in this list
    while True:
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        # If we don t have more elements to add in one of the lists, we have to add the rest of the other list to our
        # result list
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def mergesort(tab):
    if len(tab) < 2:
        return tab
    midpoint = len(tab) // 2
    left = mergesort(tab[:midpoint])
    right = mergesort(tab[midpoint:])
    return merge(left, right)
