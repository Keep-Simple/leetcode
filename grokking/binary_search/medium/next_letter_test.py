import pytest


def search_next_letter(letters, key):
    """
    Given an array of lowercase letters sorted in ascending order,
    find the smallest letter in the given array greater than a given ‘key’.

    Assume the given array is a circular list,
    which means that the last letter is assumed
    to be connected with the first letter.
    This also means that the smallest letter in the given array
    is greater than the last letter of the array
    and is also the first letter of the array.

    Write a function to return the next letter of the given ‘key’.
    """
    start, end = 0, len(letters) - 1

    while start <= end:
        middle = (start + end) // 2
        if letters[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    return letters[start] if start < len(letters) else letters[0]


@pytest.mark.parametrize(
    "letters, key, expected",
    [
        (["a", "c", "f", "h"], "f", "h"),
        (["a", "c", "f", "h"], "b", "c"),
        (["a", "c", "f", "h"], "m", "a"),
        (["a", "c", "f", "h"], "h", "a"),
        (["c", "f", "h"], "a", "c"),
    ],
)
def test_search_next_letter(letters, key, expected):
    assert search_next_letter(letters, key) == expected
