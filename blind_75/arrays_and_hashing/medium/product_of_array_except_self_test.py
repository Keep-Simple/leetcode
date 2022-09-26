import pytest


def product_except_self(nums):
    """
    Given an integer array nums,
    return an array answer such that answer[i] is equal to the product
    of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
    Follow up: Can you solve the problem in O(1) extra space complexity?
    (The output array does not count as extra space for space complexity analysis.)

    Solution:
        Init ans array with 1.
        Make forward and backward iterations:
            - during forward ans[i] contains product of values to the left
            - during backward ans[i] gets multiplied by the product of values to the right
        Handle first and last element carefully
    """
    n = len(nums)
    ans = [1] * n

    prefix = nums[0]
    for i in range(1, n):
        ans[i] = prefix
        prefix *= nums[i]

    postfix = nums[-1]
    for i in range(n - 2, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]

    return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected
