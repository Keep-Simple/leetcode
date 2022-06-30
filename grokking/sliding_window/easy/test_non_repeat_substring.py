import pytest
from non_repeat_substring import non_repeat_substring, non_repeat_substring_set


@pytest.mark.parametrize(
    "string, expected",
    [
        ("aabccbb", 3),
        ("abbbb", 2),
        ("abccde", 3),
    ],
)
def test(string, expected):
    assert non_repeat_substring(string) == expected
    assert non_repeat_substring_set(string) == expected
