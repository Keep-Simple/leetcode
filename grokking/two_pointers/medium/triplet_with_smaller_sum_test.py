import pytest


def triplet_with_smaller_sum(arr, target):
    """
    Given an array arr of unsorted numbers and a target sum,
    count all triplets in it such that arr[i] + arr[j] + arr[k] < target
    where i, j, and k are three different indices.
    Write a function to return the count of such triplets.
    """
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right] + arr[i]
            if sum >= target:
                right -= 1
            else:
                # since arr[right] >= arr[left], therefore,
                # we can replace arr[right] by any number between
                # left and right to get a sum less than the target sum
                count += right - left
                left += 1

    return count


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([-1, 0, 2, 3], 3, 2),
        ([-1, 4, 2, 1, 3], 5, 4),
    ],
)
def test(arr, target, expected):
    assert triplet_with_smaller_sum(arr, target) == expected
