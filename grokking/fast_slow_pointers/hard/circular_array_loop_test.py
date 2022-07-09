import pytest


def circular_array_loop_exists(arr):
    """
    We are given an array containing positive and negative numbers.
    Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices
    and if ‘M’ is negative move backwards ‘M’ indices.
    You should assume that the array is circular which means two things:

    - If, while moving forward, we reach the end of the array,
    we will jump to the first element to continue the movement.

    - If, while moving backward, we reach the beginning of the array,
    we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle.
    The cycle should have more than one element and should follow one direction
    which means the cycle should not contain forward and backward movements.


    solution can be improved timewise by tracking visited nodes,
    but space complexity will grow from O(1) to O(N)
    """
    for i in range(len(arr)):
        is_prev_n_positive = arr[i] >= 0
        slow = fast = i
        while True:
            fast, is_n_positive1 = get_circular_idx(arr, fast)
            fast2, is_n_positive2 = get_circular_idx(arr, fast)
            if (
                is_prev_n_positive != is_n_positive1
                or is_n_positive1 != is_n_positive2
                or fast == fast2
            ):
                break
            fast = fast2
            slow = get_circular_idx(arr, slow)[0]
            if fast == slow:
                return True

    return False


def get_circular_idx(arr, idx):
    n = arr[idx]
    return (idx + n) % len(arr), n > 0


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, -1, 2, 2], True),
        ([2, 2, -1, 2], True),
        ([2, 1, -1, -2], False),
        ([2, 1, -1, -2], False),
        ([], False),
        ([1], False),
    ],
)
def test(arr, expected):
    assert circular_array_loop_exists(arr) == expected
