def binarySearch(array, target):
    return binarySearchHelp(array, target, 0, len(array)-1)


def binarySearchHelp(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target > potential_match:
        return binarySearchHelp(array, target, middle+1, right)
    elif target < potential_match:
        return binarySearchHelp(array, target, left, middle-1)