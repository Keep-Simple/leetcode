import pytest


def three_sum(nums):
    """
    Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    """
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n - 2):
        # remove duplicates, since if prev num is the same
        # we already calculated all the pairs for it
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        target_sum = -nums[i]

        while left < right:
            sum = nums[left] + nums[right]
            if sum < target_sum:
                left += 1
            elif sum > target_sum:
                right -= 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
                # remove duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        (
            [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0],
            [[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]],
        ),
    ],
)
def test_three_sum(nums, expected):
    assert three_sum(nums) == expected
