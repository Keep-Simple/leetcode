import pytest


def longest_consecutive(nums):
    """
    Given an unsorted array of integers nums,
    return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
    """
    nums_set = set(nums)
    max_consecutive = 0

    while nums_set:
        num = nums_set.pop()
        count = 1
        queue = [num - 1, num + 1]
        while queue and nums_set:
            el = queue.pop()
            if el in nums_set:
                count += 1
                queue.extend([el - 1, el + 1])
                nums_set.remove(el)
        max_consecutive = max(max_consecutive, count)

    return max_consecutive


def longest_consecutive_2(nums):
    """
    https://leetcode.com/problems/longest-consecutive-sequence/solution/
    """
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        # ensure it's the beginning of the sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),  # 1,2,3,4
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ],
)
def test_longest_consecutive(nums, expected):
    assert longest_consecutive(nums) == expected
    assert longest_consecutive_2(nums) == expected
