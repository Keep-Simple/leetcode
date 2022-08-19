import math

import pytest


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    """
    Given an infinite sorted array (or an array with unknown size),
    find if a given number ‘key’ is present in the array.
    Write a function to return the index of the ‘key’
    if it is present in the array, otherwise return -1.

    Since it is not possible to define an array with infinite (unknown)
    size, you will be provided with an interface ArrayReader
    to read elements of the array. ArrayReader.get(index)
    will return the number at index; if the array’s size
    is smaller than the index, it will return Integer.MAX_VALUE.
    """
    # find bounds first, double it and move forward
    start, end = 0, 1
    while reader.get(end) < key:
        start, end = end + 1, end + (end - start + 1) * 2

    # perform binary search
    while start <= end:
        mid = (start + end) // 2
        if reader.get(mid) > key:
            end = mid - 1
        elif reader.get(mid) < key:
            start = mid + 1
        else:
            return mid

    return -1


@pytest.mark.parametrize(
    "reader, key, expected",
    [
        (
            ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),
            16,
            6,
        ),
        (
            ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),
            11,
            -1,
        ),
        (
            ArrayReader([1, 3, 8, 10, 15]),
            15,
            4,
        ),
        (
            ArrayReader([1, 3, 8, 10, 15]),
            200,
            -1,
        ),
    ],
)
def test_search_in_infinite_array(reader, key, expected):
    assert search_in_infinite_array(reader, key) == expected
