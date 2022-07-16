from typing import DefaultDict

import pytest


def two_sum(nums, target):
    nums_map = DefaultDict(lambda: [])
    for i in range(len(nums)):
        nums_map[nums[i]].append(i)
    nums.sort()

    left, right = 0, len(nums) - 1

    while left <= right:
        sum = nums[left] + nums[right]

        if sum > target:
            right -= 1
        elif sum == target:
            if len(nums_map[nums[left]]) > 1:
                return nums_map[nums[left]]
            return [nums_map[nums[left]][0], nums_map[nums[right]][0]]
        else:
            left += 1

    return []


def two_sum_table(nums, target):
    nums_map = {}
    for i in range(len(nums)):
        if (v := nums_map.get(target - nums[i])) is not None:
            return [v, i]
        nums_map[nums[i]] = i


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum([*nums], target) == expected
    assert two_sum_table([*nums], target) == expected
