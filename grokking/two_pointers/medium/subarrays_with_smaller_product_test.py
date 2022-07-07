from collections import deque

import pytest


def find_subarrays(arr, target):
    """
    Given an array with positive numbers and a positive target number,
    find all of its contiguous subarrays
    whose product is less than the target number.
    """
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left <= right:
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))

    return result


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([2, 5, 3, 10], 30, [[2], [5], [2, 5], [3], [5, 3], [10]]),
        ([8, 2, 6, 5], 50, [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]),
    ],
)
def test(arr, target, expected):
    assert find_subarrays(arr, target) == expected
