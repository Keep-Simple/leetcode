import pytest


def search_rotated_array(arr, key):
    """
    Given an array of numbers
    which is sorted in ascending order
    and also rotated by some arbitrary number,
    find if a given ‘key’ is present in it.

    Write a function to return the index of the ‘key’ in the rotated array.
    If the ‘key’ is not present, return -1.
    You can assume that the given array does not have any duplicates.
    """
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (end + start) // 2

        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:
            # start -> mid are in asc order
            if not (arr[start] <= key < arr[mid]):
                start = mid + 1
            else:
                end = mid - 1
        else:
            # mid + 1 -> end are in asc order
            if not (arr[mid + 1] < key <= arr[end]):
                end = mid - 1
            else:
                start = mid + 1

    return -1


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([10, 15, 1, 3, 8], 15, 1),
        ([4, 5, 7, 9, 10, -1, 2], 10, 4),
    ],
)
def test_search_rotated_array(arr, key, expected):
    assert search_rotated_array(arr, key) == expected
