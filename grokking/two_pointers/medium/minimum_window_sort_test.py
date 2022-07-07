import math

import pytest


def shortest_window_sort(arr):
    """
    Given an array,
    find the length of the smallest subarray in it
    which when sorted will sort the whole array.
    """
    left, right = 0, len(arr) - 1

    while left <= right and right > 0 and left < len(arr) - 1:
        if arr[left + 1] >= arr[left]:
            left += 1
        elif arr[right - 1] <= arr[right]:
            right -= 1
        else:
            break

    if left == right:
        return 0

    subarr_max = -math.inf
    subarr_min = math.inf

    for i in range(left, right + 1):
        subarr_max = max(subarr_max, arr[i])
        subarr_min = min(subarr_min, arr[i])

    while left > 0 and arr[left - 1] > subarr_min:
        left -= 1

    while right < len(arr) - 1 and arr[right + 1] < subarr_max:
        right += 1

    return right - left + 1


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 5, 3, 7, 10, 9, 12], 5),
        ([1, 3, 2, 0, -1, 7, 10], 5),
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
    ],
)
def test(arr, expected):
    assert shortest_window_sort(arr) == expected
