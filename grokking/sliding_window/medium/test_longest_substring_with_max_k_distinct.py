import pytest
from longest_substring_with_max_k_distinct import \
    longest_substring_with_k_distinct


@pytest.mark.parametrize(
    "string,k,expected",
    [
        ("araaci", 2, 4),
        ("araaci", 1, 2),
        ("cbbebi", 3, 5),
        ("cbbebi", 10, 6),
    ],
)
def test(string, k, expected):
    assert longest_substring_with_k_distinct(string, k) == expected
