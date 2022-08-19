import pytest


def find_single_number(arr):
    """
    In a non-empty array of integers,
    every number appears twice except for one,
    find that single number.
    """
    x = 0
    for i in range(len(arr)):
        x ^= arr[i]
    return x


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 4, 2, 1, 3, 2, 3], 4),
        ([7, 9, 7], 9),
    ],
)
def test_find_single_number(arr, expected):
    assert find_single_number(arr) == expected
