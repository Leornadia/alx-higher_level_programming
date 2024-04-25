def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a divide-and-conquer approach.
    A peak is an element that is greater than or equal to its neighbors.
    """
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = start + (end - start) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]
