import pytest


def search_quadruplets(arr, target):
    """
    Given an array of unsorted numbers and a target number,
    find all unique quadruplets in it, whose sum is equal to the target number.
    """
    quadruplets = []
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 3):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            left, right = j + 1, len(arr) - 1

            while left < right:
                sum = arr[i] + arr[j] + arr[left] + arr[right]

                if sum < target:
                    left += 1
                elif sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left - 1] == arr[left]:
                        left += 1
                    while left < right and arr[right + 1] == arr[right]:
                        right -= 1
                else:
                    right -= 1
    return quadruplets


@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
        ([2, 0, -1, 1, -2, 2], 2, [[-2, 0, 2, 2], [-1, 0, 1, 2]]),
    ],
)
def test(arr, target, expected):
    assert search_quadruplets(arr, target) == expected
