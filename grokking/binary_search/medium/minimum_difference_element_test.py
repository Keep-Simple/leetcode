import pytest


def search_min_diff_element(arr, key):
    """
    Given an array of numbers sorted in ascending order,
    find the element in the array that
    has the minimum difference with the given ‘key’.
    """
    if key < arr[0]:
        return arr[0]
    # to prevent index out of bounds exception and improve perfomance
    if key > arr[-1]:
        return arr[-1]

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return key

    # at the end of the while loop, 'start == end+1'
    # we are not able to find the element in the given array
    # return the element which is closest to the 'key'
    # arr[start] is bigger than key and arr[end] is smaller
    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([4, 6, 10], 7, 6),
        ([4, 6, 10], 4, 4),
        ([1, 3, 8, 10, 15], 12, 10),
        ([4, 6, 10], 17, 10),
    ],
)
def test_search_min_diff_element(arr, key, expected):
    assert search_min_diff_element(arr, key) == expected
