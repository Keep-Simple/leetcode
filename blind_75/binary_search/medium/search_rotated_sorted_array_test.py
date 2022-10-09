import pytest


def search(nums, target):
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated
    at an unknown pivot index k (1 <= k < nums.length) such that the resulting
    array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Solution:
        After rotation - asc sorted array is split into left growing and right growing sides
        where each element in the left is bigger any in the right side

        We need to know in which side we are and then do the next binary step
        L, M, R - left, middle and right pointers
        We are in left side if nums[L] <= nums[M], else we are in rigth side
    """
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        is_left = nums[l] <= nums[mid]

        if is_left:
            # decrease mid
            if nums[mid] > target:
                if target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            # increase mid
            else:
                l = mid + 1
        else:
            # decrease mid
            if nums[mid] > target:
                r = mid - 1
            # increase mid
            else:
                if target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
    return -1


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([5, 1, 3], 3, 2),
    ],
)
def test_search(nums, target, expected):
    assert search(nums, target) == expected
