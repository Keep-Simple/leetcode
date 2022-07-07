import pytest


def search_triplets(arr):
    """
    Given an array of unsorted numbers,
    find all unique triplets in it that add up to zero.
    """
    arr.sort()
    triplets = []

    for i, a in enumerate(arr):
        if i > 0 and a == arr[i - 1]:
            continue
        search_pair(arr, i + 1, -a, triplets)
    return triplets


def search_pair(arr, left, target_sum, triplets):
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            # skip same element to avoid duplicate triplets
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif sum > target_sum:
            right -= 1
        else:
            left += 1


@pytest.mark.parametrize(
    "arr,expected",
    [
        (
            [-3, 0, 1, 2, -1, 1, -2],
            [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]],
        ),
        ([-5, 2, -1, -2, 3], [[-5, 2, 3], [-2, -1, 3]]),
    ],
)
def test(arr, expected):
    assert search_triplets(arr) == expected
