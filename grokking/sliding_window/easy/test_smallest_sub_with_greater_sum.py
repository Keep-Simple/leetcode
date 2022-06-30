import pytest
from smallest_sub_with_greater_sum import smallest_subarray_sum


@pytest.mark.parametrize(
    "arr,s,expected",
    [
        ([2, 1, 5, 2, 3, 2], 7, 2),
        ([2, 1, 5, 2, 8], 7, 1),
        ([3, 4, 1, 1, 6], 8, 3),
    ],
)
def test(arr, s, expected):
    assert smallest_subarray_sum(s, arr) == expected
