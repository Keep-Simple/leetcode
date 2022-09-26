import pytest

"""
In problems where we deal with sorted arrays (or LinkedLists)
and need to find a set of elements that fulfill certain constraints,
the Two Pointers approach becomes quite useful.
The set of elements could be a pair, a triplet or even a subarray.
For example, take a look at the following problem:

Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.

Given that the input array is sorted,
an efficient way would be to start with one pointer in the beginning
and another pointer at the end.
At every step, we will see if the numbers pointed by the two pointers
add up to the target sum. If they do not, we will do one of two things:

- If the sum of the two numbers pointed by the two pointers is greater
    than the target sum, this means that we need a pair with a smaller sum.
    So, to try more pairs, we can decrement the end-pointer.
- If the sum of the two numbers pointed by the two pointers is smaller
    than the target sum, this means that we need a pair with a larger sum.
    So, to try more pairs, we can increment the start-pointer.
"""


# arr is sorted!
def pair_with_targetsum(arr, target_sum):
    left_pointer, right_pointer = 0, len(arr) - 1

    while left_pointer <= right_pointer:
        sum = arr[left_pointer] + arr[right_pointer]
        if sum == target_sum:
            return [left_pointer, right_pointer]
        if sum > target_sum:
            right_pointer -= 1  # lower sum
        else:
            left_pointer += 1  # increase sum

    return None


@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([1, 2, 3, 4, 6], 6, [1, 3]),
        ([2, 5, 9, 11], 11, [0, 2]),
    ],
)
def test(arr, target, expected):
    assert pair_with_targetsum(arr, target) == expected
