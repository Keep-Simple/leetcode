import pytest


def find_range(arr, key):
    """
    Given an array of numbers sorted in ascending order,
    find the range of a given number ‘key’.
    The range of the ‘key’ will be the first
    and last position of the ‘key’ in the array.

    Write a function to return the range of the ‘key’.
    If the ‘key’ is not present return [-1, -1].
    """
    if not arr or arr[-1] < key or arr[0] > key:
        return [-1, -1]

    # find upper range bound
    start, end = 0, len(arr) - 1
    has_key = False
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
            if arr[mid] == key:
                has_key = True

    if not has_key:
        return [-1, -1]

    range_end = start - 1
    # find lower range bound
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= key:
            end = mid - 1
        else:
            start = mid + 1

    return [start, range_end]


# suggested solution
def find_range2(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:  # no need to search, if 'key' is not present in the input array
        result[1] = binary_search(arr, key, True)
    return result


# modified Binary Search
def binary_search(arr, key, findMaxIndex):
    keyIndex = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            keyIndex = mid
            if findMaxIndex:
                start = mid + 1  # search ahead to find the last index of 'key'
            else:
                end = mid - 1  # search behind to find the first index of 'key'

    return keyIndex


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([4, 6, 6, 6, 9], 6, [1, 3]),
        ([1, 3, 8, 10, 15], 10, [3, 3]),
        ([1, 3, 8, 10, 15], 12, [-1, -1]),
    ],
)
def test_find_range(arr, key, expected):
    assert find_range(arr, key) == expected
    assert find_range2(arr, key) == expected
