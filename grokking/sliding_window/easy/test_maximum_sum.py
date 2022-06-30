import pytest
from maximum_sum import max_sub_array_of_size_k


@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([2, 3, 4, 1, 5], 2, 7),
    ],
)
def test(arr, k, expected):
    assert max_sub_array_of_size_k(k, arr) == expected
