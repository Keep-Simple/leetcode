import pytest


def dutch_flag_sort(arr):
    """
    Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects, hence,
    we can’t count 0s, 1s, and 2s to recreate the array.

    The flag of the Netherlands consists of three colors: red, white and blue;
    and since our input array also consists of three different numbers
    that is why it is called Dutch National Flag problem.
    """

    def swap(j, k):
        arr[j], arr[k] = arr[k], arr[j]

    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        match arr[i]:
            case 0:
                # arr[low] can't be 2, because it was swapped on prev iterations
                # if arr[low] == 0, nothing changed
                # if arr[low] == 1, we don't need to swap
                swap(low, i)
                i += 1
                low += 1
            case 1:
                i += 1
            case 2:
                # after the swap arr[i] could be 0, 1 or 2
                swap(high, i)
                high -= 1


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
        ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
    ],
)
def test(arr, expected):
    dutch_flag_sort(arr)
    assert arr == expected
