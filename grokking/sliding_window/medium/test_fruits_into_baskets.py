import pytest
from longest_substring_with_max_k_distinct import \
    longest_substring_with_k_distinct


@pytest.mark.parametrize(
    "fruits,expected",
    [
        (["A", "B", "C", "A", "C"], 3),
        (["A", "B", "C", "B", "B", "C"], 5),
    ],
)
def test(fruits, expected):
    assert longest_substring_with_k_distinct("".join(fruits), 2) == expected
