import pytest


def binary_search(arr, key):
    """
    Given a sorted array of numbers,
    find if a given number ‘key’ is present in the array.
    Though we know that the array is sorted,
    we don’t know if it’s sorted in ascending or descending order.
    You should assume that the array can have duplicates.

    Write a function to return the index of the ‘key’
    if it is present in the array, otherwise return -1.
    """
    if not arr:
        return -1

    is_asc = arr[0] < arr[-1]

    start, end = 0, len(arr) - 1

    while start <= end:
        # can be (end+start) / 2
        # but in other languages that can cause number overflow
        middle = start + (end - start) // 2
        if start > end:
            return -1
        if arr[middle] == key:
            return middle
        if (arr[middle] > key) ^ (not is_asc):
            end = middle - 1
        else:
            start = middle + 1

    return -1


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([4, 6, 10], 10, 2),
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([10, 6, 4], 10, 0),
        ([10, 6, 4], 4, 2),
    ],
)
def test_binary_search(arr, key, expected):
    assert binary_search(arr, key) == expected
