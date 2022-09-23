import math

import pytest


def find_min(nums):
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.

    For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements,
    return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.
    """
    n = len(nums)
    l, r = 0, n - 1
    ans = math.inf

    while l <= r:
        # if already sorted => return
        if nums[l] < nums[r]:
            return min(nums[l], ans)

        mid = (l + r) // 2
        # keep track of min so far
        ans = min(nums[mid], ans)
        is_left = nums[l] <= nums[mid]

        if is_left:
            l = mid + 1
        else:
            r = mid - 1

    return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([3, 1, 2], 1),
        ([4, 5, 1, 2, 3], 1),
    ],
)
def test_find_min(nums, expected):
    assert find_min(nums) == expected
