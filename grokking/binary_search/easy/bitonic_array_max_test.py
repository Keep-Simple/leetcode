import pytest


def find_max_in_bitonic_array(arr):
    """
    Find the maximum value in a given Bitonic array.
    An array is considered bitonic if it is monotonically
    increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for
    any index i in the array arr[i] != arr[i+1].
    """
    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            # we are at the desc part, max is at left
            end = mid
        else:
            # we are at the asc part, max is at right
            start = mid + 1
    # at the end of the while loop, 'start == end'
    return arr[start]


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 3, 8, 12, 4, 2], 12),
        ([3, 8, 3, 1], 8),
        ([1, 3, 8, 12], 12),
        ([10, 9, 8], 10),
    ],
)
def test_find_max_in_bitonic_array(arr, expected):
    assert find_max_in_bitonic_array(arr) == expected
