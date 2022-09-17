import pytest


def cyclic_sort(nums):
    """
    Write a function to sort the objects in-place on their creation
    sequence number (from 1 to n) in O(n) and without using any extra space

    Solution:
        As we know, the input array contains numbers from the range 1 to n.
        We can use this fact to devise an efficient way to sort the numbers.
        Since all numbers are unique, we can try placing each number at its correct place, i.e., placing 1 at index ‘0’, placing 2 at index ‘1’, and so on.

        To place a number (or an object in general) at its correct index, we first need to find that number.
        If we first find a number and then place it at its correct place, it will take us O(N^2), which is not acceptable.

        Instead, what if we iterate the array one number at a time, and if the current number we are iterating is not at the correct index,
        we swap it with the number at its correct index. This way, we will go through all numbers and place them at their correct indices,
        hence, sorting the whole array.

    TC:
        The time complexity of the above algorithm is O(n)
        Although we are not incrementing the index i when swapping the numbers,
        this will result in more than n iterations of the loop, but in the worst-case scenario,
        the while loop will swap a total of n-1 numbers, and once a number is at its correct index,
        we will move on to the next number by incrementing i. So overall, our algorithm will take O(n) + O(n-1)
        which is asymptotically equivalent to O(n)
    SC:
        O(1)
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 5, 4, 2], [1, 2, 3, 4, 5]),
        ([2, 6, 4, 3, 1, 5], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 6, 4, 3, 2], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_cyclic_sort(nums, expected):
    assert cyclic_sort(nums) == expected
