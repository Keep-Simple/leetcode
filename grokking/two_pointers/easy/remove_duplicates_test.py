import pytest

"""
Given an array of sorted numbers,
remove all duplicate number instances from it in-place,
such that each element appears only once.
The relative order of the elements should be kept the same
and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array
and after moving return the length of the subarray that has no duplicate in it.
"""


# arr is sorted!
def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    for i in range(len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1

    return next_non_duplicate


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([2, 3, 3, 3, 6, 9, 9], 4),
        ([2, 2, 2, 11], 2),
    ],
)
def test(arr, expected):
    assert remove_duplicates(arr) == expected
