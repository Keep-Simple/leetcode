import math

import pytest


def triplet_sum_close_to_target(arr, target_sum):
    """
    Given an array of unsorted numbers and a target number,
    find a triplet in the array whose sum is as close
    to the target number as possible,
    return the sum of the triplet. If there are more than one such triplet,
    return the sum of the triplet with the smallest sum.
    """
    arr.sort()
    smallest_diff = math.inf

    for i, a in enumerate(arr):
        if i > 0 and a == arr[i - 1]:
            continue
        res = search_pair(arr, i + 1, target_sum - a)
        if not res:
            continue
        diff = target_sum - (res + a)
        if abs(smallest_diff) > abs(diff):
            smallest_diff = diff
        elif abs(smallest_diff) == abs(diff):
            smallest_diff = max(smallest_diff, diff)

    return target_sum - smallest_diff


def search_pair(arr, left, target_sum):
    right = len(arr) - 1

    sum = None

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            break
        elif sum > target_sum:
            right -= 1
        else:
            left += 1

    return sum


@pytest.mark.parametrize(
    "arr,target_sum,expected",
    [
        ([-2, 0, 1, 2], 2, 1),
        ([-3, -1, 1, 2], 1, 0),
        ([1, 0, 1, 1], 100, 3),
    ],
)
def test(arr, target_sum, expected):
    assert triplet_sum_close_to_target(arr, target_sum) == expected
