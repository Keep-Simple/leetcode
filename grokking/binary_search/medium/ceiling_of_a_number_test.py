import pytest


def search_celing_of_a_number(arr, key):
    """
    Given an array of numbers sorted in an ascending order,
    find the ceiling of a given number ‘key’.
    The ceiling of the ‘key’ will be the smallest element
    in the given array greater than or equal to the ‘key’.

    Write a function to return the index of the ceiling of the ‘key’.
    If there isn’t any ceiling return -1.
    """
    # if last element is smaller then key - return
    if not arr or arr[-1] < key:
        return -1

    start, end = 0, len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] > key:
            end = middle - 1
        elif arr[middle] < key:
            start = middle + 1
        else:
            return middle

    return start


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([4, 6, 10], 6, 1),
        ([1, 3, 8, 10, 15], 12, 4),
        ([4, 6, 10], 17, -1),
        ([4, 6, 10], -1, 0),
    ],
)
def test_search_celing_of_a_number(arr, key, expected):
    assert search_celing_of_a_number(arr, key) == expected
