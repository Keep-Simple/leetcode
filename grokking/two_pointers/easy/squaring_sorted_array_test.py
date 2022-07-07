import pytest

"""
Given a sorted array,
create a new array containing squares of all the numbers
of the input array in the sorted order.
"""


def make_squares(arr):
    n = len(arr)
    left, right = 0, n - 1
    res = [0] * n
    highest_square_idx = right

    while left <= right:
        l_square = arr[left] ** 2
        r_square = arr[right] ** 2

        if l_square > r_square:
            res[highest_square_idx] = l_square
            left += 1
        else:
            res[highest_square_idx] = r_square
            right -= 1

        highest_square_idx -= 1

    return res


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
        ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9]),
    ],
)
def test(arr, expected):
    assert make_squares(arr) == expected
