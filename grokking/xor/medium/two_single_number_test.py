import pytest


def find_single_numbers(nums):
    """
    In a non-empty array of numbers,
    every number appears exactly twice except two
    numbers that appear only once.
    Find the two numbers that appear only once.
    """
    # xor all numbers
    n1xn2 = 0
    for i in range(len(nums)):
        n1xn2 ^= nums[i]

    # get rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1

    # parition 2 groups by rightmost_set_bit
    # 1 group will have num1, other num2
    num1, num2 = 0, 0
    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 4, 2, 1, 3, 5, 6, 2, 3, 5], [6, 4]),
        ([2, 1, 3, 2], [3, 1]),
    ],
)
def test_find_single_numbers(nums, expected):
    assert find_single_numbers(nums) == expected
