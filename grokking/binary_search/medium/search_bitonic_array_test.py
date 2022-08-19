import pytest


def search_bitonic_array(arr, key):
    """
    Given a Bitonic array, find if a given ‘key’ is present in it.
    An array is considered bitonic if it is monotonically
    increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any
    index i in the array arr[i] != arr[i+1].

    Write a function to return the index of the ‘key’.
    If the ‘key’ is not present, return -1.
    """
    max_el_idx = _find_max_element_idx_in_bitonic_array(arr)

    left_part = _binary_search(arr[: max_el_idx + 1], key)
    if left_part != -1:
        return left_part

    right_part = _binary_search(arr[max_el_idx + 1 :], key)
    if right_part != -1:
        return right_part + max_el_idx + 1

    return -1


def _binary_search(arr, key):
    if not arr:
        return -1

    is_asc = arr[0] < arr[-1]
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key ^ (not is_asc):
            end = mid - 1
        else:
            start = mid + 1

    return -1


def _find_max_element_idx_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1

    # find max element's idx
    while start < end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            # desc part
            end = mid
        else:
            # asc part
            start = mid + 1

    return start


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([1, 3, 8, 4, 3], 4, 3),
        ([3, 8, 3, 1], 8, 1),
        ([1, 3, 8, 12], 12, 3),
        ([10, 9, 8], 10, 0),
    ],
)
def test_search_bitonic_array(arr, key, expected):
    assert search_bitonic_array(arr, key) == expected
